
from django.urls import path
from .views import (
    home_view,
    register_view,
    login_view,
    logout_view,
)
urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', register_view, name='signup'),
    path('signin/', login_view, name='signin'),
    path('logout/', logout_view, name='logout'),
]
