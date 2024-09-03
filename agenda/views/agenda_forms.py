from django.shortcuts import render
from agenda.forms import ContactForm


def create(request):

    if request.method == 'POST':

        context = {
            'form': ContactForm(request.POST)
        }
        return render(request, 'agenda/create.html', context)

    context = {
            'form': ContactForm()
        }
    return render(request, 'agenda/create.html', context)
