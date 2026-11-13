import pytest
from cart import cart_total


def test_cart_total_simple():
    assert cart_total([100, 50]) == 150


def test_cart_total_empty():
    assert cart_total([]) == 0


def test_cart_total_with_discount():
    assert cart_total([100, 100], discount=10) == 180


def test_cart_total_negative_price():
    with pytest.raises(ValueError):
        cart_total([-5])


def test_cart_total_discount_boundaries():
    # Межі 0 і 100 є допустимими, 100% знижка дає нульову суму
    assert cart_total([80], discount=0) == 80
    assert cart_total([80], discount=100) == 0


def test_cart_total_discount_out_of_range():
    with pytest.raises(ValueError):
        cart_total([80], discount=101)
    with pytest.raises(ValueError):
        cart_total([80], discount=-1)


def test_cart_total_non_numeric_price():
    with pytest.raises(ValueError):
        cart_total(["100"])


def test_cart_total_rounds_to_kopecks():
    # 33.333... після знижки округлюється до двох знаків
    assert cart_total([33.33], discount=0) == 33.33
    assert cart_total([10, 10, 10], discount=33.33) == 20.0
