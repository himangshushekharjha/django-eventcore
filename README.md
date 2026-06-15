# django-eventcore

Outbox-backed domain events for Django — at-least-once delivery to NATS JetStream (Kafka next),
CloudEvents on the wire, and automatic OpenTelemetry trace propagation request → broker → consumer.

**Status:** early development. Building in public.

## Quickstart (local dev)

Requires Python 3.12 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

Then visit `http://127.0.0.1:8000/admin/` and log in with the superuser you just created.

Run the test suite and linter with:

```bash
uv run pytest
uv run ruff check
```
