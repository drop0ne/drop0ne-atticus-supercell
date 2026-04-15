# Operating Model

## Intent

This repository is operated as a cross-model authoritative memory root.

## Primary uses

- store compact long-term memory cells
- publish current normalized state
- mirror selected doctrine and repo state
- generate session bootstrap packets

## Model interaction rule

Models should read from this repository as a bounded memory surface and write only structured, relevant long-term memory artifacts.

## Non-goals

- replacing project-local code repos
- storing every raw chat as canon
- allowing unstructured drift to define long-term memory
