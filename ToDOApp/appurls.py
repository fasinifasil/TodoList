from django.urls import path

from ToDOApp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('update/<str:k1>',views.update,name='update'),
    path('delete/<str:k1>',views.delete,name='delete')

]
