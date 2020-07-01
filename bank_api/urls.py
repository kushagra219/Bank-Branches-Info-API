from django.urls import path, include
from . import views

app_name = 'bank_api'

urlpatterns = [
    path('ifsc/', views.IFSCBranchDetailView.as_view(), name='ifsc-branch-detail'),
    path('branches/', views.BankCityBranchesListView.as_view(), name='bank-city-branches-list'),
]