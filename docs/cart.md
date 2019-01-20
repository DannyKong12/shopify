# Shopping Cart

We use mutations to modify the `cart`. The cart is a per-user and persistent (not session based). Carts are linked to users by a `userId` field. Authentication should be handled by signed tokens which provides access to the `userId`.

## Creating a cart
Since `cart`s are user-linked, we should create a cart for each user. This is done through a `mutation`. When a user is signed up, we create a `cart` using the mutation

```
mutation {
  createCart(userId: "test") {
    cart
    success
  }
}
```

The mutation has two fields `cart` which returns the cart that was just created, as well as `success` which is `True` if the cart was created successfully. Creating a cart with a `userId` that already exists will fail.

## Viewing Items in the Cart
Accessing the cart is done through the query field `cart`. Since the cart is per-user, we also specify the `userId` in an argument. Given a `userId` "test", we can access its cart.

```
query {
  cart(userId: "test") {
    items {
      title
      quantity
    }
    price
  }
}
```

The `items` in a cart are not the same as `products` from the previous section. You can treat them as a `product` with the additional field `quantity`, but `products` are items that "belong" to a company, and `cart_items` belong to the cart. The query returns

```
{
  "data": {
    "cart": {
      "items": [
        {
          "title": "Watches",
          "quantity": 3
        },
        {
          "title": "brown shoes",
          "quantity": 1
        }
      ],
      "price": 14500
    }
  }
}
```

The `price` field of the `cart` is the price of all the items.

## Adding Items

Adding an item is done through a `mutation`, `addToCart`, which takes the fields `productId` and `userId`.

```
mutation {
  addToCart(productId: 4, userId: "test") {
    success
  }
}
```

To see the updated cart, query

```
query {
  cart(userId: "test") {
    items {
      title
      price
    }
    price
  }
}
```

```
{
  "data": {
    "cart": {
      "items": [
        {
          "title": "Watches",
          "price": 3000
        },
        {
          "title": "brown shoes",
          "price": 5500
        },
        {
          "title": "running shoes",
          "price": 6000
        }
      ],
      "price": 20500
    }
  }
}
```

Product with id: 4 (running shoes) has been added to the cart, and the price has been updated as well. The total `price` of the cart is generated automatically during the query, not stored. This means that if a `product` changes in `price`, we don't need additional action to update the `price` of the `items` in the `cart`. We can also add *cart modifiers* (e.g. sales, discounts, coupons) without needing to modify prices of `products` globally.
