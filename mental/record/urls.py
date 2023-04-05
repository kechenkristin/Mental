from django.urls import path

from . import views

urlpatterns = [
    path('record_add', views.add_record, name='record_add'),
    path('record_list', views.record_list, name='record_list'),
    path('<int:eid>/remove', views.record_remove, name='record_remove'),
    path('<int:rid>/mood', views.analysis, name="mood_analysis"),
]
