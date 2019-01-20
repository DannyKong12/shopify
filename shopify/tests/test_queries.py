import pytest

from ..schema import schema

pytestmark = pytest.mark.django_db

def test_correct_fetch_all_products():
    query = '''
    query {
      allProducts {
        title
        price
        inventory
      }
    }
    '''
    expected = {
      "allProducts": [
        {
          "title": "Watches",
          "price": 3000,
          "inventory": 5
        },
        {
          "title": "white shoes",
          "price": 5000,
          "inventory": 10
        },
        {
          "title": "brown shoes",
          "price": 5500,
          "inventory": 10
        },
        {
          "title": "running shoes",
          "price": 6000,
          "inventory": 30
        }
      ]
    }
    result = schema.execute(query)
    assert not result.errors
    assert result.data == expected

def test_correct_fetch_all_products_include_no_stock():
    query = '''
    query {
      allProducts(all: true) {
        title
        price
        inventory
      }
    }
    '''
    expected = {
      "allProducts": [
        {
          "title": "Watches",
          "price": 3000,
          "inventory": 5
        },
        {
          "title": "white shoes",
          "price": 5000,
          "inventory": 10
        },
        {
          "title": "brown shoes",
          "price": 5500,
          "inventory": 10
        },
        {
          "title": "running shoes",
          "price": 6000,
          "inventory": 30
        },
        {
        "title": "null product",
        "price": 0,
        "inventory": 0
        }
      ]
    }
    result = schema.execute(query)
    assert not result.errors
    assert result.data == expected

def test_correct_fetch_all_company_products():
    query = '''
    query {
      allCompanies {
        name
        products {
          title
        }
      }
    }
    '''
    expected = {
    "allCompanies": [
      {
        "name": "CompanyA",
        "products": [
          {
            "title": "Watches"
          }
        ]
      },
      {
        "name": "CompanyB",
        "products": [
          {
            "title": "white shoes"
          },
          {
            "title": "brown shoes"
          },
          {
            "title": "running shoes"
          },
          {
            "title": "null product"
          }
        ]
      }
    ]
    }
    result = schema.execute(query)
    assert not result.errors
    assert result.data == expected
