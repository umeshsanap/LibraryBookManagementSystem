from django.urls import path
from .import views

urlpatterns=[
    path("Librarian_registration/",views.Librarian_registration,name='Librarian-registration'),
    path("Librarian_login/",views.Librarian_login,name='Librarian-login'),
    path("add_book/",views.add_book,name='add-book'),
    path("update_book/<int:id>",views.update_book,name='update-book'),
    path('delete_book/<int:id>',views.delete_book,name='delete-book'),
    path('search_book/<str:title>',views.search_book,name='search-book'),
    path("search_book_by_filter/<str:title>",views.search_book_by_filter,name='search_book_by_filter')
]