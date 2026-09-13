from django.db import migrations


CERTIFICATIONS = [
    {
        "title": "Finalist - ShARE Global Case Summit",
        "issuer": "ShARE ITB, DWDG UGM & ShARE UB",
        "category": "achievement",
        "issued_year": 2026,
        "image_path": "img/certificates/sgcs-finalist.jpg",
        "description": "Finalist in the ShARE Global Case Summit 2026.",
        "is_featured": True,
    },
    {
        "title": "Gemini Certified Student",
        "issuer": "Google for Education",
        "category": "certification",
        "issued_year": 2026,
        "image_path": "img/certificates/gemini-certified-student.jpg",
        "description": (
            "Recognition of foundational knowledge in generative AI."
        ),
        "is_featured": False,
    },
    {
        "title": "Super Member of Data Science",
        "issuer": "GDGoC Universitas Indonesia",
        "category": "certification",
        "issued_year": 2026,
        "image_path": "img/certificates/super-member-data-science.png",
        "description": "Completed learning activities in data science.",
        "is_featured": False,
    },
    {
        "title": "Java Collections Framework",
        "issuer": "Udemy",
        "category": "course",
        "issued_year": 2026,
        "image_path": "img/certificates/java-collections.png",
        "description": (
            "Studied Java collections, generics, lambdas, and Stream API."
        ),
        "is_featured": False,
    },
    {
        "title": "GDP Labs: AI Engineer Session",
        "issuer": "RISTEK Fasilkom UI & GDP Labs",
        "category": "workshop",
        "issued_year": 2026,
        "image_path": "img/certificates/ai-engineer-session.jpg",
        "description": "Participated in an AI engineering workshop.",
        "is_featured": False,
    },
    {
        "title": "HTML Certificate of Completion",
        "issuer": "Mimo",
        "category": "course",
        "issued_year": 2025,
        "image_path": "img/certificates/mimo-html.jpg",
        "description": "Completed foundational HTML coursework.",
        "is_featured": False,
    },
]


def seed_certifications(apps, schema_editor):
    Certification = apps.get_model("main", "Certification")
    for certification in CERTIFICATIONS:
        Certification.objects.update_or_create(
            title=certification["title"],
            defaults=certification,
        )


def remove_seeded_certifications(apps, schema_editor):
    Certification = apps.get_model("main", "Certification")
    Certification.objects.filter(
        title__in=[certification["title"] for certification in CERTIFICATIONS]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_expand_and_restore_experiences"),
    ]

    operations = [
        migrations.RunPython(
            seed_certifications,
            remove_seeded_certifications,
        ),
    ]
