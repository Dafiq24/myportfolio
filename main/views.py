from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import PermissionDenied
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from main.forms import CertificationForm, ExperienceForm
from main.models import Certification, Experience


def is_experience_editor(user):
    """Return whether an authenticated user belongs to the Editor group."""
    return (
        user.is_authenticated
        and user.groups.filter(name="Editor").exists()
    )


def can_update_experience(user):
    """Allow Experience updates to editors and the portfolio owner."""
    return user.is_authenticated and (
        user.is_superuser or is_experience_editor(user)
    )


def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("main:login")

    return render(
        request,
        "register.html",
        {"name": "Sultan Noor Dafiq", "form": form},
    )


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        response = redirect("main:show_main")
        response.set_cookie(
            "last_login",
            timezone.now().strftime("%Y-%m-%d %H:%M:%S UTC"),
            httponly=True,
            secure=request.is_secure(),
            samesite="Lax",
        )
        return response

    return render(
        request,
        "login.html",
        {"name": "Sultan Noor Dafiq", "form": form},
    )


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie("last_login", samesite="Lax")
    return response

def show_main(request):
    context = {
        "name": "Sultan Noor Dafiq",
        "npm": "2506600713",
        "study_program": "Bachelor's Program in Information Systems",
        "bio": (
            "Information Systems undergraduate at Universitas Indonesia "
            "interested in solving business challenges through strategic "
            "thinking, data-driven analysis, and technology. Experienced "
            "in educational programs, student advocacy, and project coordination."
        ),
        "last_login": request.COOKIES.get(
            "last_login",
            "No login session has been recorded in this browser.",
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experiences_json(request)
    experiences = serializers.deserialize("json", json_response.content.decode("utf-8"))
    context = {
        "name": "Sultan Noor Dafiq",
        "experience_list": [experience.object for experience in experiences],
        "experience_query": request.GET.get("q", "").strip(),
        "category_query": request.GET.get("category", "").strip(),
        "experience_categories": Experience.EXPERIENCE_CHOICES,
        "is_editor": is_experience_editor(request.user),
    }
    return render(request, "experience.html", context)


def get_experiences_json(request):
    experiences = Experience.objects.all()
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()

    if query:
        experiences = experiences.filter(
            Q(title__icontains=query) | Q(organization__icontains=query)
        )
    if category:
        experiences = experiences.filter(category=category)

    return HttpResponse(
        serializers.serialize(
            "json",
            experiences,
            fields=(
                "title",
                "organization",
                "period",
                "display_order",
                "description",
                "category",
                "thumbnail",
                "started_at",
                "ended_at",
                "skills",
            ),
        ),
        content_type="application/json",
    )


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience added successfully.")
        return redirect("main:show_experience")

    context = {
        "name": "Sultan Noor Dafiq",
        "form": form,
    }
    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not can_update_experience(request.user):
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience updated successfully.")
        return redirect("main:show_experience")

    context = {
        "name": "Sultan Noor Dafiq",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
@require_POST
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)
    experience_title = experience.title
    experience.delete()
    messages.success(
        request,
        f'Experience "{experience_title}" deleted successfully.',
    )
    return redirect("main:show_experience")


@login_required(login_url="/login/")
@require_POST
def toggle_experience_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if experience.starred_by.filter(pk=request.user.pk).exists():
        experience.starred_by.remove(request.user)
    else:
        experience.starred_by.add(request.user)
    return redirect("main:show_experience")


def show_certifications(request):
    json_response = get_certifications_json(request)
    certifications = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    context = {
        "name": "Sultan Noor Dafiq",
        "certification_list": [
            certification.object for certification in certifications
        ],
        "title_query": request.GET.get("title", "").strip(),
    }
    return render(request, "certifications.html", context)


def get_certifications_json(request):
    title_query = request.GET.get("title", "").strip()
    certifications = Certification.objects.all()

    if title_query:
        certifications = certifications.filter(title__icontains=title_query)

    certifications_json = serializers.serialize(
        "json",
        certifications,
        use_natural_foreign_keys=True,
    )
    return HttpResponse(certifications_json, content_type="application/json")


@login_required(login_url="/login/")
def create_certification(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = CertificationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Certification added successfully.")
        return redirect("main:show_certifications")

    context = {
        "name": "Sultan Noor Dafiq",
        "form": form,
    }
    return render(request, "certification_form.html", context)


@login_required(login_url="/login/")
@require_POST
def delete_certification(request, certification_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    certification = get_object_or_404(Certification, pk=certification_id)
    certification_title = certification.title
    certification.delete()
    messages.success(
        request,
        f'Certification "{certification_title}" deleted successfully.',
    )
    return redirect("main:show_certifications")


@login_required(login_url="/login/")
@require_POST
def toggle_certification_star(request, certification_id):
    certification = get_object_or_404(Certification, pk=certification_id)
    if certification.starred_by.filter(pk=request.user.pk).exists():
        certification.starred_by.remove(request.user)
    else:
        certification.starred_by.add(request.user)
    return redirect("main:show_certification_detail", certification_id=certification.id)


def show_certification_detail(request, certification_id):
    context = {
        "name": "Sultan Noor Dafiq",
        "certification": get_object_or_404(
            Certification,
            pk=certification_id,
        ),
    }
    return render(request, "certification_detail.html", context)
