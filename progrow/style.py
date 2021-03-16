""" Hosts the `Style` class. """

from shutil import get_terminal_size
from typing import Optional


class Style:
    """
    Rendering style options.

    `color` describes whether to render in colour or plain text.

    `name_suffix` describes the string to append to the name.

    `show_fraction` describes whether or not to include fractions.

    `show_percent` describes whether or not to include percentages.

    `width` describes the width to render to.
    """

    def __init__(
        self,
        color: bool = True,
        name_suffix: str = " ",
        show_fraction: bool = False,
        show_percent: bool = False,
        width: Optional[int] = None,
    ) -> None:
        self.color = color
        """ Whether to render in colour or plain text. """

        self.name_suffix = name_suffix
        """ String to append to the name. """

        self.show_fraction = show_fraction
        """ Whether or not to include fractions. """

        self.show_percent = show_percent
        """ Whether or not to include percentages. """

        self.force_width = width
        """ Width to render to. """

    @property
    def fraction_prefix(self) -> str:
        """ String to inject before the fraction. """
        return " "

    @property
    def fraction_separator(self) -> str:
        """ String to inject between the enumerator and denominator. """
        return " / "

    @property
    def percent_prefix(self) -> str:
        """ String to inject before percentages. """
        return " • " if self.show_fraction else " "

    @property
    def width(self) -> int:
        """
        Actual width to render to. The terminal width if no other width was
        requested.
        """
        if self.force_width:
            return self.force_width
        (width, _) = get_terminal_size((80, 20))
        return width
