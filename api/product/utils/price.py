from apps.product.models import AddManufacturedProduct, ProductPriceList, ManufacturedProduct
from apps.recipe.models import ManufacturedProductRecipe


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
            total_price = total_price + product_price * value * quantity
        data['data'].append({
            'product': product.id,
            'total_price': total_price,
            'quantity': quantity
        })
        obj.for_price = 'calculated'
        obj.save()
    return data