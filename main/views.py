from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.http import url_has_allowed_host_and_scheme
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


def get_safe_next_url(request):
    """Return a local post-login destination or an empty string."""
    next_url = request.POST.get("next") or request.GET.get("next", "")
    if next_url and url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return next_url
    return ""


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
    next_url = get_safe_next_url(request)
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        response = redirect(next_url or "main:show_main")
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
        {
            "name": "Sultan Noor Dafiq",
            "form": form,
            "next_url": next_url,
        },
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
    context = {
        "name": "Sultan Noor Dafiq",
        "form": ExperienceForm(),
        "experience_query": request.GET.get("q", "").strip(),
        "category_query": request.GET.get("category", "").strip(),
        "experience_categories": Experience.EXPERIENCE_CHOICES,
        "is_editor": is_experience_editor(request.user),
    }
    return render(request, "experience.html", context)


def get_experiences_json(request):
    experiences = Experience.objects.prefetch_related("starred_by").all()
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()

    if query:
        experiences = experiences.filter(
            Q(title__icontains=query) | Q(organization__icontains=query)
        )
    if category:
        experiences = experiences.filter(category=category)

    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        data.append(
            {
                "pk": str(experience.id),
                "fields": {
                    "title": experience.title,
                    "organization": experience.organization,
                    "period": experience.period,
                    "display_order": experience.display_order,
                    "description": experience.description,
                    "category": experience.category,
                    "category_display": experience.get_category_display(),
                    "thumbnail": experience.thumbnail,
                    "started_at": experience.started_at.isoformat(),
                    "ended_at": (
                        experience.ended_at.isoformat()
                        if experience.ended_at
                        else None
                    ),
                    "is_ongoing": experience.is_ongoing,
                    "skills": experience.skills,
                    "skill_list": experience.skill_list,
                    "star_count": len(starred_users),
                    "is_starred": (
                        request.user.is_authenticated
                        and any(
                            user.pk == request.user.pk for user in starred_users
                        )
                    ),
                },
            }
        )

    return JsonResponse(data, safe=False)


@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add experiences."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {
                "message": "Experience added successfully.",
                "pk": str(experience.id),
            },
            status=201,
        )

    return JsonResponse(
        {"errors": form.errors.get_json_data()},
        status=400,
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
    context = {
        "name": "Sultan Noor Dafiq",
        "title_query": request.GET.get("title", "").strip(),
        "form": CertificationForm(),
    }
    return render(request, "certifications.html", context)


def get_certifications_json(request):
    title_query = request.GET.get("title", "").strip()
    certifications = Certification.objects.prefetch_related("starred_by").all()

    if title_query:
        certifications = certifications.filter(title__icontains=title_query)

    data = []
    for certification in certifications:
        starred_users = certification.starred_by.all()
        data.append(
            {
                "pk": str(certification.id),
                "fields": {
                    "title": certification.title,
                    "issuer": certification.issuer,
                    "category": certification.category,
                    "category_display": certification.get_category_display(),
                    "issued_year": certification.issued_year,
                    "image_path": certification.image_path,
                    "credential_url": certification.credential_url,
                    "description": certification.description,
                    "is_featured": certification.is_featured,
                    "star_count": len(starred_users),
                    "is_starred": (
                        request.user.is_authenticated
                        and any(
                            user.pk == request.user.pk for user in starred_users
                        )
                    ),
                },
            }
        )

    return JsonResponse(data, safe=False)


@require_POST
def create_certification_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {
                "message": (
                    "Only the portfolio owner can add certifications."
                )
            },
            status=403,
        )

    form = CertificationForm(request.POST)
    if form.is_valid():
        certification = form.save()
        return JsonResponse(
            {
                "message": "Certification added successfully.",
                "pk": str(certification.id),
            },
            status=201,
        )

    return JsonResponse(
        {"errors": form.errors.get_json_data()},
        status=400,
    )


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


def permission_denied_view(request, exception):
    """Render a helpful response without exposing permission internals."""
    return render(
        request,
        "403.html",
        {"name": "Sultan Noor Dafiq"},
        status=403,
    )
