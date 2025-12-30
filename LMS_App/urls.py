from django.urls import path
from .import views

urlpatterns=[
    path("add_book/",views.add_book,name='add-book'),
    path("update_book/",views.update_book,name='update-book'),
    path('delete_book/<int:id>',views.delete_book,name='delete-book'),
    path('search_book/<str:title>',views.search_book,name='search-book')
]