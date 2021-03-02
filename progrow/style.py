from shutil import get_terminal_size
from typing import Optional


class Style:
    """
    Style options.

    Arguments:
        color:         Render in color.
        name_suffix:   String to append after each row's name.
        show_fraction: Include each row's fractional progress.
        show_percent:  Include each row's percentage progress.
        width:         Width to draw.
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
        self.name_suffix = name_suffix
        self.show_fraction = show_fraction
        self.show_percent = show_percent
        self.force_width = width

    @property
    def fraction_prefix(self) -> str:
        """ Gets the string to inject before the fraction. """
        return " "

    @property
    def fraction_separator(self) -> str:
        """ Gets the string to inject between the two parts of the fraction. """
        return " / "

    @property
    def percent_prefix(self) -> str:
        """ Gets the string to inject before the percentage. """
        return " • " if self.show_fraction else " "

    @property
    def width(self) -> int:
        """ Gets the width to draw. """
        if self.force_width:
            return self.force_width
        (width, _) = get_terminal_size((80, 20))
        return width
