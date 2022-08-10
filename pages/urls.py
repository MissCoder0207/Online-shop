from django.urls import path

from pages.views import HomeView, AboutView
from post.views import ContactView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
]