import random

from django.core.management import BaseCommand

from classroom.apps.courses.factories import (
    CategoryFactory,
    CollectionFactory,
    CourseFactory,
    ActivityFactory,
)
from classroom.apps.courses.models import Category, Collection, Course


class Command(BaseCommand):
    def handle(self, *args, **options):
        count = Category.objects.all().count()

        if count < 20:
            CategoryFactory.create_batch(size=20 - count)

        print("Categories: ", Category.objects.all().count())

        count = Collection.objects.all().count()

        if count < 100:
            CollectionFactory.create_batch(size=100 - count)

        print("Collections: ", Collection.objects.all().count())

        categories = [cat for cat in Category.objects.all()]
        collections = [col for col in Collection.objects.all()]

        count = Course.objects.all().count()

        print("Courses: ", Course.objects.all().count(), end="\r", flush=True)

        if count < 1000:

            for n in range(1000 - count):
                print("Courses: ", Course.objects.all().count(), end="\r", flush=True)

                course = CourseFactory.create(
                    category=random.sample(categories, 1).pop(),
                    collections=random.sample(collections, 5),
                )

                ActivityFactory.create_batch(20, course=course)

        print("")
