# AGENTS.md

Context for AI agents working in this repo.

## What this is

A plain Python 3 script/package with a CLI entry point, generated from the
[cc-py](https://github.com/erujs/cc-py) `python-script` template.

## Structure

```
caffeine_py/
├── __init__.py
└── main.py     # entry point, exposes main()
tests/
└── test_main.py
```

- `main()` in `main.py` is wired as the console script entry point in
  `pyproject.toml` (`[project.scripts]`) — running `caffeine_py`
  after install calls it directly.
- Keep the package flat unless the script grows enough logic to warrant
  submodules; don't add layers (services/, utils/, etc.) speculatively.

## Testing

```bash
pytest
```

`tests/test_main.py` uses `capsys` to assert on stdout — follow that
pattern for new CLI behavior rather than introducing a mocking framework.
