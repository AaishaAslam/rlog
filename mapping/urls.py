from django.urls import path
from . import views

urlpatterns = [
        path('mapping', views.mapping, name = 'mapping')
    # path('', views.MappingView.as_view(), name = 'mapping')

]