from django.contrib import admin
from .models import Category, Brand, Product, Subcategory, Review
# Category
admin.site.register(Category)
# SubCategory
admin.site.register(Subcategory)
#brand
admin.site.register(Brand)
#Review
admin.site.register(Review)
#Product
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','brand','category','sub_category','selling_price','discounted_price']
