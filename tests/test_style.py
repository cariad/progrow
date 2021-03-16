from pytest import mark

from progrow.style import Style


def test_init__color_empty() -> None:
    assert Style().color


def test_init__color_set() -> None:
    assert not Style(color=False).color


def test_init__name_suffix_empty() -> None:
    assert Style().name_suffix == " "


def test_init__name_suffix_set() -> None:
    assert Style(name_suffix="x").name_suffix == "x"


def test_init__show_fraction_empty() -> None:
    assert not Style().show_fraction


def test_init__show_fraction_set() -> None:
    assert Style(show_fraction=True).show_fraction


def test_init__show_percent_empty() -> None:
    assert not Style().show_percent


def test_init__show_percent_set() -> None:
    assert Style(show_percent=True).show_percent


def test_fraction_prefix() -> None:
    assert Style().fraction_prefix == " "


def test_fraction_separator() -> None:
    assert Style().fraction_separator == " / "


@mark.parametrize("show_fraction, expect", [(False, " "), (True, " • ")])
def test_percent_prefix(show_fraction: bool, expect: str) -> None:
    assert Style(show_fraction=show_fraction).percent_prefix == expect


def test_width__forced() -> None:
    assert Style(width=7).width == 7


def test_width__auto() -> None:
    assert Style().width > 0
