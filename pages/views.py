# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "home.html"

# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html')