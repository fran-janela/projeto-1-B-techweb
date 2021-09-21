from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>', views.deleteView, name='delete'),
    path('update/<int:pk>', views.updateViews, name='update'),
]