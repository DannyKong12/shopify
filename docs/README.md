# Shopify Backend Challenge 2019

This is my implementation of the Shopify challenge for 2019, visit [getting started](quickstart.md) to see the docs

## Backend and API
My implementation of the challenge is a simple backend with a GraphQL endpoint. Actionable instructions and queries are handled through GraphQL queries. To test the backend, you can use the GraphIQL view to build queries.

The idea is to create a single point of interface to supply queries, so that a front end app can access information easily. Database Tables are storied using a sqlite3 store, that can be queried using GraphQL.

Full Databse documentation regarding schema and types can be found in the GraphIQL view, specific examples can be found [here](queries.md)

## Technologies
This Project was built using Django 2 and graphene on python3.
