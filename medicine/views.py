from django.shortcuts import render
from django.views import View
from django.core.files.storage import FileSystemStorage
from medicine.service.home import HomeUtils
import logging


class Home(View):
    def get(self, request):
        if 'medicine_name' not in request.GET:
            return render(request, 'index.html')
        else:
            sku_name = request.GET['medicine_name']
            data = HomeUtils().search_data(medicine_name=sku_name)
            return render(request, 'index.html', data)


class Import(View):
    def post(self, request):
        try:
            myfile = request.FILES['csv_file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            homeUtils = HomeUtils()
            homeUtils.import_csv(filename=filename)
        except Exception as e:
            logging.exception(e)
        return render(request, 'index.html')
