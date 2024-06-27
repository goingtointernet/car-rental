from django.shortcuts import render
from django.views import View
from products.models import Product, Review
from .forms import ReviewForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from products.models import CustomDiscount
from django.utils import timezone
#====Product-page================#
def all_collections(request):
    pass

#====Product-page================#
class ProductDetailsView(View):
    def get(self, request, permalink, category):
        try:
            product = Product.objects.get( permalink= permalink )
            product2 = get_object_or_404(Product, permalink= permalink)
            try:
                custom_discount = CustomDiscount.objects.get(
                    valid_cars=product2,
                    active=True,
                    valid_from__lte=timezone.now(),
                    valid_to__gte=timezone.now()
                )
            except CustomDiscount.DoesNotExist:
                custom_discount = None
            reviews = Review.objects.filter(product=product).order_by('-created_at')
            form = ReviewForm()            
            total_reviews = Review.objects.filter(product=product).count()
            product_reviews = Review.objects.filter(product=product).order_by('-created_at')
            average_rating = Review.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg'] or 0
            return render(request, 'product/product_page.html',{'product':product, "reviews":reviews, "form":form, 'total_reviews': total_reviews, 'custom_discount':custom_discount,
            'average_rating': round(average_rating, 1), "product_reviews":product_reviews})
        except Exception as e:
            print(e)
            return render(request, 'home/404.html')
    
    def post(self, request, category, permalink):
        product = get_object_or_404(Product, permalink=permalink)
        form = ReviewForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            new_rating = form.save(commit=False)
            new_rating.user = request.user
            new_rating.product = product
            new_rating.save()
            return redirect('product_page', category=category, permalink=permalink)
        else:
            return redirect('login_view')