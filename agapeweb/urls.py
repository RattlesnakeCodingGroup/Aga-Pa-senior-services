from django.urls import path

from . import views

app_name = 'agapeweb'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('about/', views.AboutView.as_view(), name='about'),
    # # path('products/', views.ProductView.as_view(), name='products'),
    # path('store/', views.StoreView.as_view(), name='store'),
    # path('products/', views.FishView.as_view(), name ='products')

]