from django.contrib import admin

from classroom.apps.courses.models import (
    Activity,
    Category,
    Collection,
    Course,
    Lesson,
    Project,
    Quiz,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    ...


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    ...


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    ...


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    ...


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    ...


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    ...
