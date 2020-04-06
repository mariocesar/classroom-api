import factory
from factory import fuzzy

from classroom.apps.courses.models import (Activity, Category, Collection,
                                           Course)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("company")


class CollectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Collection

    name = factory.Faker("company")


class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Course

    name = factory.Faker("company")
    status = fuzzy.FuzzyChoice(Course.Status.values)
    category = factory.SubFactory(CategoryFactory)
    description = factory.Faker("paragraph")

    @factory.post_generation
    def collections(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for collection in extracted:
                self.collections.add(collection)


class ActivityFactory(factory.DjangoModelFactory):
    class Meta:
        model = Activity

    type = fuzzy.FuzzyChoice(Activity.Type.values)
    course = factory.SubFactory(CourseFactory)
    title = factory.Faker("sentence")
    content = factory.Faker("text")
    sequence = factory.Sequence(lambda n: n)
