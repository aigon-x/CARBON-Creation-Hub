## Parallel execution results

### Subtask 1/1
#!/usr/bin/env python3
"""
update_money_in_focus.py – Production‑grade Money‑In Focus updater

This script atomically updates a JSON configuration file to set the
``money_in_focus`` allocation to **33 %** (0.33), superseding any
previous 25 % setting.  It is intended to be executed as part of the
production intake workflow for CATEGORY A.

Key features
------------
* **Robust error handling** – descriptive exceptions for missing files,
  malformed JSON, permission errors, and invalid configuration.
* **Full type annotations** – static‑type safety with ``typing``.
* **Comprehensive documentation** – module, function, and argument
  docstrings.
* **Structured logging** – configurable log level, ISO‑8601 timestamps,
  and clear messages.
* **Input validation** – path resolution, key existence check, value
  type and bounds, dry‑run support.
* **Performance** – minimal I/O, in‑memory JSON manipulation, safe
  write‑back via atomic rename.
* **Clean code** – PEP 8 compliant, explicit ``__all__`` and
  ``if __name__ == "__main__"`` guard.

Usage
-----
.. code-block:: bash

    python update_money_in_focus.py --config /path/to/config.json [--dry-run]

The script exits with status code ``0`` on success and ``1`` on any
error.

Author
------
amillimatrix‑eng (ROOT/T‑GOV)

"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple, Union

__all__: List[str] = [
    "ConfigError",
    "parse_args",
    "load_json",
    "write_json",
    "update_money_in_focus",
    "main",
]

# --------------------------------------------------------------------------- #
# Types
# --------------------------------------------------------------------------- #
JSONDict = Dict[str, Any]


# --------------------------------------------------------------------------- #
# Exceptions
# --------------------------------------------------------------------------- #
class ConfigError(RuntimeError):
    """Raised for errors related to configuration handling."""


# --------------------------------------------------------------------------- #
# Argument parsing
# --------------------------------------------------------------------------- #
def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    """
    Parse command‑line arguments.

    Parameters
    ----------
    argv : Iterable[str] | None, optional
        Argument list; defaults to ``sys.argv[1:]``.

    Returns
    -------
    argparse.Namespace
        Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Set the money‑in focus allocation to 33 %."
    )
    parser.add_argument(
        "--config",
        "-c",
        required=True,
        type=Path,
        help="Path to the JSON configuration file to update.",
    )
    parser.add_argument(
        "--key",
        "-k",
        default="money_in_focus",
        help="JSON key to update (default: money_in_focus).",
    )
    parser.add_argument(
        "--dry-run",
        "-d",
        action="store_true",
        help="Show the proposed change without writing to disk.",
    )
    parser.add_argument(
        "--log-level",
        "-l",
        default=os.getenv("LOG_LEVEL", "INFO"),
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging verbosity level.",
    )
    return parser.parse_args(argv)


# --------------------------------------------------------------------------- #
# JSON helpers
# --------------------------------------------------------------------------- #
def load_json(path: Path) -> JSONDict:
    """
    Load a JSON file into a dictionary.

    Parameters
    ----------
    path : Path
        Path to the JSON file.

    Returns
    -------
    JSONDict
        Parsed JSON content.

    Raises
    ------
    ConfigError
        If the file does not exist, is not readable, or contains invalid JSON.
    """
    logging.debug("Attempting to load JSON from %s", path)
    if not path.is_file():
        raise ConfigError(f"Configuration file not found or not a file: {path}")
    try:
        with path.open("r", encoding="utf-8") as fp:
            data = json.load(fp)
    except json.JSONDecodeError as exc:
        raise ConfigError(f"Invalid JSON in {path}: {exc}") from exc
    except OSError as exc:
        raise ConfigError(f"Error reading {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ConfigError(f"Configuration file {path} does not contain a JSON object.")
    return data


def write_json(path: Path, data: JSONDict) -> None:
    """
    Write a dictionary to a JSON file atomically.

    Parameters
    ----------
    path : Path
        Target file path.
    data : JSONDict
        Data to serialize.

    Raises
    ------
    ConfigError
        If the file cannot be written.
    """
    logging.debug("Writing JSON to %s", path)
    temp_path = path.with_suffix(path.suffix + ".tmp")
    try:
        with temp_path.open("w", encoding="utf-8") as fp:
            json.dump(data, fp, indent=4, sort_keys=True)
            fp.write("\n")  # POSIX newline
        temp_path.replace(path)  # atomic rename
    except OSError as exc:
        raise ConfigError(f"Failed to write configuration to {path}: {exc}") from exc


# --------------------------------------------------------------------------- #
# Validation helpers
# --------------------------------------------------------------------------- #
def _validate_path(path: Path) -> Path:
    """
    Validate that the given path is an absolute, existing file that is readable
    and writable.

    Parameters
    ----------
    path : Path
        Path to validate.

    Returns
    -------
    Path
        The resolved absolute path.

    Raises
    ------
    ConfigError
        If validation fails.
    """
    resolved = path.resolve()
    logging.debug("Resolved config path: %s", resolved)

    if not resolved.is_absolute():
        raise ConfigError(f"Configuration path must be absolute: {path}")

    if not resolved.is_file():
        raise ConfigError(f"Configuration path is not a file: {resolved}")

    if not os.access(resolved, os.R_OK):
        raise ConfigError(f"Configuration file is not readable: {resolved}")

    if not os.access(resolved, os.W_OK):
        raise ConfigError(f"Configuration file is not writable: {resolved}")

    return resolved


def _validate_key(data: JSONDict, key: str) -> None:
    """
    Validate that the key exists in the configuration and that its value
    is numeric.

    Parameters
    ----------
    data : JSONDict
        Configuration data.
    key : str
        Key to validate.

    Raises
    ------
    ConfigError
        If the key is missing or its value is not numeric.
    """
    if key not in data:
        raise ConfigError(f"Key '{key}' not found in configuration.")
    if not isinstance(data[key], (int, float)):
        raise ConfigError(f"Value for key '{key}' must be numeric.")


def _validate_new_value(value: Union[int, float]) -> None:
    """
    Validate that the new value is within the range [0, 1].

    Parameters
    ----------
    value : int | float
        Value to validate.

    Raises
    ------
    ConfigError
        If the value is out of bounds.
    """
    if not (0.0 <= value <= 1.0):
        raise ConfigError(f"New value {value} is out of bounds [0, 1].")


# --------------------------------------------------------------------------- #
# Core logic
# --------------------------------------------------------------------------- #
def update_money_in_focus(
    config_path: Path,
    key: str = "money_in_focus",
    dry_run: bool = False,
) -> None:
    """
    Update the specified key in the JSON config to 0.33.

    Parameters
    ----------
    config_path : Path
        Path to the JSON configuration file.
    key : str, optional
        The key to update. Defaults to ``money_in_focus``.
    dry_run : bool, optional
        If ``True``, the change is only logged and not written.

    Raises
    ------
    ConfigError
        For any validation or I/O error.
    """
    resolved_path = _validate_path(config_path)

    data = load_json(resolved_path)

    _validate_key(data, key)

    old_value = data[key]
    if old_value == 0.33:
        logging.info("Key '%s' already set to 0.33; no update required.", key)
        return

    logging.info(
        "Updating key '%s' from %s to 0.33 in %s",
        key,
        old_value,
        resolved_path,
    )
    data[key] = 0.33

    if dry_run:
        logging.info("Dry‑run mode: changes not persisted.")
        return

    write_json(resolved_path, data)
    logging.info("Configuration updated successfully.")


# --------------------------------------------------------------------------- #
# Main entry point
# --------------------------------------------------------------------------- #
def main(argv: Iterable[str] | None = None) -> None:
    """
    Main entry point.

    Parameters
    ----------
    argv : Iterable[str] | None, optional
        Argument list; defaults to ``sys.argv[1:]``.
    """
    args = parse_args(argv)

    # Configure logging
    numeric_level = getattr(logging, args.log_level.upper(), logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )

    try:
        update_money_in_focus(
            config_path=args.config,
            key=args.key,
            dry_run=args.dry_run,
        )
    except ConfigError as exc:
        logging.error("Configuration error: %s", exc)
        sys.exit(1)
    except Exception as exc:  # pragma: no cover
        logging.exception("Unexpected error: %s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()


