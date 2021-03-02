from typing import Optional, Tuple

from pytest import mark

from progrow.layout import Layout
from progrow.row import Row
from progrow.style import Style

fraction_part_test_cases = [
    (0, False, None, ("0", 1)),
    (1, False, None, ("1", 1)),
    (1.2, False, None, ("1.2", 3)),
    (-3.4, False, None, ("-3.4", 4)),
]


@mark.parametrize(
    "row, style, layout, expect",
    [
        (
            Row(name="foo", maximum=9, current=1),
            Style(color=False, width=40),
            Layout(),
            "foo ████",
        ),
        (
            Row(name="foo", maximum=9, current=1),
            Style(color=False, show_fraction=True, width=40),
            Layout(),
            "foo ███▍                           1 / 9",
        ),
        (
            Row(name="foo", maximum=9, current=1),
            Style(color=False, show_percent=True, width=40),
            Layout(),
            "foo ███▌                             11%",
        ),
        (
            Row(name="foo", maximum=9, current=1),
            Style(color=False, show_fraction=True, show_percent=True, width=40),
            Layout(),
            "foo ██▋                      1 / 9 • 11%",
        ),
        (
            Row(name="foo", maximum=9, current=1),
            Style(color=True, show_fraction=True, show_percent=True, width=40),
            Layout(),
            (
                "\x1b[33mfoo\x1b[39m \x1b[32m██▋                     "
                + "\x1b[39m \x1b[94m1\x1b[39m / \x1b[94m9\x1b[39m • "
                + "\x1b[36m11%\x1b[39m"
            ),
        ),
    ],
)
def test_to_string(row: Row, style: Style, layout: Layout, expect: str) -> None:
    assert row.render(layout, style) == expect


@mark.parametrize(
    "current, maximum, color, length, expect",
    [
        (0, 16, False, 2, "  "),  # 0/8
        (1, 16, False, 2, "▏ "),  # 1/8
        (2, 16, False, 2, "▎ "),  # 2/8
        (3, 16, False, 2, "▍ "),  # 3/8
        (4, 16, False, 2, "▌ "),  # 4/8
        (5, 16, False, 2, "▋ "),  # 5/8
        (6, 16, False, 2, "▊ "),  # 6/8
        (7, 16, False, 2, "▉ "),  # 7/8
        (8, 16, False, 2, "█ "),  # 8/8
        (9, 16, False, 2, "█▏"),  # 8/8 + 1/8
        (10, 16, False, 2, "█▎"),  # 8/8 + 2/8
        (11, 16, False, 2, "█▍"),  # 8/8 + 3/8
        (12, 16, False, 2, "█▌"),  # 8/8 + 4/8
        (13, 16, False, 2, "█▋"),  # 8/8 + 5/8
        (14, 16, False, 2, "█▊"),  # 8/8 + 6/8
        (15, 16, False, 2, "█▉"),  # 8/8 + 7/8
        (16, 16, False, 2, "██"),  # 8/8 + 8/8
        (0.5, 1, True, 2, "\x1b[32m█ \x1b[39m"),
    ],
)
def test_render_bar(
    current: float, maximum: float, color: bool, length: int, expect: str
) -> None:
    row = Row("foo", current=current, maximum=maximum)
    assert row.render_bar(color=color, length=length) == expect


@mark.parametrize(
    "left, right, color, prefix, separator, left_length, right_length, expect",
    [
        (0, 1, False, "", "", None, None, ("01", 2)),
        (0, 1, False, "=", "/", None, None, ("=0/1", 4)),
        (0, 1, True, "=", "/", None, None, ("=\x1b[94m0\x1b[39m/\x1b[94m1\x1b[39m", 4)),
        (0, 1, False, "=", "/", 3, 2, ("=  0/ 1", 7)),
        (
            0,
            1,
            True,
            "=",
            "/",
            3,
            2,
            ("=\x1b[94m  0\x1b[39m/\x1b[94m 1\x1b[39m", 7),
        ),
    ],
)
def test_render_fraction(
    left: float,
    right: float,
    color: bool,
    prefix: str,
    separator: str,
    left_length: Optional[int],
    right_length: Optional[int],
    expect: str,
) -> None:
    row = Row("foo", current=left, maximum=right)
    actual = row.render_fraction(
        color=color,
        prefix=prefix,
        separator=separator,
        left_length=left_length,
        right_length=right_length,
    )
    assert actual == expect


@mark.parametrize(
    "maximum, current, expect",
    [
        (50, 25, 0.5),
        (3, 2, 0.6666666666666666),
    ],
)
def test_percent(maximum: float, current: float, expect: float) -> None:
    assert Row("foo", maximum=maximum, current=current).percent == expect


@mark.parametrize("value, color, length, expect", fraction_part_test_cases)
def test_render_left_fraction(
    value: float,
    color: bool,
    length: Optional[int],
    expect: str,
) -> None:
    row = Row("foo", current=value, maximum=value + 1.0)
    assert row.render_left_fraction(color=color, length=length) == expect


@mark.parametrize(
    "name, color, suffix, length, expect",
    [
        ("foo", False, "", None, ("foo", 3)),
        ("foo", False, "doo", 4, ("food", 4)),
        ("foo", False, "", 2, ("fo", 2)),
        ("foo", False, "", 5, ("foo  ", 5)),
        ("foo", True, "", None, ("\x1b[33mfoo\x1b[39m", 3)),
        ("foo", True, "bar", 4, ("\x1b[33mfoo\x1b[39mb", 4)),
        ("foo", True, "", 2, ("\x1b[33mfo\x1b[39m", 2)),
        ("foo", True, "", 5, ("\x1b[33mfoo\x1b[39m  ", 5)),
    ],
)
def test_render_name(
    name: str,
    color: bool,
    suffix: str,
    length: Optional[int],
    expect: Tuple[str, int],
) -> None:
    row = Row(name, current=0, maximum=1)
    assert row.render_name(color=color, suffix=suffix, length=length) == expect


@mark.parametrize(
    "current, maximum, color, prefix, length, expect",
    [
        (0, 11, False, "", None, ("0%", 2)),
        (1, 11, False, "", None, ("9%", 2)),
        (2, 11, False, "", None, ("18%", 3)),
        (3, 11, False, "", None, ("27%", 3)),
        (4, 11, False, "", None, ("36%", 3)),
        (5, 11, False, "", None, ("45%", 3)),
        (6, 11, False, "", None, ("54%", 3)),
        (7, 11, False, "", None, ("63%", 3)),
        (8, 11, False, "", None, ("72%", 3)),
        (9, 11, False, "", None, ("81%", 3)),
        (10, 11, False, "", None, ("90%", 3)),
        (11, 11, False, "", None, ("100%", 4)),
    ],
)
def test_render_percent(
    current: float,
    maximum: float,
    color: bool,
    prefix: str,
    length: Optional[int],
    expect: str,
) -> None:
    row = Row("foo", current=current, maximum=maximum)
    actual = row.render_percent(
        color=color,
        prefix=prefix,
        length=length,
    )
    assert actual == expect


@mark.parametrize("value, color, length, expect", fraction_part_test_cases)
def test_render_right_fraction(
    value: float,
    color: bool,
    length: Optional[int],
    expect: str,
) -> None:
    row = Row("foo", current=value - 1.0, maximum=value)
    assert row.render_right_fraction(color=color, length=length) == expect
