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

    # Task 7
    def split_sequence(self, split):
        genes_length = self.bases.split(split)
        genes_sequence = []
        for i in range(len(genes_length)):
            genes_sequence.append(Sequence(genes_length[i]))
        return genes_sequence


    # Task 9
    def compare_sequence(self,given_sequence, splitter):
        """In This method getting getting a given sequence, spliting it by task 7, comparing it with another sequence by task 5 and
        then this method return values in this order:
        1.Length of mismatched genes, "mismatch_indices_in_base"          
        2.different bases for "genes_length"
        3. mutations count in each nonsimilar base "counting_base_mutation"
        4.Total number of different bases by "number_of_different_bases"
        """

        self_genome_spliter= self.split_sequence(splitter)
        given_sequence_splitted=given_sequence.split_sequence(splitter)

        #for comparison taking empty arrays
        mismatch_indices_in_base = []
        genes_length=[]
        counting_base_mutation=[]
        number_of_different_bases=0

        for i in range(len(given_sequence_splitted)):
            flag_for_matching = given_sequence_splitted[i].matching_sequence(self_genome_spliter[i].bases)
            if flag_for_matching != -1:
                mismatch_indices_in_base.append(i)
                genes_length.append(len(given_sequence_splitted[i].bases))
                counter = 0
                for j in range(len(given_sequence_splitted[i].bases)):
                    if given_sequence_splitted[i].bases[j] != self_genome_spliter[i].bases[j]:
                        counter=counter +1
                counting_base_mutation.append(counter)
            else:
                continue
        number_of_different_bases = sum(counting_base_mutation)
        return len(mismatch_indices_in_base), genes_length, counting_base_mutation, number_of_different_bases