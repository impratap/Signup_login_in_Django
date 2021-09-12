from django.views.generic import TemplateView

# Create your views here.
class HomeageView(TemplateView):
    template_name='home.html'
