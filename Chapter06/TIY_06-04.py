glossary = {
    'abstract base class': 'Abstract base classes complement duck-typing by providing a way to define interfaces when other techniques like hasattr() would be clumsy or subtly wrong (for example with magic methods). ABCs introduce virtual subclasses, which are classes that don’t inherit from a class but are still recognized by isinstance() and issubclass(); see the abc module documentation. Python comes with many built-in ABCs for data structures (in the collections module), numbers (in the numbers module), and streams (in the io module). You can create your own ABCs with the abc module.',
    'classic class': 'Any class which does not inherit from object. See new-style class. Classic classes have been removed in Python 3.',
    'dictionary': 'An associative array, where arbitrary keys are mapped to values. The keys can be any object with __hash__() and __eq__() methods. Called a hash in Perl.',
    'garbage collection': 'The process of freeing memory when it is not used anymore. Python performs garbage collection via reference counting and a cyclic garbage collector that is able to detect and break reference cycles.',
    'immutable': 'An object with a fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered.A new object has to be created if a different value has to be stored. They play an important role in places where a constant hash value is needed, for example as a key in a dictionary.',
    'key function': 'A key function or collation function is a callable that returns a value used for sorting or ordering. For example, locale.strxfrm() is used to produce a sort key that is aware of locale specific sort conventions.',
    'lambda': 'An anonymous inline function consisting of a single expression which is evaluated when the function is called. The syntax to create a lambda function is lambda [arguments]: expression'
}

for term, explanation in glossary.items():
    print("{0}: \n\t{1}".format(term, explanation))




