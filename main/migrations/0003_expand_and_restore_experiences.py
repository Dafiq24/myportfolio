from django.db import migrations, models


EXPERIENCES = [
    {
        "title": "HR Software Engineering Academy",
        "organization": "COMPFEST 18",
        "period": "March 2026 - Present",
        "display_order": 1,
        "description": (
            "Supported staff recruitment communications and coordinated "
            "administrative screening, interviews, and onboarding."
        ),
        "category": "volunteer",
        "skills": "Recruitment, Coordination, Communication",
        "ongoing": True,
    },
    {
        "title": "Super Member",
        "organization": "Google Developer Groups on Campus UI",
        "period": "January 2026 - June 2026",
        "display_order": 2,
        "description": (
            "Practiced data preparation, exploratory data analysis, and basic "
            "feature engineering with Python, Pandas, and NumPy."
        ),
        "category": "volunteer",
        "skills": "Python, Data Analysis, Team Learning",
        "ongoing": False,
    },
    {
        "title": "Teaching Staff",
        "organization": "BETIS Fasilkom UI",
        "period": "January 2026 - March 2026",
        "display_order": 3,
        "description": (
            "Guided the learning process of more than 100 prospective UTBK "
            "participants using presentation materials and quizzes."
        ),
        "category": "part-time",
        "skills": "Teaching, Content Development, Public Communication",
        "ongoing": False,
    },
    {
        "title": "Advocacy & Student Welfare Intern",
        "organization": "BEM Fasilkom UI",
        "period": "September 2025 - December 2025",
        "display_order": 4,
        "description": (
            "Coordinated an interactive mental-health activity for more than "
            "100 participants and contributed to educational content and "
            "student aspiration outreach."
        ),
        "category": "internship",
        "skills": "Student Advocacy, Content Development, User Empathy",
        "ongoing": False,
    },
]


def restore_experiences(apps, schema_editor):
    Experience = apps.get_model("main", "Experience")
    for source in EXPERIENCES:
        item = source.copy()
        ongoing = item.pop("ongoing")
        experience, _ = Experience.objects.update_or_create(
            title=item["title"],
            defaults=item,
        )
        if not ongoing and experience.ended_at is None:
            experience.ended_at = experience.started_at
            experience.save(update_fields=["ended_at"])


def remove_restored_experiences(apps, schema_editor):
    Experience = apps.get_model("main", "Experience")
    Experience.objects.filter(
        title__in=[item["title"] for item in EXPERIENCES]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_certification"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="organization",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="experience",
            name="display_order",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="experience",
            name="period",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="experience",
            name="skills",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.RunPython(
            restore_experiences,
            remove_restored_experiences,
        ),
        migrations.AlterModelOptions(
            name="experience",
            options={"ordering": ["display_order", "-started_at"]},
        ),
    ]
