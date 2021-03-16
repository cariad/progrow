""" Hosts the `Rows` class. """

from typing import List, Optional

from progrow.layout import Layout
from progrow.row import Row
from progrow.style import Style


class Rows:
    """ Describes a collection of rows. """

    def __init__(self, rows: List[Row] = []) -> None:
        self.rows = rows

    def append(self, name: str, current: float, maximum: float) -> None:
        """
        Appends a row.

        `name` describes the name of the row.

        `current` describes the current progress. For example, `3` if 3 out of 7
        units of work are complete.

        `maximum` describes the potential maximum progress. For example, `7` if
        3 out of 7 units of work are complete.
        """
        self.rows.append(Row(name=name, maximum=maximum, current=current))

    def calculate_layout(self, style: Style) -> Layout:
        """ Calculates a layout to align all rows. """

        layout = Layout()

        for row in self.rows:
            name_len = row.render_name(color=False, suffix=style.name_suffix)[1]
            layout.consider_name(name_len)

            if style.show_fraction:
                left_len = row.render_left_fraction(color=False)[1]
                layout.consider_left_fraction(left_len)
                right_len = row.render_right_fraction(color=False)[1]
                layout.consider_right_fraction(right_len)

            if style.show_percent:
                pc_len = row.render_percent(color=False, prefix=style.percent_prefix)[1]
                layout.consider_percent(pc_len)

        return layout

    def render(self, style: Optional[Style] = None) -> str:
        """ Renders the rows. """

        style = style or Style()

        layout = self.calculate_layout(style)
        rendered = ""

        for row in self.rows:
            rendered += row.render(layout, style) + "\n"

        return rendered.rstrip()
