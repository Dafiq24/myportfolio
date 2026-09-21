from django.urls import path

from main.views import (
    create_certification,
    create_experience,
    delete_certification,
    delete_experience,
    get_certifications_json,
    get_experiences_json,
    login_user,
    logout_user,
    register,
    show_certification_detail,
    show_certifications,
    show_experience,
    show_main,
    update_experience,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("experience/", show_experience, name="show_experience"),
    path("api/experiences/", get_experiences_json, name="get_experiences_json"),
    path("experience/add/", create_experience, name="create_experience"),
    path(
        "experience/<uuid:experience_id>/edit/",
        update_experience,
        name="update_experience",
    ),
    path(
        "experience/<uuid:experience_id>/delete/",
        delete_experience,
        name="delete_experience",
    ),
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
