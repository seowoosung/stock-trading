from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('api/accounts', views.AccountsView.as_view(), name='accounts'),
    path('api/stock/data', views.StockDataView.as_view(), name='stock_data'),
]
