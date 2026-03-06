from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'Contacts.html')

def discounts(request):
    return render(request, 'Discounts.html')

def news(request):
    return render(request, 'News.html')

def online_registration(request):
    return render(request, 'Online-registration.html')

def ours_works(request):
    return render(request, 'Ours-works.html')

def personal_account(request):
    return render(request, 'Personal-account.html')

def prices(request):
    return render(request, 'prices.html')

def repair(request):
    return render(request, 'prices.html')

def reviews(request):
    return render(request, 'Reviews.html')

def shopping_cart(request):
    return render(request, 'Shopping-cart.html')