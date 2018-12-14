# Here is a basic class that takes in a name, personal email, and work email.
# In order to validate that the user is inputting correct information we have had to

import re
from weakref import WeakKeyDictionary

EMAIL_REGEX = re.compile(
    r"[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@"
    "[A-Za-z0-9-]+(.[A-Za-z0-9]+)*(.[A-Za-z]{2,})"
)


def ValidateEmail(email_address):
    """
    Validates an email address:

    Raises:
        ValueError: If the email is invalid.
    """
    if not EMAIL_REGEX.match(email_address):
        raise ValueError


class Email(object):
    """Descriptor class used to hold an email address."""

    def __init__(self):
        """
        Initializes the object.

        Attrs:
            pool: (WeakKeyDictionary) Maps object instance to a corresponding email address.
        """
        self.pool = WeakKeyDictionary()

    def __get__(self, instance, owner):
        """
        Called when the user is accessing a class level instance of type Email.

        For example assuming the following class:

            class Employee(object):
                email = Email()

        and an instance of it:

            employee = Employee()

        The following assignment

            x = employee.email

        will call this method.

        Args:
            instance : (python object) the python object having a class level attribute of type email.
            owner : The type of the calling object. Not used here.

        Returns:
            (string) The email as it exists in the pool.
        """
        return self.pool.get(instance, 0)

    def __set__(self, instance, email_address):
        """
        Called when the user sets the value of a class level instance of type Email.

        For example assuming the following class:

        class Employee(object):
            email = Email()

        and an instance of it:
            employee = Email()

        The following assignment

            employee.email = 'first.lastname@some_server.com'

        will call this method.

        Raises:
             ValueError: When passed an invalid email address.
        Args:
            instance: (python object) the python object having a class level attribute of type Email.
            email_address: The value to assign.
        """
        if not EMAIL_REGEX.match(email_address):
            raise ValueError
        self.pool[instance] = email_address


class Employee(object):
    """
    Used to demo the use of descriptors.
    """
    personal_email = Email()
    work_email = Email()

    def __init__(self, name, personal_email, work_email):
        self.name = name
        self.personal_email = personal_email
        self.work_email = work_email


# Creating two employees.
johnDoe = Employee(name='John Doe', personal_email='john.doe@personal.com', work_email='john.doe@work.com')
mikeSmith = Employee(name='Mike Smith', personal_email='mike.smith@personal.com', work_email='mike.smith@work.com')

# Try and create an invalid employee assignment.
try:
    jessCitizen = Employee(name='Jess Citizen', personal_email='jess.citizen@personal.com', work_email='jess.citizen@')
except ValueError:
    print("Failed to assign email.")

# Print
print(johnDoe.personal_email)
print(mikeSmith.personal_email)

