from django.shortcuts import render
from .models import Product


# Create your views here.
def get_index_page(request):
    products = Product.objects.all()
    return render(
        request=request, template_name="shop/index.html", context={"products": products}
    )


def get_product_details(request, primary_key):
    product = Product.objects.get(id=primary_key)
    return render(
        request=request,
        template_name="shop/product_details.html",
        context={"product": product},
    )
