from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('view/<int:item_id>/',views.details,name="details"),
    path('delete/<int:item_id>/',views.delete_item,name="delete_item"),
    path('add/',views.create_item,name="create_item"),
    path('update/<int:item_id>',views.update_item,name="update_item")
]