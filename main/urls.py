from django.urls import path

from main.views import (
    create_certification,
    delete_certification,
    get_certifications_json,
    show_certification_detail,
    show_certifications,
    show_experience,
    show_main,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path(
        "api/certifications/",
        get_certifications_json,
        name="get_certifications_json",
    ),
    path("certifications/", show_certifications, name="show_certifications"),
    path(
        "certifications/add/",
        create_certification,
        name="create_certification",
    ),
    path(
        "certifications/<uuid:certification_id>/delete/",
        delete_certification,
        name="delete_certification",
    ),
    path(
        "certifications/<uuid:certification_id>/",
        show_certification_detail,
        name="show_certification_detail",
    ),
]
