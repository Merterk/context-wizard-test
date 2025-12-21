Project Conventions
===================

Naming
------

- Functions must be snake_case.
- Constants must be UPPER_SNAKE_CASE.
- Avoid single-letter variable names except in very small loops.
- Public functions should have docstrings in Google style.

Error handling
--------------

- Do not swallow exceptions. Either re-raise or wrap with a clearer exception.
- Log errors with context; do not print.

Architecture
------------

- Core logic lives in a pure function; keep I/O separate.
- Avoid hidden global state.
