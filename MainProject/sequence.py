# This file contains a class declaration.
# I have included the initializer and an example method to help you.
# You will need to add the other methods yourself.


class Sequence:

    # This method is the initializer, it is called when creating (instantiating) an object (instance) of this class.
    def __init__(self, bases):
        # store the bases as an attribute.
        self.bases = bases
    # Task 1
    # This is an example method, it returns the first base.
    def first_base(self):
        # We can access the 'bases' for this instance via 'self'.
        result = self.bases[0]
        return result
    # Task 2
    def bases_in_DNA(self):
        counter = 0
        for base in self.bases:
            counter = counter +1
        return counter
    # Task 3
    def bool_dna(self):
        flag =True
        if len(self.bases) == 0:
            flag =False
        else:
            for i in range(len(self.bases)):
              if self.bases[i] == 'A' : flag = True
              elif self.bases[i] == 'T': flag = True
              elif self.bases[i] == 'C': flag = True
              elif self.bases[i] == 'G': flag = True 
              else:
                  flag = False
                  break
        return flag
    # Task 4
    def compliment_of_sequence(self):
        replace = ''
        for i in range(len(self.bases)):
              if self.bases[i] == 'A' :
                  replace = replace + 'T'
              elif self.bases[i] == 'T': 
                  replace = replace + 'A'
              elif self.bases[i] == 'C': 
                  replace = replace + 'G'
              elif self.bases[i] == 'G': 
                  replace = replace + 'c'
        return replace

    # Task 5
    def matching_sequence(self, second_sequence):
        assert len(self.bases) == len(second_sequence), 'Sequence are not having same length' 
        
        if len(self.bases) == 0:
            return -1
        else:
            counter = -1
            for i in range(len(self.bases)):
                if self.bases[i] == second_sequence[i]:
                    counter =counter + 1
                    if (len(self.bases)-1)== counter:
                        return -1
                else:
                    return counter + 1
