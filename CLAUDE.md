# django-eventcore

A Django-native transactional-outbox + domain-events library. Emit domain events inside
`transaction.atomic()`; a relay delivers them at-least-once to a broker (NATS JetStream first,
Kafka in v0.2) as CloudEvents, with automatic OpenTelemetry context propagated end-to-end.

> Status: early development (pre-0.1). APIs will change.

## Contributing
- Conventional Commits; clean history.
- Architecture decisions recorded as ADRs in `/adr` (MADR template).
- Tests accompany every feature.
- License: MIT.

## Layout (as it lands)
- `eventcore/` — the library
- `examples/PactFlow/` — document-workflow demo app that emits events through the library
- `adr/` — decision records
