In this practice you need to accomplish the following:

1. Create a model called Gradebook.
2. In Gradebook it should have the following fields:

- [ ] 'Assignment Name' a string that is the name of the assignment.
- [ ] 'Percentage' - an integer stating the number grade the student received on that assignment. This should default to 0 if no grade is given and should only allow you to put a number between 0 and 100.
- [ ] 'Student Name' a string that is the name of the student
- [ ] 'Date' a datetime field that gives the day month and year of when the assignment was given.
- [ ] 'Notes' an optional string field for any extra notations.

3. You should have the following functions capable in your model:

- [x] Create a Grade.
- [x] Find a grade by it's id.
- [x] Update the percentage of a grade.
- [x] Update the notes of a grade.
- [x] Remove a grade from the system (Delete a grade model)
- [x] Filter grades by student name.
- [x] Filter grades by assignment name.
- [ ] Filter grades by assignment name and greater than or equal to a percentage.

4. You should write your own tests for each of these functionalities.
