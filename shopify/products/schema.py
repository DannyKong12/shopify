import graphene
from graphene import Node

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from shopify.products.models import Company, Product, Cart, CartItem

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class CompanyType(DjangoObjectType):
    products = graphene.List(ProductType, title=graphene.String())

    def resolve_products(self, info, title=""):
        if title is not "":
            return Product.objects.filter(company=self.id).filter(title=title)

        return Product.objects.filter(company=self.id)

    class Meta:
        model = Company

class CartItemType(DjangoObjectType):
    price = graphene.Int()
    title = graphene.String()

    def resolve_title(self, info):
        return self.product.title

    def resolve_price(self, info):
        return self.product.price

    class Meta:
        model = CartItem

class CartType(DjangoObjectType):
    price = graphene.Int()
    userId = graphene.String()

    def resolve_price(self, info):
        return sum([x.product.price*x.quantity for x in self.items.all()])

    class Meta:
        model = Cart

class Query(object):
    all_companies = graphene.List(CompanyType)
    all_products = graphene.List(ProductType, all=graphene.Boolean())
    product = graphene.Field(ProductType, id=graphene.Int(), title=graphene.String())
    company = graphene.Field(CompanyType, id=graphene.Int(), name=graphene.String())
    cart = graphene.Field(CartType, userId=graphene.String())

    def resolve_all_companies(self, info, **kwargs):
        return Company.objects.all()

    def resolve_all_products(self, info, **kwargs):
        get_all = kwargs.get('all')
        if get_all is None or all is False:
            return Product.objects.select_related('company').filter(inventory__gt=0)

        return Product.objects.select_related('company').all()

    def resolve_product(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Product.objects.get(pk=id)
        if title is not None:
            return Product.objects.get(title=title)

        return None

    def resolve_company(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Company.objects.get(pk=id)
        if name is not None:
            return Company.objects.get(name=name)

        return None

    def resolve_cart(self, info, **kwargs):
        id = kwargs.get('userId')

        return Cart.objects.get(userId=id)

class CreateCart(graphene.Mutation):
    class Arguments:
        userId = graphene.String()

    items = []
    success = graphene.Boolean()
    cart = graphene.Field(lambda: CartType)

    def mutate(self, info, userId):
        pk = Cart.objects.all().count() + 1
        cart = Cart(userId=userId, pk=pk)
        cart.save()
        success = True
        return CreateCart(cart=cart, success=success)

class AddToCart(graphene.Mutation):
    class Arguments:
        userId = graphene.String()
        productId = graphene.Int()
        quantity = graphene.Int(default_value=1)

    success = graphene.Boolean()

    def mutate(self, info, userId, productId, quantity):
        product = Product.objects.get(id=productId)
        if (quantity > product.inventory):
            success = False
            return None

        cartitem = CartItem(product=product, quantity=quantity)
        cartitem.save()
        cart = Cart.objects.get(userId=userId)
        cart.items.add(cartitem)
        success = True
        return AddToCart(success=success)

class Mutation(object):
    create_cart = CreateCart.Field()
    add_to_cart = AddToCart.Field()
