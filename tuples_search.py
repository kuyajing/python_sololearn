'''
You are given a list of contacts, where each contact is represented by a tuple, with the name and age of the contact.
Complete the program to get a string as input, search for the name in the list of contacts and output the age of the contact in the format presented below:

Sample Input
John

Sample Output
John is 31

contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

'''


def search_contact(contacts, name):
    # Search for the name in the list of contacts
    for contact in contacts:
        if contact[0] == name:
            # Output the age of the contact in the format presented below
            return f"{name} is {contact[1]}"
    # Return this message if the name is not found in the contacts list
    return f"Not Found"

# Sample list of contactsamt
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

# Get a string as input
name = input()

# Output the result
print(search_contact(contacts, name))