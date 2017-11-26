# A namespace is therefore a mapping from names to objects.

# Examples are the set of built-in names
# (containing functions that are always accessible for free in any Python program),
# the global names in a module,  and the local names in a function.
# --> Even the set of attributes of an object can be considered a namespace.

# --> they allow you to de ne and organize your names with clarity
# --> from library.second_floor.section_x.row_three import book


# # namespaces are places where names are associated to objects.
#
#  There are four different scopes that Python makes accessible (not necessarily all of them present at the same time, of course):
# • The local scope, which is the innermost one and contains the local names.
# • The enclosing scope, that is, the scope of any enclosing function. It contains
# non-local names and also non-global names.
# • The global scope contains the global names.
# • The built-in scope contains the built-in names. Python comes with a set of functions that you can use in a off-the-shelf fashion, such as print, all, abs, and so on. They live in the built-in scope.


# The rule is the following: when we refer to a name, Python starts looking for it in the current namespace. If the name is not found, Python continues the search to
# the enclosing scope and this continue until the built-in scope is searched. If a name hasn't been found after searching the built-in scope, then Python raises a NameError exception
#




