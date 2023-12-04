import pytest
import figure


TEST_CASE1 = (
    (
        5,
        5
    ),
    (
        10,
        10
    )
)



@pytest.mark.parametrize('square_1, square_2', TEST_CASE1)
def test_get_figure(square_1: int, square_2: int) -> None:
    assert hash(figure.FigureFlyweight.get_figure('Square', square_1)) == hash(figure.FigureFlyweight.get_figure('Square', square_2))


TEST_CASE2 = (
    (
        7,
        9
    ),
    (
        15,
        16
    )
)



@pytest.mark.parametrize('circle_1, circle_2', TEST_CASE2)
def test_case_2(circle_1: int, circle_2: int) -> None:
    assert hash(figure.FigureFlyweight.get_figure('Circle', circle_1)) == hash(figure.FigureFlyweight.get_figure('Circle', circle_2))
