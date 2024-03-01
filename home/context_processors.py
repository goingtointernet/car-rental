from django.conf import settings
from .models import StaticPosts, SiteData
from products.models import CustomDiscount
from cart.models import Cart

#Static-Page-Post
def staticposts(request):
    staticposts = StaticPosts.objects.all()
    return {"staticposts": staticposts}

#Footer Data
def sitedata(request):
    sitedata = SiteData.objects.all()[0]
    custom_discounts = CustomDiscount.objects.all()
    if custom_discounts.exists():
        global_discount = custom_discounts[0]
    else:
        global_discount = 0

    total_cart_item = 0
    if request.user.is_authenticated:
        total_cart_item = len(Cart.objects.filter(user=request.user))
    return {"sitedata": sitedata,'total_cart_item':total_cart_item, "globalDiscount":global_discount}