from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.item_list, name='item_list'),  # GET: List all items
    path('items/create/', views.create_item, name='create_item'),  # POST: Create a new item
]
