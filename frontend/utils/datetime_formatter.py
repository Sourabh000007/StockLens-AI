from datetime import datetime, timezone


def format_relative_date(date_string: str) -> str:
    """
    Convert an ISO timestamp into a human-friendly relative date.
    """

    published = datetime.fromisoformat(
        date_string.replace("Z", "+00:00")
    )

    now = datetime.now(timezone.utc)

    delta = now - published

    if delta.days == 0:

        hours = delta.seconds // 3600

        if hours == 0:
            minutes = delta.seconds // 60
            return f"{minutes} min ago"

        return f"{hours}h ago"

    if delta.days == 1:
        return "Yesterday"

    if delta.days < 7:
        return f"{delta.days} days ago"

    return published.strftime("%b %d, %Y")