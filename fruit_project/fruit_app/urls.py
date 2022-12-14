
from django.urls import path
from . import views
app_name='fruit_app'
urlpatterns = [

    path('',views.index,name='index'),
    path('fruit/<int:fruit_id>/',views.detail,name='detail'),
    path('add/', views.add_fruit, name='add_fruit'),
    path('update/<int:id>/',views.update,name='update'),
    path('remove/<int:id>/',views.remove,name='remove'),
]
