import csv

from django.shortcuts import render
from django.conf import settings

def inflation_view(request):
    with open(settings.INFLATION_DATA_CSV, encoding='utf-8') as f:
        row_list = list(csv.reader(f))
    inflation_list = list()
    for item in row_list:
        item = item[0].split(';')
        inflation_list.append(item)
    tab_title = inflation_list.pop(0)
    return render(request, template_name='task1/inflation.html',
                  context={
                      'inflation_list': inflation_list,
                      'tab_title': tab_title,
                  })