import graphene
import graphql_jwt

import shopify.products.schema

class Query(shopify.products.schema.Query, graphene.ObjectType):
    pass

class Mutations(shopify.products.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
