from typing import List

from progrow.layout import Layout
from progrow.row import Row
from progrow.style import Style


class Rows:
    """
    Describes an aligned collection of rows.

    Arguments:
        rows: Rows.
    """

    def __init__(self, rows: List[Row] = []) -> None:
        self.rows = rows

    def append(self, name: str, current: float, maximum: float) -> None:
        """
        Appends a row.

        Arguments:
            name:    Name.
            current: Current value.
            maximum: Maximum value.
        """
        self.rows.append(Row(name=name, maximum=maximum, current=current))

    def calculate_layout(self, style: Style) -> Layout:
        """
        Calculates the layout to ensure rendered values are aligned.

        Arguments:
            style: Style.

        Returns:
            Layout.
        """

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

    def render(self, style: Style = Style()) -> str:
        """
        Renders all the rows to a string.

        Arguments:
            style: Style.

        Returns:
            Rendered rows.
        """

        layout = self.calculate_layout(style)
        rendered = ""

        for row in self.rows:
            rendered += row.render(layout, style) + "\n"

        return rendered
