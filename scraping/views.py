from django.shortcuts import render
from .models import Vacancy
from .forms import FindForm, UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# Create your views here.
def home(request):
	form = FindForm()
	city = request.GET.get('city')
	language = request.GET.get('language')
	context = {'city': city, 'language': language, 'form': form}
	if city or language:
		_filter = {}
		if city:
			_filter['city__slug'] = city
		if language:
			_filter['Language__slug'] = language

		qs = Vacancy.objects.filter(**_filter)
		paginator = Paginator(qs, 2)

		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context['object_list'] = page_obj

	return render(request, 'scraping/home.html', context)



def list(request):
	lst = Vacancy.objects.all().order_by('-timestamp')
	return render(request, 'scraping/list.html', {'lst': lst})




class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'scraping/users/user_register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"

