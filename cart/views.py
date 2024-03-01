from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import redirect, render
from numpy import product
from cart.models import Cart, Booking
from products.models import CustomDiscount
from products.models import Product
from django.db.models import Q
from account.models import User
from account.forms import EditUserAddressForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
import stripe
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
import json
from datetime import date, timedelta, datetime
from django.shortcuts import get_object_or_404
stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    data = json.loads(request.body)
    total_amount = data['amount']
    booking_id = data['booking_id']
    total_amount = int(total_amount*100)
    base_url = request.build_absolute_uri('/')[:-1]  # Remove trailing slash
    success_url = f'{base_url}/cart/paymentdone/{booking_id}'
    cancel_url = f'{base_url}/cart/checkout/{booking_id}'
    print(total_amount)
    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Total Amount',
                    },
                    'unit_amount': total_amount, # in cents, meaning $20.00
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url,
            customer_email=request.user.email,
        )
        return JsonResponse({
            'id': session.id
        })
    return redirect('index')
#====show-cart================#
@login_required
def shop_cart(request):
        user = request.user
        cart = Cart.objects.filter(user=user).order_by('-pk')
        return render(request, 'product/cart.html', {'cart':cart})

#====checkout================#
@login_required
def checkout(request, cart_id):
        user = request.user
        booking_car_details= Cart.objects.get(id=cart_id)
        total_amount = booking_car_details.order_price
        amount =booking_car_details.order_price
        summary_shipping = 0.0
        summary_amount = booking_car_details.order_price
        return render(request, 'product/checkout.html',{'booking_car_details':booking_car_details, 'total_amount':total_amount, 'summary_amount':summary_amount, 'summary_shipping':summary_shipping })

#====order================#
@login_required
def payment_done(request, cart_id):
    try:
        cart = get_object_or_404(Cart, id=cart_id)
        # Update the order_status to 'active'
        booking = Booking(
                user=request.user,
                car=cart.car,
                pickup_date=cart.pickup_date,
                pickup_time=cart.pickup_time,
                dropoff_date=cart.dropoff_date,
                dropoff_time=cart.dropoff_time,
                pickup_point=cart.pickup_point,
                city=cart.city,
                seller_car_location=cart.seller_car_location,
                rent_days=cart.rent_days, 
                insurance_amount = cart.insurance_amount,
                total_amount=cart.total_amount, 
                user_name=cart.user_name,
                user_phone=cart.user_phone,
                user_address=cart.user_address,
                user_pay=cart.total_amount, 
            )
        booking.save()
        cart_booking = Cart.objects.filter(user=request.user)
        for c in cart_booking:
            c.delete()
        return redirect('order')
    except ValueError as e:
        return redirect('checkout',cart_id)
#====order================#
@login_required
def order(request):
    user = request.user
    order = Booking.objects.filter(user=user).order_by('-pk')
    return render(request, 'product/order.html', {'order':order})
    
def get_available_dates(car_id, pickup_date, dropoff_date):
    overlapping_bookings = Booking.objects.filter(
        car_id=car_id,
        pickup_date__lt=dropoff_date,
        dropoff_date__gt=pickup_date,
    ).values_list('pickup_date', 'dropoff_date')

    # Get the unavailable date range for the car
    unavailable_dates = []
    for booking_pickup, booking_dropoff in overlapping_bookings:
        overlap_start = max(pickup_date, booking_pickup)
        overlap_end = min(dropoff_date, booking_dropoff)
        
        # Check if there is a valid overlap
        if overlap_start < overlap_end:
            overlap_range = [overlap_start + timedelta(n) for n in range((overlap_end - overlap_start).days + 1)]
            unavailable_dates.extend(overlap_range)
    # Calculate available dates within the given range
    all_dates = [date.today() + timedelta(n) for n in range(90)]
    available_dates = [d for d in all_dates if d not in unavailable_dates]


    # Convert available dates to string for JavaScript usage
    available_dates_str = json.dumps(available_dates, cls=DjangoJSONEncoder)
    return available_dates_str

@login_required
def car_booking(request, car_id):
    try:
        all_bookings = Booking.objects.filter(car_id=car_id)
        print(all_bookings)
        car = Product.objects.get(id=car_id)
        # Assuming you want to consider the pickup and dropoff dates of the first booking
        if all_bookings:
            # Initialize pickup and dropoff dates with the first booking
            pickup_date = all_bookings.first().pickup_date
            dropoff_date = all_bookings.first().dropoff_date

            # Iterate through all bookings and adjust pickup and dropoff dates if needed
            for booking in all_bookings[1:]:
                if booking.pickup_date < pickup_date:
                    pickup_date = booking.pickup_date
                if booking.dropoff_date > dropoff_date:
                    dropoff_date = booking.dropoff_date
        else:
            # If there are no bookings, use default or today's date
            pickup_date = date.today()
            dropoff_date = date.today() + timedelta(days=1)

            # Calculate available dates
        available_dates = get_available_dates(car_id, pickup_date, dropoff_date)
        return render(request, 'product/dates.html', {'available_dates': available_dates, "car":car})
    except Exception as e:
        print(e)
        return render(request, 'home/404.html')
    
@login_required
def save_booking(request):
    try:
        if request.method == 'POST':
            pickup_dropoff_date = request.POST['pickup_dropoff']
            pickup_date = None
            dropoff_date = None
            pickup_time = request.POST['pickup_time']
            dropoff_time = request.POST['dropoff_time']
            pickup_location = request.POST['pickup_location']
            city = request.POST['city']
            phone = request.POST['phone']
            car_id = request.POST['car_id']
            name = request.POST['full_name']
            car_location = request.POST['car_address']
            user_address = request.POST['user_address']
            insurance_amount = request.POST['insurance_amount']
            print(insurance_amount, "ins")
            required_fields = [pickup_dropoff_date, name, pickup_time, dropoff_time, pickup_location, city, phone, car_id]
            custom_discounts = CustomDiscount.objects.all()
            if custom_discounts.exists():
                global_discount = custom_discounts[0]
            else:
                global_discount = 0
            
            if None in required_fields or '' in required_fields:
                return redirect('car_booking',car_id)
            if 'to' in pickup_dropoff_date:
                pickup_date_str, dropoff_date_str = map(lambda x: x.strip(), pickup_dropoff_date.split("to"))

                try:
                    pickup_date = datetime.strptime(pickup_date_str, '%Y-%m-%d').date()
                    dropoff_date = datetime.strptime(dropoff_date_str, '%Y-%m-%d').date()
                except ValueError as e:
                    print(f"Error: {e}")
                    # Handle the error, redirect or display a message to the user
                    return render(request, 'your_error_template.html', {'error_message': 'Invalid date format'})

            # Calculate the number of days
                rental_days = (dropoff_date - pickup_date).days
                rental_days = rental_days + 1
            else:
                pickup_date_str = pickup_dropoff_date.strip()
                try:
                    pickup_date = datetime.strptime(pickup_date_str, '%Y-%m-%d').date()
                except ValueError as e:
                    print(f"Error: {e}")
                    # Handle the error, redirect or display a message to the user
                    return render(request, 'your_error_template.html', {'error_message': 'Invalid date format'})

                dropoff_date = pickup_date
                rental_days = 1

            car_instance = Product.objects.get(id=car_id)

            cart = Cart(
                user=request.user,
                car=car_instance,
                pickup_date=pickup_date,
                pickup_time=pickup_time,
                dropoff_date=dropoff_date,
                dropoff_time=dropoff_time,
                pickup_point=pickup_location,
                city=city,
                seller_car_location=car_location,
                rent_days=rental_days, 
                total_amount=car_instance.selling_price*rental_days+car_instance.total_tax - int(global_discount.discount_price) + int(insurance_amount), 
                user_name=name,
                insurance_amount = insurance_amount,
                user_phone=phone,
                user_address=user_address,
                order_price=car_instance.selling_price*rental_days+car_instance.total_tax - int(global_discount.discount_price) + int(insurance_amount), 
            )
            cart.save()
            return redirect('checkout',cart.id)
    
        else:
            return redirect('car_booking',car_id)
    except ValueError as e:
        return redirect('car_booking',car_id)