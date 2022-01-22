from django.http import request
from django.shortcuts import render
import requests

def index(request):
    if request.method == "POST":
        girilen = request.POST.get("firstCurrency")
        karsilik = request.POST.get("secondCurrency")
        miktar = request.POST.get("amount")

        url = "http://data.fixer.io/api/latest?access_key=key"
        response = requests.get(url)
        veri = response.json()

        girilen_deger = veri["rates"][girilen]
        karsilik_deger = veri["rates"][karsilik]
            
        sonuc = karsilik_deger/girilen_deger * float(miktar)
        context = {
            "miktar":miktar,
            "girilen":girilen,
            "sonuc":sonuc,
            "karsilik":karsilik
        }
        return render(request,"index.html",context)

    else:
        return render(request,"index.html")
