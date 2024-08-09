
# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Booking, Hall

def front(request):
    return render(request, 'hotel_app/front.html')

def halls(request):
    return render(request, 'hotel_app/Halls.html')

def booking_success(request):
    return render(request, 'hotel_app/booking_success.html')

def submit_booking(request):
    if request.method == 'POST':
        hall_id = request.POST.get('hall_id')
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        date = request.POST.get('date')
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')
        people = request.POST.get('people')
        activity = request.POST.get('activity')

        # Validate hall ID
        try:
            hall = Hall.objects.get(id=hall_id)
        except Hall.DoesNotExist:
            return render(request, 'hotel_app/error.html', {'message': 'Invalid hall ID'})

        # Create and save the booking
        booking = Booking(
            hall=hall,
            first_name=first_name,
            surname=surname,
            email=email,
            contact=contact,
            address=address,
            date=date,
            time_start=time_start,
            time_end=time_end,
            people=people,
            activity=activity
        )
        booking.save()

        return redirect('booking_success')  # Redirect to a success page or the front page

    return render(request, 'hotel_app/error.html', {'message': 'Invalid request method'})


from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': request.csrf_token})