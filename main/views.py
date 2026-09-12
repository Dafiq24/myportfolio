from django.shortcuts import get_object_or_404, render

from main.models import Certification, Experience

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
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Sultan Noor Dafiq",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_certifications(request):
    context = {
        "name": "Sultan Noor Dafiq",
        "certification_list": Certification.objects.all(),
    }
    return render(request, "certifications.html", context)


def show_certification_detail(request, certification_id):
    context = {
        "name": "Sultan Noor Dafiq",
        "certification": get_object_or_404(
            Certification,
            pk=certification_id,
        ),
    }
    return render(request, "certification_detail.html", context)
