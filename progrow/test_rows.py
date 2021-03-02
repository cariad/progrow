from typing import List

from pytest import mark

from progrow.layout import Layout
from progrow.row import Row
from progrow.rows import Rows
from progrow.style import Style


def test_append() -> None:
    rows = Rows([Row(name="foo", current=1, maximum=9)])
    rows.append(name="bar", current=2, maximum=9)
    style = Style(color=False, width=40)
    assert rows.render(style) == "foo ████\nbar ███████▉\n"


@mark.parametrize(
    "rows, style, expect",
    [
        (
            Rows(
                [
                    Row(name="red", current=1, maximum=9),
                ]
            ),
            Style(width=40, name_suffix=""),
            Layout(name_length=3),
        ),
        (
            Rows(
                [
                    Row(name="red", current=1, maximum=9),
                ]
            ),
            Style(width=40, name_suffix="x"),
            Layout(name_length=4),
        ),
        (
            Rows(
                [
                    Row(name="red", current=1, maximum=9),
                ]
            ),
            Style(width=40, name_suffix="", show_fraction=True),
            Layout(name_length=3, left_fraction_length=1, right_fraction_length=1),
        ),
        (
            Rows(
                [
                    Row(name="red", current=10, maximum=90),
                ]
            ),
            Style(width=40, name_suffix="", show_fraction=True),
            Layout(name_length=3, left_fraction_length=2, right_fraction_length=2),
        ),
        (
            Rows(
                [
                    Row(name="red", current=1000, maximum=9000),
                ]
            ),
            Style(width=40, name_suffix="", show_fraction=True),
            Layout(name_length=3, left_fraction_length=5, right_fraction_length=5),
        ),
        (
            Rows(
                [
                    Row(name="red", current=1, maximum=9),
                ]
            ),
            Style(width=40, name_suffix="", show_percent=True),
            Layout(name_length=3, percent_length=4),
        ),
    ],
)
def test_calculate_layout(rows: Rows, style: Style, expect: Layout) -> None:
    layout = rows.calculate_layout(style)
    assert layout.left_fraction_length == expect.left_fraction_length
    assert layout.right_fraction_length == expect.right_fraction_length
    assert layout.name_length == expect.name_length
    assert layout.percent_length == expect.percent_length


@mark.parametrize(
    "rows, style, expect",
    [
        (
            Rows(
                [
                    Row(name="red", maximum=9, current=1),
                    Row(name="yellow", maximum=9, current=2),
                    Row(name="green", maximum=9, current=3),
                ]
            ),
            Style(color=False, width=40),
            [
                "red    ███▋",
                "yellow ███████▍",
                "green  ██████████▉",
            ],
        ),
        (
            Rows(
                [
                    Row(name="brown", maximum=9, current=4),
                    Row(name="scarlet", maximum=19, current=15),
                    Row(name="black", maximum=119, current=116),
                ]
            ),
            Style(color=False, show_fraction=True, width=40),
            [
                "brown   █████████▊               4 /   9",
                "scarlet █████████████████▍      15 /  19",
                "black   █████████████████████▌ 116 / 119",
            ],
        ),
        (
            Rows(
                [
                    Row(name="ochre", maximum=9, current=7),
                    Row(name="peach", maximum=9, current=8),
                    Row(name="ruby", maximum=9, current=9),
                ]
            ),
            Style(color=False, show_percent=True, width=40),
            [
                "ochre ██████████████████████▌        77%",
                "peach █████████████████████████▊     88%",
                "ruby  █████████████████████████████ 100%",
            ],
        ),
        (
            Rows(
                [
                    Row(name="olive", maximum=9, current=7),
                    Row(name="violet", maximum=9, current=8),
                    Row(name="fawn", maximum=9, current=9),
                ]
            ),
            Style(color=False, show_fraction=True, show_percent=True, width=40),
            [
                "olive  ███████████████▌     7 / 9 •  77%",
                "violet █████████████████▊   8 / 9 •  88%",
                "fawn   ███████████████████▉ 9 / 9 • 100%",
            ],
        ),
    ],
)
def test_to_string(rows: Rows, style: Style, expect: List[str]) -> None:
    assert rows.render(style) == "\n".join(expect) + "\n"
