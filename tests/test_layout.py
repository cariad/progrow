from typing import List, Optional

from pytest import mark

from progrow.layout import Layout


def test_init__left_fraction_length_empty() -> None:
    assert Layout().left_fraction_length is None


def test_init__left_fraction_length_set() -> None:
    assert Layout(left_fraction_length=3).left_fraction_length == 3


def test_init__name_length_empty() -> None:
    assert Layout().name_length is None


def test_init__name_length_set() -> None:
    assert Layout(name_length=3).name_length == 3


def test_init__percent_length_empty() -> None:
    assert Layout().percent_length is None


def test_init__percent_length_set() -> None:
    assert Layout(percent_length=3).percent_length == 3


def test_init__right_fraction_length_empty() -> None:
    assert Layout().right_fraction_length is None


def test_init__right_fraction_length_set() -> None:
    assert Layout(right_fraction_length=3).right_fraction_length == 3


consideration_test_cases = [
    ([], None),
    ([1], 1),
    ([1, 2], 2),
    ([2, 3, 1], 3),
]


@mark.parametrize("considerations, expect", consideration_test_cases)
def test_consider_left_fraction(
    considerations: List[int],
    expect: Optional[int],
) -> None:
    layout = Layout()
    for consideration in considerations:
        layout.consider_left_fraction(consideration)
    assert layout.left_fraction_length == expect


@mark.parametrize("considerations, expect", consideration_test_cases)
def test_consider_name(
    considerations: List[int],
    expect: Optional[int],
) -> None:
    layout = Layout()
    for consideration in considerations:
        layout.consider_name(consideration)
    assert layout.name_length == expect


@mark.parametrize("considerations, expect", consideration_test_cases)
def test_consider_percent(
    considerations: List[int],
    expect: Optional[int],
) -> None:
    layout = Layout()
    for consideration in considerations:
        layout.consider_percent(consideration)
    assert layout.percent_length == expect


@mark.parametrize("considerations, expect", consideration_test_cases)
def test_consider_right_fraction(
    considerations: List[int],
    expect: Optional[int],
) -> None:
    layout = Layout()
    for consideration in considerations:
        layout.consider_right_fraction(consideration)
    assert layout.right_fraction_length == expect
