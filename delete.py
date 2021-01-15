class Phone:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.contacts = []

    def add_contact(self, name, number):
        if self.contacts and self.is_duplicate(number):
            if self.duplicate():
                self.contacts.append({"Name": name, "Number": str(number)})
            else:
                print("The contact has *not* been added.")
        else:
            self.contacts.append({"Name": name, "Number": str(number)})

    def is_duplicate(self, number):
        for contact in self.contacts:
            if contact["Number"] == str(number):
                return True
        return False

    def duplicate(self):
        print("This *number* is already in your contacts.")
        answer = input("Do you want to add contact?: y/N \n")
        return answer.lower() == "y"

    def remove_contact(self, credential):
        indexed_contacts = self.get_indexed_contacts(credential)
        if len(indexed_contacts) > 1:
            index = self.get_index_choice(indexed_contacts)
            del self.contacts[index]
        elif len(indexed_contacts) == 1:
            index = list(indexed_contacts.keys())[0]
            del self.contacts[index]
            print(f"The contact '{credential}' has been deleted.")
        else:
            print(f"The contact '{credential}' has *not* been found.")

    def lookup_contact(self, credential):
        indexed_contacts = self.get_indexed_contacts(credential)
        if not indexed_contacts:
            print(f"The contact '{credential}' has *not* been found.")
            return False
        elif len(indexed_contacts) > 1:
            index = self.get_index_choice(indexed_contacts)
            return self.contacts[index]
        else:
            index = list(indexed_contacts.keys())[0]
            return self.contacts[index]

    def get_index_choice(self, indexed_contacts):
        print("There's more than 1 contact:")
        for index, contact in indexed_contacts.items():
            print(f"{index}: {contact}")
        index = input("Choose the contact you want to *pick* by its index: ")
        return int(index)

    def get_indexed_contacts(self, str_credentials):
        """
        :param str_credentials: String, number, or combination of these.
        :return: Dictionary with:
                - the location in the contacts list (index) for keys
                - the contacts for values
        """
        str_credentials = str(str_credentials)

        indexed_contacts = {}
        for index, contact in enumerate(self.contacts):
            is_name = str_credentials.isalnum() and str_credentials in contact["Name"]
            is_number = str_credentials.isnumeric() and str_credentials in contact["Number"]
            if is_name or is_number:
                indexed_contacts[index] = contact

        return indexed_contacts
