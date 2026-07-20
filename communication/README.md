# JARVIS Communication Subsystem

Decoupled messaging system containing:
- **Event Model**: Standard UUID, timestamped event payload schemas.
- **Event Bus**: In-memory subscription/publisher routing registry.
- **Queue**: Asynchronous FIFO processing buffer using `asyncio.Queue`.
- **Dead Letter Queue (DLQ)**: Failure registry for unresolvable event handler crashes.
