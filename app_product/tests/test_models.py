import pytest

pytestmark = pytest.mark.django_db


class TestCategory:
    def test_str_method(self, category_factory):
        test_obj = category_factory(name="test_category")
        assert test_obj.__str__() == "test_category"


class TestBrand:
    def test_str_method(self, brand_factory):
        test_obj = brand_factory(name="test_brand")
        assert test_obj.__str__() == "test_brand"


class TestProduct:
    def test_str_method(self, product_factory):
        test_obj = product_factory(name="test_product")
        assert test_obj.__str__() == "test_product"
