# This file contains a class declaration.
# I have included the initializer and an example method to help you.
# You will need to add the other methods yourself.


class Sequence:

    # This method is the initializer, it is called when creating (instantiating) an object (instance) of this class.
    def __init__(self, bases):
        # store the bases as an attribute.
        self.bases = bases

    # This is an example method, it returns the first base.
    def first_base(self):
        # We can access the 'bases' for this instance via 'self'.
        result = self.bases[0]
        return result

    # TODO: add other methods here to complete the tasks.
