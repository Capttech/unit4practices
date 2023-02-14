from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class gradeBook(models.Model):
    assignmentName = models.TextField()
    percentage = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])
    studentName = models.TextField()
    date = models.DateField()
    notes = models.TextField()

    
def createGrade(assignmentName, percentage, studentName, date, notes=''):
    createdGrade = gradeBook(assignmentName=assignmentName, percentage=percentage, studentName=studentName, date=date, notes=notes)
    createdGrade.save()
    return createdGrade


def findGrade(id):
    return gradeBook.objects.get(id=id)


def updateGrade(id, grade):
    foundGrade = gradeBook.objects.get(id=id)
    foundGrade.percentage = grade
    return foundGrade


def updateNotes(id, note):
    foundGrade = gradeBook.objects.get(id=id)
    foundGrade.notes = note
    return foundGrade


def removeGrade(id):
    foundGrade = gradeBook.objects.get(id=id)
    foundGrade.delete()


def getAllGrades():
    return gradeBook.objects.all()


def filterGradeName(testName):
    return gradeBook.objects.filter(assignmentName=testName)
     

def filterGradeNamePercent(testName, testPercent):
    return gradeBook.objects.filter(assignmentName=testName, percentage=testPercent)


























# Create your models here.
# class Taxi(models.Model):
#     occupied = models.BooleanField()
#     capacity = models.IntegerField()
#     fare = models.IntegerField()
#     passengers = models.IntegerField()
#     notes = models.TextField(null=True, default="")
#     taxi_number = models.IntegerField(default=111)

#     def save(self, *args, **kwargs):
#         allTaxi = Taxi.objects.all()

#         if allTaxi.exists() and self._state.adding:
#             taxis_sorted = sorted(allTaxi, key=lambda c: c.taxi_number)
#             last_taxi = taxis_sorted[-1]
#             self.taxi_number = last_taxi.taxi_number + 11
#         super().save(*args, **kwargs)


# def create_taxi(occupied, capacity, fare, passengers, notes=""):
#     cratedTaxi = Taxi(
#         occupied=occupied,
#         capacity=capacity,
#         fare=fare,
#         passengers=passengers,
#         notes=notes,
#     )
#     cratedTaxi.save()
#     return cratedTaxi


# def all_taxis():
#     return Taxi.objects.all()


# def remove_taxi(taxiNumber):
#     try:
#         data = Taxi.objects.get(taxi_number=taxiNumber)
#         data.delete()
#     except:
#         raise ValueError


# def filter_free_taxis():
#     return Taxi.objects.filter(occupied=False)


# def filter_free_capacity_taxis(capacity):
#     return Taxi.objects.filter(occupied=False, capacity__gte=capacity)


# def finish_fare(taxiNumber, distance):
#     data = Taxi.objects.get(taxi_number=taxiNumber)
#     if data.occupied == False:
#         raise ValueError
#     totalFare = data.fare * distance
#     return totalFare


# def send_taxi_out(taxiNumber, numPassengers):
#     data = Taxi.objects.get(taxi_number=taxiNumber)

#     if data.capacity < numPassengers:
#         raise ValueError

#     data.occupied = True
#     data.passengers = numPassengers
#     return data
