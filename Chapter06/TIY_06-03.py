glossary = {
    'abstract base class': 'Abstract base classes complement duck-typing by providing a way to define interfaces when other techniques like hasattr() would be clumsy or subtly wrong (for example with magic methods). ABCs introduce virtual subclasses, which are classes that don’t inherit from a class but are still recognized by isinstance() and issubclass(); see the abc module documentation. Python comes with many built-in ABCs for data structures (in the collections module), numbers (in the numbers module), and streams (in the io module). You can create your own ABCs with the abc module.',
    'classic class': 'Any class which does not inherit from object. See new-style class. Classic classes have been removed in Python 3.',
    'dictionary': 'An associative array, where arbitrary keys are mapped to values. The keys can be any object with __hash__() and __eq__() methods. Called a hash in Perl.',
 }

for term, explanation in glossary.items():
    print("{0}: \n\t{1}".format(term, explanation))




