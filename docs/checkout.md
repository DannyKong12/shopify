# Checking Out

Checking out is done in a two step process. First the products are added to the `cart`, which is described in the [previous section](cart.md). Then, when the user is ready to make a purchase, we expose the `CheckoutCart` endpoint. At this point, the frontend should also verify information such as billing and shipping address.

## CheckoutCart

Once a user is done shopping, they can proceed to checkout for the items in their `cart`. This can be done using the `CheckoutCart` endpoint on the API.

Checking out is done through a mutation, with the following query

```
mutation {
  CheckoutCart(userId: "test") {
    success
  }
}
```

The `success` field is an `enum`, and is set to `True` when the checkout process is complete, and changes in the database are made accordingly. Once checkout is completed, the `items` in the `cart` are *emptied* and the inventory of the `products` purchased are also removed with respect to the quantity purchased.

Users cannot proceed to checkout with no items in the cart, or if the quantity added to the cart exceeds the inventory in stock. When the item is added, the inventory is checked, and again at checkout. All of these will produce `success=False`.

## Exception Safety

The `CheckoutCart` endpoint makes key database changes, so we need to ensure that the function works properly. `CheckoutCart` can only be run if there are `items` in the `cart`, and if the `items` have enough inventory. Otherwise, the function fails without exception, setting `success=False` and **does not make changes to the database**. The `success` field allows for failure transparency, and the frontend should reflect errors accordingly.
