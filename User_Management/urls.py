from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signup/done/', SignupDoneView.as_view(), name='signup-done'),
    path('<int:pk>/', PassengerInfoView.as_view(), name='update'),
]

app_name = 'User_Management'
