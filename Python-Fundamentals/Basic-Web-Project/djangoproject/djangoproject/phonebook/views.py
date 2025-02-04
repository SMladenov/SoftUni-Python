from django.shortcuts import render, redirect
from djangoproject.phonebook.models import Contact

def landing_page(request):
    context = {
        #Equivalent to Select * from Contact
        'contacts': Contact.objects.all(),
    }
    return render(request, 'phonebook\index.html',context)

def create_contact(request):
    name = request.POST.get('name')
    number = request.POST.get('number')
    contact = Contact(
        name = name,
        number = number
    )

    contact.save()
    return redirect('landing-page')
