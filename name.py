from traceback import print_last


# So, what are n, address and employee? They are names.
# Names that we can use to retrieve data within our code.
# They need to be kept somewhere so that whenever we need to retrieve those objects,
#  we can use their names to fetch them.
#
# We need some space to hold them, hence: namespaces!

n = 3  # integer number
address = "221b Baker Street, NW1 6XE, London"  # S. Holmes
# a Dictionnary
employee = {
    'age': 45,
    'role': 'CTO',
    'SSN': 'AB1234567',
}

print(n)
print(address)
print(employee)


 # what if I try to print a name I didn't define?
# print(other_name)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'other_name' is not defined

# We de ned three objects in the preceding code (do you remember what are the three features every Python object has?):
# • An integer number n (type: int, value: 3)
# • A string address (type: str, value: Sherlock Holmes' address)
# • A dictionary employee (type: dict, value: a dictionary which holds three key/value pairs)