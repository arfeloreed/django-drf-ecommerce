import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import BrandFactory, CategoryFactory, ProductFactory

register(CategoryFactory)  # to access this, use category_factory
register(BrandFactory)  # brand_factory
register(ProductFactory)  # product_factory


@pytest.fixture
def api_client():
    return APIClient
