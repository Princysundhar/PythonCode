
from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('clsbaseviewhome/',views.tasklistview.as_view(),name='clsbaseviewhome'),
    path('clsbaseviewdetails/<int:pk>/',views.taskdetailview.as_view(),name='clsbaseviewdetails'),
    path('clsbasedupdate/<int:pk>/',views.taskupdateview.as_view(),name='clsbasedupdate'),
    path('clsbasedelete/<int:pk>/',views.taskdeleteview.as_view(),name='clsbasedelete'),
]