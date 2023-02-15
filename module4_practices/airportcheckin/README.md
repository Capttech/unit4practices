# README

1. Create a model called Airline.
2. In Airline it should have the following fields:

- [ ] 'Date' a DateField that takes datetime with date of the flight.
- [ ] 'Destination' a TextField that takes the destination.
- [ ] 'Passenger' a TextField that takes the passenger name.
- [ ] 'Bags' an OPTIONAL that defaults to 0, IntegerField that takes the number of checked luggage.
- [ ] 'FirstClass' a BooleanField that takes True/False for if they are first class or not. It should default to False.

3. You should have the following functions capable in your model:

- [ ] Create a ticket.
- [ ] Find a ticket by id.
- [ ] Give a list of all tickets
- [ ] Upgrade to first class: makes the first class field true.
- [ ] Delete a ticket given the object id.
- [ ] Filter tickets by destination.
- [ ] Filter tickets by first class, should only show passengers that are first class.
- [ ] Update a tickets checked bags value.
