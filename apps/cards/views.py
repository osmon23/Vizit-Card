from django.views import View
from django.shortcuts import render

from .models import Title, Contact, BankRequisites


class VizitCardView(View):
    def get(self, request):
        titles = Title.objects.all()
        contacts = Contact.objects.all()
        requisites = BankRequisites.objects.all()
        return render(request, 'cards/index.html', {'titles': titles, 'contacts': contacts, 'requisites': requisites})
