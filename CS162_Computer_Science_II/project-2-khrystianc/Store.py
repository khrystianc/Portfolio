# Author: Khrystian Clark
# Date: 10/5/2020
# Description: This is a primitive store simulator that includes product descriptions and membership info.

class InvalidCheckoutError(Exception):
    """Initiates the possibility of the invalid checkout error that responds with an explanatory message to the user"""
    pass


class Product:
    """Object that takes in five private entries that are details of the store's products"""

    def __init__(self, product_id, title, description, price, quantity_available):
        """Takes on the five parameters that initialize the Product class: product_id,
        title, description, price, quantity_available"""
        self._product_id = product_id
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_product_id(self):
        """Get method for product_id"""
        return self._product_id

    def get_title(self):
        """Get method for title"""
        return self._title

    def get_price(self):
        """Get method for price"""
        return self._price

    def get_description(self):
        """Get method for description"""
        return self._description

    def get_quantity_available(self):
        """Get method for quantity_available"""
        return self._quantity_available

    def decrease_quantity(self):
        """This method decreases the quantity by one, every iteration it is run"""
        self._quantity_available -= 1
        return self._quantity_available


class Customer:
    """Object that takes in the customer information in three private entries"""

    def __init__(self, name, customer_id, premium_member):
        """Takes on the three parameters that initialize the Customer class: name, customer_id, premium_member"""
        self._name = name
        self._customer_id = customer_id
        self._premium_member = premium_member  # boolean value
        self._cart = []  # creates the cart list

    def get_name(self):
        """Get method for customer name"""
        return self._name

    def get_customer_id(self):
        """Get method for customer_id"""
        return self._customer_id

    def get_cart(self):
        """Get method for a customer's cart"""
        return self._cart

    def is_premium_member(self):
        """Method to define if a member is a premium member, returns a boolean"""
        return self._premium_member

    def add_product_to_cart(self, new_product_id):
        """Add method that takes product id code and adds it the cart list"""
        self._cart.append(new_product_id)

    def empty_cart(self):
        """This method empties a customer's cart, when initialized"""
        self._cart = []


class Store:
    """The object that conducts the most functions within store, adding members
    and inventory and checking out members' carts"""

    def __init__(self):
        """Initializes the inventory and membership dictionaries/directories as data members"""
        self._inventory = dict()  # list or dictionary of the store's products
        self._membership = dict()  # list or dictionary of the customers that are members
        # this should initialize anything needed for the store

    def add_product(self, new_product):
        """Takes Product object and adds it to the store inventory"""
        self._inventory[new_product.get_product_id()] = new_product
        # adds a product object to the store inventory

    def add_member(self, new_member):
        """Takes the Customer object and adds it to the membership directory"""
        self._membership[new_member.get_customer_id()] = new_member

    def get_product_from_id(self, product_id):
        """Take a product ID and returns the product with the given ID,
        returns None if there is no matching product"""
        for item in self._inventory:
            if item == product_id:
                return self._inventory[item]
        return None

    def get_member_from_id(self, member_id):
        """Takes the Customer ID and returns the customer with the matching ID,
        returns None if there is no match found"""
        for person in self._membership:
            if person == member_id:
                return self._membership[member_id]
        return None

    def product_search(self, search):
        """Takes on a search 'string' and returns a sorted list of id codes for the whoel inventory.
        The search is case-sensitive, and returns the list empty, if the search string is not found"""
        list_of_ids = []
        for item in self._inventory:
            title = self._inventory[item].get_title()
            description = self._inventory[item].get_descrption()
            if search.lower() in title.lower() or search.lower() in description.lower():
                list_of_ids.append(item)

    def add_product_to_member_cart(self, product_id, customer_id):
        """Takes product and customer ID. Lets you know if the product or member is not found in the
        either the inventory or membership list. Adds a product to the customers cart if both are found"""
        if product_id not in self._inventory:
            return "product ID not found"
        if customer_id not in self._membership:
            return "member ID not found"
        if self._inventory[product_id].get_quantity_available() > 0:
            self._membership[customer_id].add_product_to_cart(product_id)
            return "product added to cart"
        return "product out of stock"

    def check_out_member(self, customer_id):
        """The checkout step for the customer. Raises InvalidCheckoutError if there is an issue with membership.
        Or else it returns the charge or status of the cart at the end of the shopping scenario"""
        if customer_id not in self._membership:
            raise(InvalidCheckoutError())
        charge = 0
        member_status = self._membership[customer_id]
        for product_id in member_status.get_cart():
            product = self._inventory[product_id]
            if product.get_quantity_available() > 0:
                charge += product.get_price()
                product.decrease_quantity()
        if not member_status.is_premium_member():
            charge += 0.07 * charge
        member_status.empty_cart()
        return charge


if __name__ == '__main__':
    """the given main function that runs and gives contingencies in 
    the case that the InvalidCheckoutError is triggered"""
    p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
    c1 = Customer("Yinsheng", "QWF", False)
    myStore = Store()
    myStore.add_product(p1)
    myStore.add_member(c1)
    myStore.add_product_to_member_cart("889", "QWF")
    result = myStore.check_out_member("QWF")
    try:
        result = myStore.check_out_member("QWF")
        print("Your total is $"+str(result))
    except InvalidCheckoutError:
        print("Please review yojur Member ID")
    finally:
        print("Thank you for shopping!")
