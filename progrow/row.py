from math import floor
from typing import Optional, Tuple

import colorama

from progrow.layout import Layout
from progrow.style import Style


class Row:
    """
    Describes a row.

    Arguments:
        name:    Name.
        current: Current value.
        maximum: Maximum value.
    """

    def __init__(self, name: str, current: float, maximum: float) -> None:
        self.name = name
        self.maximum = maximum
        self.current = current

    @property
    def percent(self) -> float:
        """ Gets the percentage of this row's current value. """
        return (1.0 / self.maximum) * self.current

    def render(self, layout: Layout = Layout(), style: Style = Style()) -> str:
        """
        Renders the row to a string.

        Arguments:
            layout: Layout.
            style:  Style.

        Returns:
            Rendered row.
        """

        name, name_len = self.render_name(
            color=style.color,
            suffix=style.name_suffix,
            length=layout.name_length,
        )

        if style.show_fraction:
            fraction, fraction_len = self.render_fraction(
                color=style.color,
                prefix=style.fraction_prefix,
                separator=style.fraction_separator,
                left_length=layout.left_fraction_length,
                right_length=layout.right_fraction_length,
            )
        else:
            fraction = ""
            fraction_len = 0

        if style.show_percent:
            percent, percent_len = self.render_percent(
                color=style.color,
                prefix=style.percent_prefix,
                length=layout.percent_length,
            )
        else:
            percent = ""
            percent_len = 0

        bar = self.render_bar(
            color=style.color,
            length=style.width - name_len - fraction_len - percent_len,
        )

        return (name + bar + fraction + percent).rstrip()

    def render_bar(self, color: bool, length: int) -> str:
        """
        Renders the progress bar to a string.

        Arguments:
            color:  Render in color.
            length: Length to draw to.
        """

        s = ""

        if color:
            s += str(colorama.Fore.GREEN)

        pc_per_block = 1.0 / length
        remaining_percent = self.percent

        for _ in range(length):
            this_pc = min(1.0, (1.0 / pc_per_block) * remaining_percent)
            remaining_percent -= min(remaining_percent, pc_per_block)
            s += " " if this_pc == 0.0 else chr(0x258F - floor(this_pc / (1.0 / 7)))

        if color:
            s += str(colorama.Fore.RESET)

        return s

    def render_fraction(
        self,
        color: bool,
        prefix: str,
        separator: str,
        left_length: Optional[int] = None,
        right_length: Optional[int] = None,
    ) -> Tuple[str, int]:
        """
        Renders the fraction to a string.

        Arguments:
            color:        Render in color.
            left_length:  Optional length to pad the left number to.
            separator:    String to separate the two numbers.
            prefix:       Prefix to inject before the left numbers.
            right_length: Optional length to pad the right number to.
        """

        s = (
            prefix
            + self.render_left_fraction(color=color, length=left_length)[0]
            + separator
            + self.render_right_fraction(color=color, length=right_length)[0]
        )

        if color:
            length = self.render_fraction(
                color=False,
                prefix=prefix,
                separator=separator,
                left_length=left_length,
                right_length=right_length,
            )[1]
        else:
            length = len(s)

        return (s, length)

    def render_left_fraction(
        self,
        color: bool,
        length: Optional[int] = None,
    ) -> Tuple[str, int]:
        """
        Renders the left fraction to a string.

        Arguments:
            color:  Render in color.
            length: Optional length to pad the number to.
        """

        s = ""

        if color:
            s += str(colorama.Fore.LIGHTBLUE_EX)

        if length:
            s += f"{self.current:,}".rjust(length)
        else:
            s += f"{self.current:,}"

        if color:
            s += str(colorama.Fore.RESET)

        if color:
            length = self.render_left_fraction(color=False)[1]
        else:
            length = len(s)

        return (s, length)

    def render_name(
        self,
        color: bool,
        suffix: str,
        length: Optional[int] = None,
    ) -> Tuple[str, int]:
        """
        Renders the name to a string.

        Arguments:
            color:  Render in color.
            suffix: Suffix.
            length: Optional length to pad the name to.
        """

        s = ""

        if length and len(self.name + suffix) > length:
            if len(self.name) < length:
                inc_suffix = suffix[0 : length - len(self.name)]
                inc_name = self.name
            else:
                inc_suffix = ""
                inc_name = self.name[0:length]
        else:
            inc_name = self.name
            inc_suffix = suffix

        if color:
            s += str(colorama.Fore.YELLOW)

        s += inc_name

        if color:
            s += str(colorama.Fore.RESET)

        s += inc_suffix

        if length:
            padding = length - len(inc_name) - len(inc_suffix)
            s += " " * padding
        elif color:
            length = self.render_name(color=False, suffix=suffix)[1]
        else:
            length = len(s)

        return (s, length)

    def render_percent(
        self,
        color: bool,
        prefix: str,
        length: Optional[int] = None,
    ) -> Tuple[str, int]:
        """
        Renders the fraction to a string.

        Arguments:
            color:  Render in color.
            prefix: Prefix to inject before the percentage.
            length: Optional length to pad the percentage to.
        """

        s = prefix

        if color:
            s += str(colorama.Fore.CYAN)

        percent = str(floor(self.percent * 100)) + "%"

        if length:
            numeric_pad = length - len(prefix)
            s += percent[0:numeric_pad].rjust(numeric_pad)
        else:
            s += percent

        if color:
            s += str(colorama.Fore.RESET)

        if color:
            length = self.render_percent(color=False, prefix=prefix, length=length)[1]
        else:
            length = len(s)

        return (s, length)

    def render_right_fraction(
        self,
        color: bool,
        length: Optional[int] = None,
    ) -> Tuple[str, int]:
        """
        Renders the right fraction to a string.

        Arguments:
            color:  Render in color.
            length: Optional length to pad the number to.
        """

        s = ""

        if color:
            s += str(colorama.Fore.LIGHTBLUE_EX)

        if length:
            s += f"{self.maximum:,}".rjust(length)
        else:
            s += f"{self.maximum:,}"

        if color:
            s += str(colorama.Fore.RESET)

        if color:
            length = self.render_right_fraction(color=False)[1]
        else:
            length = len(s)

        return (s, length)
