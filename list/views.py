from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from .models import ListModel 
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

class ListTop(TemplateView):
    # top.htmlをレンダリング
    template_name = 'list/top.html'

class ListIndex(ListView):
    # index.htmlをレンダリング
    template_name = 'list/index.html'
    model = ListModel

class ListNew(CreateView):
    # new.htmlをレンダリング
    template_name = 'list/new.html'
    model = ListModel
    fields = ['item']
    success_url = reverse_lazy('list:index')

class ListEdit(UpdateView):
    # edit.htmlをレンダリング
    template_name = 'list/edit.html'
    model = ListModel
    fields = ['item']
    success_url = reverse_lazy('list:index')

@require_POST
def deletefunc(request, pk):
    item = get_object_or_404(ListModel, id=pk)
    item.delete()
    return redirect('list:index')