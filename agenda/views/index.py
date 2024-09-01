from django.shortcuts import render
from agenda.models import Contact

# Create your views here.


def index(request):
    contacts = {
        'contacts': Contact.objects.filter(show=True)[:10]
    }
    return render(request, 'agenda/index.html', contacts)
