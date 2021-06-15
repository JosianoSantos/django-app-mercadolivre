from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.AuthView.as_view(), name='auth'),
    path('home', views.HomeView.as_view(), name='home'),
    path('best-sellers', views.BestSellersView.as_view(), name='best_sellers'),
    path('most-expensives', views.MostExpensivesItemsView.as_view(), name='most_expensive_items'),
    path('logout', views.LogoutView.as_view(), name='logout'),

]
