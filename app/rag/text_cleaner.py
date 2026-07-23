import re


class TextCleaner:
    """
    Cleans parsed annual report text.
    """

    def clean(
        self,
        text: str,
    ) -> str:

        text = self._remove_html_comments(text)

        text = self._replace_html_breaks(text)

        text = self._normalize_whitespace(text)

        return text

    def _remove_html_comments(
        self,
        text: str,
    ) -> str:

        return re.sub(
            r"<!--.*?-->",
            "",
            text,
            flags=re.DOTALL,
        )

    def _replace_html_breaks(
        self,
        text: str,
    ) -> str:

        return re.sub(
            r"<br\s*/?>",
            " ",
            text,
            flags=re.IGNORECASE,
        )

    def _normalize_whitespace(
        self,
        text: str,
    ) -> str:

        text = re.sub(
            r"[ \t]+",
            " ",
            text,
        )

        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text,
        )

        return text.strip()