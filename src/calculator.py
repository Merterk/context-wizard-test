from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CalculatorConfig:
    """Configuration for Calculator."""
    max_abs_result: int = 1_000_000


class Calculator:
    """A small calculator with simple validation."""

    def __init__(self, config: CalculatorConfig | None = None) -> None:
        self._config = config or CalculatorConfig()

    def add(self, left: int, right: int) -> int:
        """Return the sum of two integers."""
        result = left + right
        return self._clamp(result)

    def subtract(self, left: int, right: int) -> int:
        """Return the difference of two integers."""
        result = left - right
        return self._clamp(result)

    def _clamp(self, value: int) -> int:
        """Clamp value to configured bounds."""
        limit = self._config.max_abs_result
        if value > limit:
            return limit
        if value < -limit:
            return -limit
        return value
