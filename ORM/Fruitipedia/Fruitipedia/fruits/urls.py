from django.urls import path, include

from Fruitipedia.fruits import views

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-fruit/', views.create_view, name='create_fruit'),
    path('create-category/', views.create_category_view, name='create_category'),
    path('<int:pk>/', include([path('details-fruit/', views.details_view, name='details_fruit'),
                               path('edit-fruit/', views.edit_view, name='edit_fruit'),
                               path('delete-fruit/', views.delete_view, name='delete_fruit'),
                               ]))
)
