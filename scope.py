# A Scope :a textual region of a Python program,
# where a namespace is directly accessible.
# Directly accessible means that when you're looking for an unqualifed reference to a name,
# Python tries to find it in the namespace.

# There are four different scopes that Python makes accessible (not necessarily all of them present at the same time, of course):
# • The local scope, which is the innermost one and contains the local names.
# • The enclosing scope, that is, the scope of any enclosing function. It contains
# non-local names and also non-global names.
# • The global scope contains the global names.
# • The built-in scope contains the built-in names. Python comes with a set of functions that you can use in a off-the-shelf fashion, such as print, all, abs, and so on. They live in the built-in scope.



# --> The rule is the following: when we refer to a name, Python starts looking for it in the current namespace. If the name is not found, Python continues the search to
# the enclosing scope and this continue until the built-in scope is searched.
# If a name hasn't been found after searching the built-in scope, then Python raises a NameError exception !!!!!!



# scopes1.py  @function name
# Local versus Global

def local():  # we define a function, called local
    m = 7
    print(m)


m = 5        # we define a Global, called local
print(m)
local() # we call, or `execute` the function local



# python scopes1.py   @for calling function


# As expected, Python prints m the  rst time, then when the function local is called,
# m isn't found in its scope, so Python looks for it following the LEGB chain until m is found in the global scope.



# scopes3.py
# Local, Enclosing and Global
def enclosing_func():
    m = 13
    def localy():
           # m doesn't belong to the scope defined by the local
           # function so Python will keep looking into the next
           # enclosing scope. This time m is found in the enclosing
           # scope
       print(m,'printing from the local scope')
       # calling the function local
    localy()
m= 5
print(m, 'printing from the global scope')
enclosing_func()



