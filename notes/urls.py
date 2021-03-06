from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexNote, name='indexNote'),
    path('delete/<int:pk>', views.deleteNoteView, name='delete'),
    path('update/<int:pk>', views.updateNoteViews, name='update'),
    path('tags/', views.indexTag, name='tags'),
    path('detailtag/<int:pk>', views.detailTag, name='detailTag')
]