from django.shortcuts import render, redirect
from .forms import LoansForm

# Create your views here.


def loans(request):
    context = {}
    return render(request, 'loans/loans.html', context)


def create_loans(request):
    form = LoansForm()

    if request.method == 'POST':
        form = LoansForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
        else:
            print(form.errors)
            return render(request, 'forms.html', {'form': form})

    context = { 'form': form }
    return render(request, 'forms.html', context)
