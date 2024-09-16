import os
import sys
from pathlib import Path
from datetime import datetime

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings"

settings.USE_TZ = False

django.setup()

if __name__ == "__main__":
    import faker
    from random import choice

    from contact.models import Contact, Category

    Contact.objects.all().delete()  # Deleta todos os contatos
    Category.objects.all().delete()  # Deleta todas as categorias

    fake = faker.Faker("pt_BR")
    categories = ["Amigos", "Familia", "Conhecidos"]

    django_categories = [Category(name=name) for name in categories]
    for category in django_categories:
        category.save()

    django_contacts = []
    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email: str = profile["mail"]
        first_name, last_name = profile["name"].split(" ", 1)
        phone: str = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=200)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)
