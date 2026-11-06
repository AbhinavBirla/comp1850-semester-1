# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    def __init__(self, name, birth):
        """Creates a Person with a name and date of birth."""
        if type(name) != str:
            raise TypeError

        if name == "":
            raise ValueError

        if type(birth) != date:
            raise TypeError

        self.name = name
        self.birth = birth

    def initials(self):
        """Return the initials of the person's name."""

        initials = ""

        for word in self.name.split():
            initials += word[0].upper()

        return initials

    def is_birthday(self):
        """Return True if today is person's birthday"""

        today = date.today()
        return today.day == self.birth.day and today.month == self.birth.month
 
    
        
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
