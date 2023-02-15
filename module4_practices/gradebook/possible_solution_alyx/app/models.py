from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Gradebook(models.Model):
    assignment = models.TextField()
    percentage = models.IntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    name = models.TextField()
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)


def create_grade(assignment, name, date, percentage=0, notes=None):
    grade = Gradebook(
        assignment=assignment, percentage=percentage, name=name, date=date, notes=notes
    )
    grade.save()
    return grade


def find_grade(id):
    return Gradebook.objects.get(id=id)


def update_percent(id, percentage):
    grade = find_grade(id)
    grade.percentage = percentage
    grade.save()
    return grade


def update_notes(id, notes):
    grade = find_grade(id)
    grade.notes = notes
    grade.save()
    return grade


def delete_grade(id):
    grade = find_grade(id)
    grade.delete()


def all_grades():
    return Gradebook.objects.all()


def filter_by_name(name):
    return Gradebook.objects.filter(name=name)


def filter_by_assignment(assignment):
    return Gradebook.objects.filter(assignment=assignment)


def filter_by_pass_assignment(assignment, percentage):
    return Gradebook.objects.filter(assignment=assignment, percentage__gte=percentage)
