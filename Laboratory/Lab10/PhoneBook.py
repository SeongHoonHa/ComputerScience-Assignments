from Contact import Contact

class PhoneBook:

    def __init__(self):
        """
        The phonebook keeps track of all contacts. This class is an example of 
        interacting with other classes a coder will make.

        count
        contactList 

        Instance variables provided for this constructor.
        """
        self.contactList = []
        self.count = 0

    
    def addContact(self, c):
        """
        Given a contact, determine if you are given a dictionary or an instance of 
        a Contact class. Handle the adding to our phone book appropriately and update the counter.

        If you are given a dictionary, assume that a dictionary has the following keys 
        (and the values are in the correct format):
        - name
        - number
        - email
        - birthday

        NOTE: Why do we have to manually update the counter?
        """
        if isinstance(c, Contact):
            self.contactList.append(c) # self.contactList += [c]
            self.count += 1

        elif isinstance(c, dict):
            # Getting the information from the dict
            name = c["name"]
            num = c["number"]
            email = c["email"]
            b = c["birthday"]

            # Create a new contact
            newContact = Contact(name, num, email, b)

            # adding to the list and updating the count
            self.contactList.append(newContact)
            self.count += 1


    
    def getContactCount(self):
        """
        Returns the number of contacts stored in the 
        """
        return self.count
    
    def findContact(self, lName):
        """
        Given a last name, find the contact(s) and return the contact information. 

        Will be a list. 
        """
        contacts_with_same_lname = []

        # loop through all of my contact
        for contact in self.contactList:

            # if that contact has lName as last
            if contact.last == lName:

                # Append
                contacts_with_same_lname.append(contact)

        return contacts_with_same_lname



    def groupChat(self, message):
        """
        Send a message to every contact in the phonebook
        """
        for contact in self.contactList:
            contact.sendText(message)

    def __str__(self):
        """
        Returns a string representation of the phonebook class. 

        The output will be
        > Phone Book: #

        Where # is the number of contacts in the phonebook. 
        """
        return "Phone Book: " + str(self.count)
