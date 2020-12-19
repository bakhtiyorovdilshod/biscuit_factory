from decimal import Decimal

from apps.product.models import AddManufacturedProduct, ProductPriceList, ManufacturedProduct
from apps.recipe.models import ManufacturedProductRecipe


def change_status_product():
    produced_products = AddManufacturedProduct.objects.filter(for_price='un_calculate')
    for produced_product in produced_products:
        produced_product.for_price = 'calculated'
        produced_product.save()

def calculate_man_product_price():
    data = {'data':[

    ]}
    products = AddManufacturedProduct.objects.filter(for_price='un_calculate')
    for obj in products:
        total_price = 0
        product = obj.product
        quantity = obj.quantity
        recipes = ManufacturedProductRecipe.objects.filter(manufactured_product=product)
        for recipe in recipes:
            product = recipe.product
            value = recipe.value
            product_price = ProductPriceList.objects.filter(product=product).order_by('-id').first().price
            total_price = Decimal(total_price + product_price * value * quantity)/Decimal(quantity)
        data['data'].append({
            'product': product.id,
            'product_cost': total_price,
        })
    return data