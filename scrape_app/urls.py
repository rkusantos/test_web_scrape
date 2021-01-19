from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'scrape_app'

urlpatterns = [
    path('search_product/', views.SearchProductListView.as_view(template_name="scrape_app/search_product.html"), name='search_product'),
]