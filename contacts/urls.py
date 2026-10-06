from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.contact_list, name="contact_list"),
    path("contacts/add/", views.contact_add, name="contact_add"),
    path(
    "contacts/<int:pk>/delete/",
    views.contact_delete,
    name="contact_delete",
    ),
    path("contacts/search/", views.contact_search, name="contact_search"),
    path("contacts/<int:pk>/edit/", views.contact_edit, name="contact_edit"),
    path("contacts/<int:pk>/row/", views.contact_row, name="contact_row"),
    path("contacts/<int:pk>/update/", views.contact_update, name="contact_update"),
]