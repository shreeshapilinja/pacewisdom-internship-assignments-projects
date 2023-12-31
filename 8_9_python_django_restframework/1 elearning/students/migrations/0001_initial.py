from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=100)),
                ("otp_code", models.CharField(max_length=6)),
                (
                    "subscribed_courses",
                    models.ManyToManyField(
                        related_name="subscribed_students", to="teachers.course"
                    ),
                ),
            ],
        ),
    ]
