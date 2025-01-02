from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Booking, Bike, Customer, Feedback
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect



#------- authentication part -----
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test #this identifies if the user is admin or not
from django.utils.decorators import method_decorator #idk but i think this is the same as the previous two that requires users to log in first 

# Existing views
class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'

class ListPageView(ListView):
    model = Bike
    template_name = 'app/list.html' 
    context_object_name = 'bikes' 

class BikeDetailView(DetailView):
    model = Bike
    template_name = 'app/bike_detail.html'
    context_object_name = 'bike'  

def is_admin(user):
    return user.is_staff

@method_decorator(user_passes_test(is_admin), name='dispatch')
class DashboardPageView(TemplateView):
    template_name = 'app/dashboard.html'
    model = Booking
    context_object_name = 'bookings' 



class BookingCreateView(CreateView):
    model = Booking
    fields = ['customer_name', 'phone_number', 'bike', 'days_booked']  
    template_name = 'app/create_req.html'
    success_url = reverse_lazy('pending')  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bikes'] = Bike.objects.filter(availability=True) 
        return context

class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['customer_name', 'phone_number', 'bike', 'days_booked']
    template_name = 'app/update_req.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bikes'] = Bike.objects.filter(availability=True) 
        return context
    
    def get_success_url(self):
        redirect_to = self.request.GET.get('redirect', None)
        if redirect_to == 'approved':
            return reverse('approved')
        elif redirect_to == 'completed':
            return reverse('completed')
        return reverse('pending')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'app/delete_req.html' 

    def get_success_url(self):
        redirect_to = self.request.GET.get('redirect', None)
        if redirect_to == 'completed':
            return reverse('completed')
        return reverse('pending')


class ApproveBookingView(View):
    def post(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.status = 'approved'
        booking.save()
        return redirect('pending')  
    
class CheckBookingView(View):
    def post(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.status = 'completed'
        booking.save()
        return redirect('approved')
    

class PendingRequestsView(ListView):
    model = Booking
    template_name = 'app/pending_req.html'  
    context_object_name = 'requests' 

    def get_queryset(self):
        return Booking.objects.filter(status='pending')

class ApprovedRequestsView(ListView):
    model = Booking
    template_name = 'app/approved_req.html' 
    context_object_name = 'requests'

    def get_queryset(self):
        return Booking.objects.filter(status='approved')
    
class CompletedRequestsView(ListView):
    model = Booking
    template_name = 'app/completed_req.html' 
    context_object_name = 'requests'

    def get_queryset(self):
        return Booking.objects.filter(status='completed')


def approve_booking(request, pk):
    booking = Booking.objects.get(pk=pk)
    booking.status = 'approved'
    booking.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))





class SignInPageView(TemplateView):
    template_name = 'app/signIn.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_staff:  
                messages.success(request, "You have been logged in as ADMIN.")
                return redirect('crud')  
            else:
                messages.success(request, "You have been logged in.")
                return redirect('home') 
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return render(request, self.template_name)  
        
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')  
