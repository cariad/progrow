""" Hosts the `Layout` class. """


from typing import Optional


class Layout:
    """
    Describes the layout of a row.

    This is usually calculated automatically, but you can create a custom layout
    if, for example, you want to render a stream of `Row` instances. The rows
    won't be aligned since the layout cannot be precalculated until all values
    are known, but if you provide your own best-guess layout then the rows will
    (depending on how good your guess is) align.

    `left_fraction_length` describes the length to reserve for the enumerator
    part of the fraction. For example, `3` to accommodate a three-digit value.

    `name_length` describes the length to reserve for the name. For example, `8`
    to accommodate an 8-character name.

    `percent_length` describes the length to reserve for the percentage. For
    example, `3` to accommodate a 2-digit percentage plus the `%` character.

    `right_fraction_length` describes the length to reserve for the denominator
    part of the fraction. For example, `3` to accommodate a three-digit value.
    """

    def __init__(
        self,
        left_fraction_length: Optional[int] = None,
        name_length: Optional[int] = None,
        percent_length: Optional[int] = None,
        right_fraction_length: Optional[int] = None,
    ) -> None:
        self.left_fraction_length = left_fraction_length
        """
        Length to reserve for the enumerator part of the fraction.

        For example, `3` to accommodate a three-digit value.
        """

        self.name_length = name_length
        """
        Length to reserve for the name.

        For example, `8` to accommodate an 8-character name.
        """

        self.percent_length = percent_length
        """
        Length to reserve for the percentage.

        For example, `3` to accommodate a 2-digit percentage plus the `%`
        character.
        """

        self.right_fraction_length = right_fraction_length
        """
        Length to reserve for the denominator part of the fraction.

        For example, `3` to accommodate a three-digit value.
        """

    def consider_left_fraction(self, length: int) -> None:
        """
        Sets `Layout.left_fraction_length` to `length` if `length` is larger.
        """
        self.left_fraction_length = max(self.left_fraction_length or 0, length)

    def consider_name(self, length: int) -> None:
        """
        Sets `Layout.name_length` to `length` if `length` is larger.
        """
        self.name_length = max(self.name_length or 0, length)

    def consider_percent(self, length: int) -> None:
        """
        Sets `Layout.percent_length` to `length` if `length` is larger.
        """
        self.percent_length = max(self.percent_length or 0, length)

    def consider_right_fraction(self, length: int) -> None:
        """
        Sets `Layout.right_fraction_length` to `length` if `length` is larger.
        """
        self.right_fraction_length = max(self.right_fraction_length or 0, length)
