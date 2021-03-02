from typing import Optional


class Layout:
    """
    Row layout.

    Arguments:
        left_fraction_length:  Length of the "current" part of the fraction. For
                               example, `3` to accommodate a three-digit value.

        name_length:           Length of the name column. For example, `10` to
                               accommodate a ten-character name.

        percent_length:        Length of the percentage column. For example, `3`
                               to accommodate a two-digit value plus `%` symbol.

        right_fraction_length: Length of the "maximum" part of the fraction. For
                               example, `3` to accommodate a three-digit value.
    """

    def __init__(
        self,
        left_fraction_length: Optional[int] = None,
        name_length: Optional[int] = None,
        percent_length: Optional[int] = None,
        right_fraction_length: Optional[int] = None,
    ) -> None:
        self.left_fraction_length = left_fraction_length
        self.name_length = name_length
        self.percent_length = percent_length
        self.right_fraction_length = right_fraction_length

    def consider_left_fraction(self, consider: int) -> None:
        """
        Considers a left fraction as potentially the longest.

        Arguments:
            consider: Length to consider.
        """
        self.left_fraction_length = max(self.left_fraction_length or 0, consider)

    def consider_name(self, consider: int) -> None:
        """
        Considers a name as potentially the longest.

        Arguments:
            consider: Length to consider.
        """
        self.name_length = max(self.name_length or 0, consider)

    def consider_percent(self, consider: int) -> None:
        """
        Considers a percentage as potentially the longest.

        Arguments:
            consider: Length to consider.
        """
        self.percent_length = max(self.percent_length or 0, consider)

    def consider_right_fraction(self, consider: int) -> None:
        """
        Considers a right fraction as potentially the longest.

        Arguments:
            consider: Length to consider.
        """
        self.right_fraction_length = max(self.right_fraction_length or 0, consider)
