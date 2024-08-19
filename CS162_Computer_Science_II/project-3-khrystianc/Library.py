# Author: Khrystian Clark
# Date: 10/12/2020
# Description: A basic Library Simulator that involves patrons, items and transactions.


class LibraryItem:
    """Library class that holds item, title, location, person with book,
    person requesting book, and date data members established"""
    library_item_id = ''
    title = ''
    location = ''
    checked_out_by = ''
    requested_by = ''
    date_checked_out = 0

    def __init__(self, item_id, title):
        """Initializing method for the private data members, including item id's and the title of the item"""
        self.library_item_id = item_id
        self.title = title
        self.checked_out_by = None
        self.requested_by = None
        self.location = 'ON_SHELF'
        self.date_checked_out = 0

    def get_item_id(self):
        """Retrieves the item ID from the library_item_id"""
        return self.library_item_id

    def get_title(self):
        """Retrieves the title from the private data member 'title'."""
        return self.title

    def get_location(self):
        """Retrieves the location of a library item"""
        return self.location

    def get_checked_out_by(self):
        """Retrieves which patron a library item is checked out to"""
        return self.checked_out_by

    def get_requested_by(self):
        """Refers to the patron that has requested an item in the library, if any"""
        return self.requested_by

    def get_date_checked_out(self):
        """Retrieves the date the library item was checked out"""
        return self.date_checked_out

    def set_item_id(self, item_id):
        """Sets the library item id to a given value"""
        self.library_item_id = item_id

    def set_title(self, title):
        """Sets the title of an item to a given value"""
        self.title = title

    def set_location(self, location):
        """Sets the library item's location to on hold, on the shelf or checked out"""
        self.location = location

    def set_checked_out_by(self, person_name):
        """Gives a value to which patron has a certain item checked out"""
        self.checked_out_by = person_name

    def set_requested_by(self, request_name):
        """Sets up who has requested any arbitrary library item"""
        self.requested_by = request_name

    def set_date_checked_out(self, day):
        """Sets the date that the library item was checked out"""
        self.date_checked_out = day


class Book(LibraryItem):
    """Subclass inheriting from the LibraryItem that holds information on books in question"""
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.author = author

    def set_author(self, author):
        """Establishes the author of a book in the library"""
        self.author = author

    def get_author(self):
        """Retrieves the author information on a book in the library"""
        return self.author

    def get_check_out_length(self):
        """returns the number of days the item can be checked out"""
        return 21


class Album(LibraryItem):
    """Subclass, inheriting from the LibraryItem that holds information on Albums in question"""
    def __init__(self, item_id, title, artist):
        super().__init__(item_id, title)
        self.artist = artist

    def set_author(self, artist):
        """Establishes an artists name of a library object"""
        self.artist = artist

    def get_artist(self):
        """Retrieves and artist's name from an object in the library"""
        return self.artist

    def get_check_out_length(self):
        """returns the number of days the item can be checked out"""
        return 14


class Movie(LibraryItem):
    """Subclass, inheritng from the LibraryItem that holds information on Movies in question"""
    def __init__(self, item_id, title, director):
        super().__init__(item_id, title)
        self.director = director

    def set_director(self, director):
        """Establishes the director of a film in the library"""
        self.director = director

    def get_director(self):
        """Retrieves the director of a movie in the library"""
        return self.director

    def get_check_out_length(self):
        """returns the number of days the item can be checked out"""
        return 7


class Patron:
    """Class that establishes patron identifier, names, their checked out items, and the amount they owe."""
    def __init__(self, patron_id, patron_name):
        """Initializes patron id's,names, checked out items and their fine amount"""
        self.patron_id = patron_id
        self.name = patron_name
        self.checked_out_items = []
        self.fine_amount = 0.00

    def set_patron_id(self, patron_id):
        """Established the identifier for a specific patron"""
        self.patron_id = patron_id

    def set_name(self, patron_name):
        """Establishes the name of a patron"""
        self.name = patron_name

    def set_fine_amount(self, amount_owed):
        """Establishes the amount a patron owes"""
        self.fine_amount = amount_owed

    def get_patron_id(self):
        """Retrieves the id of the patron"""
        return self.patron_id

    def get_name(self):
        """Retrieves the name of a patron"""
        return self.name

    def get_fine_amount(self):
        """Retrieves the amount a patron owes"""
        return self.fine_amount

    def add_library_item(self, library_item):
        """adds a library to the list of items a patron has checked out"""
        self.checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """Removes a library item from a patron's checked out items"""
        self.checked_out_items.remove(library_item)

    def amend_fine(self, charges):
        """An argument that increases or decreases the amount owed by a patron"""
        self.fine_amount = self.fine_amount + charges

    def get_checked_out_items(self):
        return self.checked_out_items


class Library:
    """The class that establishes what is and is not in the library, and the members of the library"""
    holdings = []
    members = []

    def __init__(self):
        """Initializes the list of library items and the current date"""
        self.holdings = []
        self.members = []
        self.current_date = 0

    def set_current_date(self, day):
        """Sets the current date as a day"""
        self.current_date = day

    def get_current_date(self):
        """Retrieves the current date"""
        return self.current_date

    def add_library_item(self, library_item):
        """Takes a library item and adds it to the holdings list"""
        self.holdings.append(library_item)

    def add_patron(self, patron):
        """Takes on a patron and adds them to the members list"""
        self.members.append(patron)

    def get_library_item_from_id(self, library_item):
        """This method returns the library item with an input ID parameter. Or else None"""
        for item in self.holdings:
            if library_item == item.get_item_id():
                return item
            return None

    def get_patron_from_id(self, patron_id):
        """This method returns a patron that has a corresponding ID from with the members list"""
        for member in self.members:
            if patron_id == member.get_patron_id():
                return member
            return None

    def check_out_library_item(self, person_id, library_item_id):
        """This method checks out a library otem to a patron, or else gives the items status/location"""
        patron_id = self.get_patron_from_id(person_id)
        library_item = self.get_library_item_from_id(library_item_id)
        if patron_id is None:
            return "patron not found"
        if library_item is None:
            return "item not found"
        if library_item.get_location() == "CHECKED_OUT":
            return "item already checked out"
        elif library_item.get_location() == "ON_HOLD_SHELF":
            return "item on hold by other patron"
        library_item.set_checked_out_by(patron_id)
        library_item.set_date_checked_out(self.current_date)
        library_item.set_location("CHECKED_OUT")
        if library_item.get_requested_by() == person_id:
            library_item.set_requested_by(None)
        patron_id.add_library_item(self, library_item_id)
        return "check out successful"

    def return_library_item(self, person_id, library_item_id):
        """This method returns an item to the library, or else gives its status or location"""
        library_item = self.get_library_item_from_id(library_item_id)
        if library_item is None:
            return "item not found"
        if library_item.get_location != "CHECKED_OUT":
            return "item already in library"
        person_id = self.get_patron_from_id(person_id)
        person_id.remove_library_item(library_item_id)
        if library_item_id.get_requested_by is not None:
            library_item_id.set_location("ON_HOLD_SHELF")
        else:
            library_item_id.set_location("ON_SHELF")
            library_item_id.set_checked_out_by(None)
            return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """This method is used for a patron to request a library item and returns the item's status
        if it not available"""
        patron = self.get_patron_from_id(patron_id)
        library_item = self.get_library_item_from_id(library_item_id)
        if patron is None:
            return "patron not found"
        if library_item is None:
            return "item not found"
        if library_item.get_location == "ON_HOLD_SHELF":
            return "item already on hold"
        else:
            library_item.set_requested_by(patron_id)
        if library_item.get_location == "ON_SHELF":
            library_item.set_location("ON_HOLD_SHELF")
            return "request successful"

    def pay_fine(self, patron_id, amount_paid):
        """Retrieves a patron from the list, if they are a member, this gives the
        remainder of the account balance after they paid an amount"""
        patron_id = self.get_patron_from_id(amount_paid)
        if patron_id is None:
            return "patron not found"
        else:
            patron.ammend_fine(amount_owed)
            return "payment successful"

    def increment_current_date(self):  #This is where i got stuck
        """Takes the amount of days a patron has an item checked out and adds 10 cents for each
        item that is overdue"""
        current_date = self.current_date + 1
        length = current_date - get_check_out_date
        if length >= get_check_out_length:
            return "OVERDUE"
        else:
            return length.ammend_fine(self.current_date * .10)

