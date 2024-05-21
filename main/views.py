from django.views.generic import TemplateView
from articles.models import Article


class MainPageView(TemplateView):
    template_name = 'index.html'

