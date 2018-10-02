from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import ClientForm


@login_required
def client_list(request):
    data = {
        'clients': Client.objects.all()
    }
    return render(request, 'client/list.html', data)


@login_required
def client_new(request):
    form = ClientForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    data = {
        'form': form
    }
    return render(request, 'client/form.html', data)


@login_required
def client_update(request, id):
    client = get_object_or_404(Client, pk=id)
    form = ClientForm(request.POST or None, request.FILES or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('client_list')
    data = {
        'form': form
    }
    return render(request, 'client/form.html', data)


@login_required
def client_delete(request, id):
    client = get_object_or_404(Client, pk=id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'client/delete.html', {'client': client})

