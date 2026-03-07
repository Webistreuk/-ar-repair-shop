"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index , name='Главная страница'),
    path('about/', views.about, name='О нас'),
    path('contacts/', views.contacts, name='Контакты'),
    path('discounts/', views.discounts, name='Скидки'),
    path('news/', views.news, name='Новости'),
    path('online-registration/', views.online_registration, name='Запись онлайн'),
    path('ours-works/', views.ours_works, name='Наши работы'),
    path('personal-account/', views.personal_account, name='Личный кабинет'),
    path('prices/', views.prices, name='Цены'),
    path('repair/', views.repair, name='Ремонт'),
    path('reviews/', views.reviews, name='Отзывы'),
    path('shopping-cart/', views.shopping_cart, name='Корзина'),
]
