from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:product_id>', views.detail, name='detail'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
]
