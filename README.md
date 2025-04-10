# Inline snapshot pytester repro

- run with `uv run pytest --inline-snapshot=create` and see that it does not create a snapshot
- comment out `test_pytester` and see that it now works.
