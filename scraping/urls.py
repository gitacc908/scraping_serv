from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

urlpatterns = [
	path('', views.home, name='home'),
	path('list/', views.list, name='list_of_vacancies'),
	path('register/', views.SignUpView.as_view(), name='register'),
	path('login/', LoginView.as_view(template_name='scraping/users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
	]