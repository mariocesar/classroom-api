from django.db import models

from classroom.core.managers import CoreManager


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        ACTIVE = "active", "Active"
        CLOSED = "closed", "Closed"

    category = models.ForeignKey(
        Category, related_name="courses", on_delete=models.PROTECT
    )
    status = models.CharField(max_length=10, choices=Status.choices)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    collections = models.ManyToManyField(Collection, blank=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    class Type(models.TextChoices):
        LESSON = "lesson", "Lesson"
        QUIZ = "quiz", "Quiz"
        PROJECT = "project", "Project"

    type = models.CharField(choices=Type.choices, max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    sequence = models.IntegerField()

    class Meta:
        verbose_name_plural = "activities"

    def __str__(self):
        return f"{self.type} / {self.title}"


class Lesson(Activity):
    objects = CoreManager(type=Activity.Type.LESSON)

    class Meta:
        proxy = True

    def __str__(self):
        return f"{self.title}"


class Quiz(Activity):
    objects = CoreManager(type=Activity.Type.QUIZ)

    class Meta:
        proxy = True

    def __str__(self):
        return f"{self.title}"


class Project(Activity):
    objects = CoreManager(type=Activity.Type.PROJECT)

    class Meta:
        proxy = True

    def __str__(self):
        return f"{self.title}"
