def format_large_number(
    value: float | int | None,
) -> str:
    """
    Convert a large number into a human-readable format.
    """

    if value is None:
        return "-"

    abs_value = abs(value)

    if abs_value >= 1_000_000_000_000:
        return f"{value / 1_000_000_000_000:.2f}T"

    if abs_value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f}B"

    if abs_value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"

    if abs_value >= 1_000:
        return f"{value / 1_000:.2f}K"

    return f"{value:,.0f}"