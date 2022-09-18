from django.urls import path
from receipts import views

urlpatterns = [
    path('', views.receipts, name='receipts'),
    path('receipts_in/', views.receipts_in, name='receipts_in'),
    path('statistic/', views.statistic, name='statistic'),
    path('all/', views.all_receipts, name='all'),
    path('test/', views.ProductCreateView.as_view(), name='test'),
    path('test2/', views.ProductUpdateView.as_view(), name='test2'),

]