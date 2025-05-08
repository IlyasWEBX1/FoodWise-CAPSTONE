from django.shortcuts import render

# Create your views here.
def landing_page(request):
    funfacts = [
        "1.3 miliar ton makanan terbuang setiap tahunnya",
        "Makanan yang terbuang bisa memberi makan 2 miliar orang",
        "Food waste menyumbang 8% emisi gas rumah kaca global",
        "Indonesia membuang 13 juta ton makanan per tahun",
        "1/3 makanan yang diproduksi dunia terbuang percuma"
    ]

    return render(request, 'landing_page/landing_page.html', {'funfacts': funfacts})
