from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.utils import timezone
from django.conf import settings

from .models import *
from .forms import *




class SearchProductListView(ListView):


    template_name = 'scrape_app/search_product.html'
    success_message = ''
    error_message = ''

    def get(self, request, *args, **kwargs):

        form = SearchProductForm()

        data = Product.objects.all().order_by('-adddate')


        return render(request, self.template_name, {'form': form, 'data':data})

    # def post(self, request, *args, **kwargs):

    #     form = InputDataForm(request.POST or None, request.FILES)
        

    #     if form.is_valid():
    #         try:
                
    #             if 'teachers' in request.FILES:

    #                 df = pd.read_csv(request.FILES['teachers'])
    #                 df = df.dropna()

    #                 # checking for more than 5 subjects
    #                 # possible stopping point though model will not allow more than 5 subjects per teacher in insert
    #                 for subs in df['Subjects taught']:
    #                     if len(subs.split(",")) > 5:
    #                         self.error_message = 'ERROR: uploading more than 5 subjects'
    #                         return render(request, self.template_name, {'form': form, 'error_message':self.error_message})
                        
    #                 for index, row in df.iterrows():
    #                     teacher = Teacher(first_name=row['First Name'],
    #                                                                 last_name=row['Last Name'],
    #                                                                 profile_picture=row['Profile picture'],
    #                                                                 email_address=row['Email Address'],
    #                                                                 phone_number=row['Phone Number'],
    #                                                                 room_number=row['Room Number'],
    #                                                                 )
    #                     teacher.save()

    #                     for subject in row['Subjects taught'].split(","):
                        
    #                         subjects_insert = Subjects(subject=subject, teacher=teacher)
    #                         subjects_insert.save()

                    

    #                 # OPTIONAL BULK INSERT METHOD
    #                 # Teacher.objects.bulk_create([Teacher(first_name=row['First Name'],
    #                 #                                                 last_name=row['Last Name'],
    #                 #                                                 profile_picture=row['Profile picture'],
    #                 #                                                 email_address=row['Email Address'],
    #                 #                                                 phone_number=row['Phone Number'],
    #                 #                                                 room_number=row['Room Number'],
    #                 #                                                 ) for index, row in dataframe.iterrows()])

    #             if 'pictures' in request.FILES:

    #                 with ZipFile(request.FILES['pictures']) as myzip:
                        
    #                     myzip.extractall(settings.MEDIA_ROOT + '/images')

    #             if request.FILES == {}:
                    
    #                 return render(request, self.template_name, {'form': form})

    #             self.success_message = 'FILE UPLOAD SUCCESSFUL!'

    #             return render(request, self.template_name, {'form': form, 'success_message':self.success_message})

    #         except Exception as e:
    #                 self.error_message = e
    #                 return render(request, self.template_name, {'form': form, 'error_message':self.error_message})

    #     else:
    #         return render(request, self.template_name, {'form': form})                  