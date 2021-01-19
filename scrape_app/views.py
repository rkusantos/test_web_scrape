from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.utils import timezone
from django.conf import settings

from .models import *
from .forms import *
from .functions import *



class SearchProductListView(ListView):


    template_name = 'scrape_app/search_product.html'
    success_message = ''
    error_message = ''
    data = Product.objects.all().order_by('-adddate')

    def get(self, request, *args, **kwargs):

        form = SearchProductForm()

        return render(request, self.template_name, {'form': form, 'data':self.data})


    def post(self, request, *args, **kwargs):

        form = SearchProductForm(request.POST or None)
        

        if form.is_valid():
            
            self.product = form.cleaned_data['product']
            try:
                amazon = amazon_scrape_web(product=self.product)
                noon = noon_scrape_web(product=self.product)

                a = Product(product_name=amazon[0], product_source='Amazon', 
                            product_price=amazon[3], product_image_link=amazon[1], product_link=amazon[2])
                n = Product(product_name=noon[0], product_source='Noon', 
                            product_price=noon[3], product_image_link=noon[1], product_link=noon[2])
                a.save()
                n.save()
            
            except Exception as e:
                print(e)

                return render(request, self.template_name, {'form': form, 'data':self.data, 'error_message':'Search Error!'})

            return render(request, self.template_name, {'form': form, 'data':self.data, 'amazon':amazon, 'noon':noon})     

        else:
            return render(request, self.template_name, {'form': form, 'data':self.data})     

             