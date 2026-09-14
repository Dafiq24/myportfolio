from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import CertificationForm
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

    certifications_json = serializers.serialize("json", certifications)
    return HttpResponse(certifications_json, content_type="application/json")


def create_certification(request):
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


def show_certification_detail(request, certification_id):
    context = {
        "name": "Sultan Noor Dafiq",
        "certification": get_object_or_404(
            Certification,
            pk=certification_id,
        ),
    }
    return render(request, "certification_detail.html", context)
