from django.urls import path
from receipts import views

urlpatterns = [
    path('', views.receipts, name='receipts'),
    path('receipts_in/', views.receipts_in, name='receipts_in'),
    path('statistic/', views.statistic, name='statistic'),
    path('all/', views.Products_ALL.as_view(), name='product-form'),
    path('manual_in/', views.ProductCreateView.as_view(), name='manual_in'),
    path('test2/', views.ProductUpdateView.as_view(), name='test2'),

]