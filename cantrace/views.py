from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView

from .functions import analyze, update_database, update_database2
from .models import *


def upload(request):
    print(request.method)
    if request.method == 'POST':
        try:
            my_file = request.FILES['myfile']
            # can1set, can2set = analyze(my_file)
            # context = {'can1set': can1set, 'can2set': can2set}
            update_database2(my_file)
            return redirect('cantrace:analysis')
        except:
            return render(request, 'cantrace/upload.html')

    return render(request, 'cantrace/upload.html')


def analysis(request):
    return render(request, 'cantrace/analysis.html')


class TraceListView(ListView):
    model = Trace
    template_name = 'cantrace/traceList.html'


class TraceDetailView(DetailView):
    model = Trace
    template_name = 'cantrace/traceDetail.html'


