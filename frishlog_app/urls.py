from django.urls import path
from django.http import HttpResponse   # add this if home_view is here
from .views import login_view, registration_view

def home_view(request):
    return HttpResponse("✅ You are logged in!")   # simple test response

urlpatterns = [
    path('loginn/', login_view, name='loginn'),
    path('register/', registration_view, name='register'),
    path('home/', home_view, name='home'),   # ✅ add this line
]
