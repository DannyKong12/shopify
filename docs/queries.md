# Making Queries

Products on our backend can be queried through the standard GraphQL querying language. Products are categorized into the companies that sell them. Test it out by making a simple query.

```
query {
    allProducts {
      title
      price
    }
}
```

If you installed the example data, should see the following:

```
{
  "data": {
    "allProducts": [
      {
        "title": "Watches",
        "price": 3000
      },
      {
        "title": "white shoes",
        "price": 5000
      },
      {
        "title": "brown shoes",
        "price": 5500
      },
      {
        "title": "running shoes",
        "price": 6000
      }
    ]
  }
}
```
**NOTE** By default, the query will only return items with inventory. Supplying a flag `allProducts(all: True)` will also return items that are currently out of stock.

Notice the format of the data resembles the format of the query. We can add additional fields besides title and price, for example inventory, or product id. Also note here that `price` is an integer, representing CENTS

We also have queries for allCompanies. Go ahead and try some different combinations of queries and fields.

## Querying Specific Products

We can query for a single product or a single company by using the `product` or `company` field, along with an argument, `id` and `name` for company, or `title` for product. These arguments must match exactly.

```
query {
  product(id: 4) {
    title
  }
}
```

returns:

```
{
  "data": {
    "product": {
      "title": "running shoes"
    }
  }
}
```

The arguments are not required, no arguments will return `None`, as will conflicting arguments.

## Querying Products from a Company

The following query

```
query {
    allCompanies {
      products {
        item
        price
      }
    }
}
```

Is guaranteed to return products categorized by company.

```
{
  "data": {
    "allCompanies": [
      {
        "products": [
          {
            "title": "Watches",
            "price": 3000,
            "inventory": 5
          }
        ]
      },
      {
        "products": [
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
    ]
  }
}
```

We can apply filters defined previously to get more specific results.

```
query {
  company(id: 2) {
    products(title: "running shoes") {
      price
      inventory
    }
  }
}
```

```
{
  "data": {
    "company": {
      "products": [
        {
          "price": 6000,
          "inventory": 30
        }
      ]
    }
  }
}
```

This allows us to search for products from specific companies, as well as search for products from all companies.
