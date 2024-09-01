from agenda.models import Contact

c = Contact()
c = Contact.objects.get(pk=1)
c.first_name
