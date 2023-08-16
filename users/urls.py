from . import views
from django.urls import path
from .views import HomePageView
from django.views.generic.base import TemplateView

urlpatterns = [
    # path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('', HomePageView.as_view(), name='home'),
    path('signup/', views.signup, name='signup'),
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]