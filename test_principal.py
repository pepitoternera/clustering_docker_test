import pytest
from principal import raiz


def test_raiz():
    assert raiz(25) == 5


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (1, 1),
        (4, 2),
        (9, 3),
        (0.25, 0.5),
        (raiz(16), 2),
        (6, raiz(6))
    ]
)
def test_raiz_mult(input_a, expected):
    assert raiz(input_a) == expected
