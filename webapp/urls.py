from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    DashboardPageView,
    ListPageView,
    SignInPageView,
    PendingRequestsView,
    ApprovedRequestsView,
    CompletedRequestsView, 
    BookingCreateView,
    BookingUpdateView,
    BookingDeleteView,
    ApproveBookingView,
    CheckBookingView,
    BikeDetailView,
    user_logout,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('crud/', DashboardPageView.as_view(), name='crud'),  # Only admins can access this
    path('list/', ListPageView.as_view(), name='list'),
    path('signIn/', SignInPageView.as_view(), name='signIn'),

    path('pending/', PendingRequestsView.as_view(), name='pending'),
    path('approved/', ApprovedRequestsView.as_view(), name='approved'),
    path('completed/', CompletedRequestsView.as_view(), name='completed'),

    path('bike/<int:pk>/', BikeDetailView.as_view(), name='bike_detail'),
    path('create-request/', BookingCreateView.as_view(), name='create_req'), 
    path('update-request/<int:pk>/', BookingUpdateView.as_view(), name='update_req'),
    path('delete-request/<int:pk>/', BookingDeleteView.as_view(), name='delete_req'),
    path('approve-request/<int:pk>/', ApproveBookingView.as_view(), name='approve_req'),
    path('check-request/<int:pk>/', CheckBookingView.as_view(), name='check_req'),
    path('logout/', user_logout, name='Logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
