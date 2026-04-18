# ARCHITECTURE.md — ATTICUS MPO

## Overview

ATTICUS is a governed multi-provider AI orchestrator with a Tkinter desktop operator console. The architecture is intentionally layered and flat to keep imports predictable, testing practical, and provider logic separate from UI code.

Current baseline: **v5.0.0b6** — Schema: **v8** — Framework: **ATTICUS v6.4.1-HCII**

---

## Package Structure

```
atticus/
├── main.py
├── core/
│   ├── types.py                # APP_VERSION, FRAMEWORK_VERSION, enums, protocols, typed dicts
│   ├── errors.py               # Exception hierarchy
│   ├── logging_config.py       # Structured logging setup
│   ├── env_diagnostics.py      # Runtime environment inspector
│   ├── memory_cells.py         # Typed cell definitions, registry, packs, prompt compilation
│   ├── trace_context.py        # Thread-local correlation context [PROTECTED]
│   ├── session.py              # WorkerSession: headless execution model [PROTECTED]
│   └── component_identity.py   # ComponentInfo registry, IntrospectionService
├── persistence/
│   ├── config_store.py         # Config read/write with SecretStr
│   ├── migrations.py           # Schema migration chain [PROTECTED]
│   ├── path_migration.py       # Legacy path copy-migration
│   └── sqlite_store.py         # Session/transcript persistence [PROTECTED]
├── providers/
│   ├── base.py                 # Abstract provider interface
│   ├── model_catalog.py        # Structured catalog service
│   ├── openai_provider.py      # OpenAI adapter
│   ├── anthropic_provider.py   # Anthropic adapter
│   ├── gemini_provider.py      # Gemini adapter
│   ├── ollama_provider.py      # Ollama adapter
│   └── registry.py             # Provider factory and capability resolution
├── plugins/
│   ├── base.py                 # Plugin abstractions
│   ├── registry.py             # Plugin registry
│   └── builtins/               # Built-in plugins (CodeRunner, etc.)
├── services/
│   ├── orchestrator.py         # OrchestratorState, run-phase tracking
│   ├── transcript_manager.py   # Authoritative in-memory transcript source of truth
│   ├── session_turn_adapter.py # ProviderTurnAdapter, typed turn conversion
│   ├── viewmodel.py            # UI state boundary (WorkbenchViewModel)
│   ├── cost_service.py         # Token cost attribution
│   ├── tts_service.py          # Text-to-speech pipeline
│   └── audit_service.py        # Durable audit trail [PROTECTED]
├── ui/
│   ├── app.py                  # Tkinter operator console, button handlers, render loop
│   ├── settings_dialog.py      # Settings panel
│   └── boot_screen.py          # Launch screen
└── tests/
    ├── test_session_seed_speaker_fidelity.py
    ├── test_bridge_auto_seed_continuity.py
    ├── test_mission_result_fallback.py
    ├── test_stream_epoch.py
    ├── test_committed_boundary_mark.py
    ├── test_session_status_restoration.py
    ├── test_recovery_sentinel.py
    └── ...
```

Items marked `[PROTECTED]` must not be modified without explicit sprint scope authorization (see `DEV_LIFECYCLE.md`).

---

## Layer Responsibilities

| Layer | Responsibility | Boundary Rule |
|-------|---------------|---------------|
| `core/` | Types, errors, logging, environment diagnostics, memory cells, trace context | No provider or UI networking logic |
| `persistence/` | Config, path migration, SQLite session storage | Canonical runtime path is `~/.atticus/` |
| `providers/` | Provider adapters, registry, model catalogs, capability resolution | Live/cache/fallback model selection happens here |
| `plugins/` | Plugin abstractions and builtins | Unsafe tools stay default-off |
| `services/` | Orchestration, transcript state, viewmodel assembly, routing, cost, TTS | No Tk widgets |
| `ui/` | Tkinter operator console | Renders state and dispatches actions only |

---

## Runtime Flow: Top-Down Stack

```
┌──────────────────────────────────────────────────────────────┐
│                        OPERATOR SURFACE                      │
│                      Tkinter Desktop UI                      │
│                    ui/app.py, settings_dialog.py             │
└──────────────────────────┬───────────────────────────────────┘
                           │ button handlers, render loop
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                    VIEW / CONTROL LAYER                      │
│         ViewModel, control flow, session/run-state glue      │
│                     services/viewmodel.py                    │
└──────────────────────────┬───────────────────────────────────┘
                           │ state queries, action dispatch
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                 ORCHESTRATION / SERVICE LAYER                │
│       TranscriptManager, Orchestrator, Cost, TTS, Audit      │
│                    services/*.py                             │
└──────────────────────────┬───────────────────────────────────┘
                           │ turn execution, provider calls
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                     PROVIDER LAYER                           │
│     OpenAI, Anthropic, Gemini, Ollama adapters + registry    │
│                    providers/*.py                            │
└──────────────────────────┬───────────────────────────────────┘
                           │ persistence, config
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                    PERSISTENCE LAYER                         │
│          SQLite store, config store, migrations              │
│                    persistence/*.py                          │
└──────────────────────────────────────────────────────────────┘
```

---

## Canonical Send Path

After the Recovery Program (Phases 1–6), there is **one authoritative send path** for all user-initiated turns:

1. **UI action** (Send button, Bridge Step, Bridge Auto) → calls into `ui/app.py` handlers
2. **Seed construction** → `TranscriptManager.get_committed_typed_turns()` provides the canonical conversation history
3. **WorkerSession construction** → `WorkerSession` receives `seed_turns` as read-only context
4. **Provider dispatch** → `ProviderTurnAdapter.adapt_typed()` converts typed turns to provider format
5. **Provider call** → The appropriate provider adapter executes the API call
6. **Transcript commit** → Response committed through `TranscriptManager`
7. **UI render** → `_render_active_tail` projects the committed transcript to the Tk widget

Key invariants:
- All send paths (manual, Bridge Step, Bridge Auto) seed through `TranscriptManager`
- Seed turns are read-only; old turns are never re-committed as new turns
- The legacy ConversationService queue spine (`_start_turn`, `_process_queue`, `_handle_message`) has been removed (Phase 6)
- WorkerSession is the sole execution model

---

## Provider Pipeline

### Model Selection

For each provider (OpenAI, Anthropic, Gemini, Ollama), ATTICUS resolves models using:

1. **Live discovery** from the provider API when credentials are available
2. **Cached last-known-good catalog** in `~/.atticus/model_cache.json`
3. **Hardcoded fallback catalog** bundled with the app

The UI displays human-readable labels where metadata exists, but ATTICUS always preserves the actual `model_id` for request execution.

### Provider Registry

`providers/registry.py` owns provider construction. The registry and capability resolution layer determine how model families map to provider behavior. Provider-family logic stays out of the UI and orchestration layers.

### Sampling Safety Envelope

Provider sampling parameters (temperature, top_p) are resolved through a safety envelope that enforces resolver exclusivity. The sampling resolver is the authoritative source; deprecated `effective_temperature()`/`effective_top_p()` helpers are scheduled for removal.

---

## Memory-Cell System

`core/memory_cells.py` contains typed memory cell definitions, a builtin registry, pack definitions, and prompt compilation logic.

Current baseline inventory: 27 builtin cells, 7 packs (including ATTICUS v6.4.1 Governance and Full Stack packs).

Provider prompts are assembled from: locked runtime cells → selected packs/cells → provider shims → operator notes → current objective.

---

## Transcript Management

`services/transcript_manager.py` is the **authoritative in-memory source of truth** for conversation state. The UI is a pure projection layer that renders from `TranscriptManager` state.

Key mechanisms:
- `_stream_epoch` counter prevents stale render interference during streaming
- `committed_end_mark` at `"end-1c"` prevents preview tattooing
- `get_committed_typed_turns()` provides the canonical seed for new sessions

---

## Observability

The observability spine (delivered in beta.2/b5) provides:
- **ComponentInfo registry** — in-memory component identity and metadata
- **IntrospectionService** — on-demand debug snapshots
- **Debug fingers** — metadata-only `trace_fields` logging across 24 classes
- **Ambient trace context** — `core/trace_context.py` propagated across UI, transcript manager, and worker thread boundaries

Instrumentation stages: on-demand (current) → per-turn (current) → continuous (deferred, requires performance measurement).

---

## Persistence

ATTICUS stores config, model cache, logs, and transcripts under `~/.atticus/`.

- Legacy migration from `~/.dual_llm_workbench/` is copy-based and non-destructive
- Schema version is tracked in a `schema_version` table (currently v8)
- Profile export is non-secret by default

---

## Security Boundary Notes

Full details in `SECURITY.md`. Summary:
- Secrets wrapped in `SecretStr`; raw access only through explicit getters
- Provider/business logic stays outside Tkinter
- No hidden widgets as long-term state storage
- Unsafe code runner flows remain opt-in and environment-gated
- Deny-by-default key storage: env vars → OS keyring → explicit insecure plaintext fallback
