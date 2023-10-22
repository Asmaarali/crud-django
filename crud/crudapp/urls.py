from django.urls import path
from crudapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.adduser,name='adduser'),
    path('delete/<int:item_id>/',views.delete,name="delete"),
    path('edit/<int:item_id>/',views.edit,name="edit")
]
