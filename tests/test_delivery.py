import pytest
from delivery import calculate_delivery

@pytest.mark.parametrize("subtotal, expected", [
    (0, 300),
    (999, 300),
    (1000, 150),
    (4999, 150),
    (5000, 0),
])
def test_regular_delivery(subtotal, expected):
    assert calculate_delivery(subtotal) == expected

@pytest.mark.parametrize("subtotal, expected", [
    (0, 550),
    (999, 550),
    (1000, 400),
    (4999, 400),
    (5000, 250),
])
def test_express_delivery(subtotal, expected):
    assert calculate_delivery(subtotal, express=True) == expected

def test_negative_subtotal():
    with pytest.raises(ValueError):
        calculate_delivery(-1)

def test_invalid_type_subtotal():
    with pytest.raises(TypeError):
        calculate_delivery("1000")

def test_invalid_type_express():
    with pytest.raises(TypeError):
        calculate_delivery(1000, express="yes")
