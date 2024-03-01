from django.shortcuts import render
from numpy import product
from .models import StaticPosts, Faqs
from django.core.mail import send_mail
from django.contrib import messages
from django.views import View
from products.models import Product
#==Home=======================#
class ProductView(View):
    def get(self,request):
        try:
            all = Product.objects.all().order_by('-pk')
            return render(request,'home/index.html', {'all':all})
        except:
            all = Product.objects.all()
            return render(request,'home/index.html', {'all':all})

class ProductAll(View):
    def get(self,request):
        all = Product.objects.all()
        viewall = True
        return render(request,'home/search.html', {'product':all, 'viewall':viewall})

#==Static-post============================#
def staticpost(request,slug):
    staticpost = StaticPosts.objects.filter(slug=slug).first()
    allpost = StaticPosts.objects.all()
    
    context = {'allpost': allpost,'staticpost':staticpost}
    return render(request, 'home/static-post.html', context)    


#==Contact-Page==========================#
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
            'name':name,
            'email':email,
            'message':message,
        }
        message = '''
        New Message:{}

        From:{}
        '''.format(data['message'],data['email'])
        send_mail(data['name'], message, '',['touseeqijazpro1@gmail.com'])
        messages.success(request, '*Sent Successfully')
    return render(request, 'home/contact.html')

#==Search============================#
def search(request):
    search=request.GET['search']
    if len(search)>78:
        product = []
    else:    
        product_title = Product.objects.filter(title__icontains=search)
        product_location = Product.objects.filter(complete_location__icontains=search)
        product_city = Product.objects.filter(city__icontains=search)
        product_category = Product.objects.filter(category__name__icontains=search)
        product_subcategory = Product.objects.filter(sub_category__name__icontains=search)
        product = product_title.union(product_category).union(product_subcategory).union(product_location).union(product_city)
    params={'product': product,'search':search}
    return render(request, 'home/search.html', params)

def custom_404(request, exception):
    return render(request, "home/404.html", {}, status=404)




#==Static-post============================#
def faqs(request):
    allfaqs = Faqs.objects.all().order_by("-pk")
    context = {'faqs': allfaqs}
    return render(request, 'home/faqs.html', context)   