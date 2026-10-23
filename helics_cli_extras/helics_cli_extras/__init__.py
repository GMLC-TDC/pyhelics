"""Deprecated compatibility namespace for the former CLI extras package."""

import warnings

warnings.warn(
    "helics_cli_extras is deprecated and has no functionality; use helics[server] instead",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = []
