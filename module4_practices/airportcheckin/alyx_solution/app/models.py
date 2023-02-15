from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Airline(models.Model):
    date = models.DateField()
    destination = models.TextField()
    passenger = models.TextField()
    bags = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
    firstclass = models.BooleanField(default=False)


def create_ticket(date, destination, passenger, bags=0):
    ticket = Airline(date=date, destination=destination, passenger=passenger, bags=bags)
    ticket.save()
    return ticket


def find_ticket(x):
    try:
        ticket = Airline.objects.get(id=x)
        return ticket
    except Airline.DoesNotExist:
        raise ValueError("Ticket does not exist.")


def upgrade_firstclass(id):
    ticket = find_ticket(id)
    if not ticket.firstclass:
        ticket.firstclass = True
        ticket.save()
        return ticket
    else:
        raise ValueError("Already First Class!")


def all_tickets():
    return Airline.objects.all()


def delete_ticket(id):
    ticket = find_ticket(id)
    ticket.delete()


def filter_by_destination(x):
    return Airline.objects.filter(destination=x)


def filter_by_firstclass():
    return Airline.objects.filter(firstclass=True)


def update_bags(id, bags):
    ticket = find_ticket(id)
    ticket.bags = bags
    ticket.save()
    return ticket
