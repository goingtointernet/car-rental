from django.db import models
from account.models import User

# Category
class Category(models.Model):
    name = models.CharField(max_length=160, unique= True)
    category_img = models.ImageField(upload_to = 'category_img', null = True, blank = True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Category.objects.get(id=self.id)
            if this.category_img != self.category_img:
                this.category_img.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Category, self).save(*args, **kwargs)

# SubCategory
class Subcategory(models.Model):
    name = models.CharField(max_length=160, unique= True)
    
    def __str__(self):
        return self.name

# Brand
class Brand(models.Model):
    name = models.CharField(max_length=160, unique= True)
    
    def __str__(self):
        return self.name

class AvaibleTiming(models.Model):
    Time = models.CharField(max_length=160, unique= True, default="")
    def __str__(self):
        return self.Time
    
class PickupLocation(models.Model):
    location = models.CharField(max_length=160, unique= True, default="")
    def __str__(self):
        return self.location

class ProductImages(models.Model):
    image = models.ImageField(upload_to='product_img')

# Product
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=160)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    selling_price = models.FloatField()
    rent_per_day_price = models.FloatField()
    total_tax = models.FloatField(default=0)
    description = models.TextField()
    seats = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product_thumb = models.ImageField(upload_to='product_img')
    product_images = models.ManyToManyField(ProductImages, null = True)
    instructions = models.CharField(max_length=300, default="")
    features = models.CharField(max_length=500, default="")
    pro_tips = models.CharField(max_length=500)
    complete_location = models.CharField(max_length=300, default="")
    city = models.CharField(max_length=300, default="")
    country = models.CharField(max_length=300, default="")
    available_timing = models.ManyToManyField(AvaibleTiming, null = True)
    pickup_locations = models.ManyToManyField(PickupLocation, null = True)
    heighlights = models.TextField(default='''
    <strong>What is it? </strong>
    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Reiciendis vero voluptas ducimus inventore enim. Voluptas ipsam modi aliquid dicta voluptatem sit rem praesentium repellat corrupti, officia ducimus quos saepe molestias.</p>
    <br/>
    <strong>What makes it special? </strong>
    <ul>
        <li>Olive Oil Glossing Polish (6oz) enhances your hair for incredible shine and restores moisture to hair </li>
        <li>Helps to eliminate frizz and fly-always and resist humidity for longer lasting style </li>
        <li>Helps to leave hair healthy and more manageable </li>
    </ul>''')
    is_available = models.BooleanField(default=True)
    use_own_insurance = models.BooleanField(default=False)
    supplemental_liability_coverage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    damage_coverage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    permalink =models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Product.objects.get(id=self.id)
            if this.product_img != self.product_img:
                this.product_img.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Product, self).save(*args, **kwargs)




class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class CustomDiscount(models.Model):
    # your existing fields
    discount_price_percentage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_valid_days = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)