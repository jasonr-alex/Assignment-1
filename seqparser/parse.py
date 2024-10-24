import io
from typing import Tuple, Union


class Parser:
    """
    Base Class for Parsing Algorithms
    """
    def __init__(self, filename: str):
        """
        Initialization to be shared by all inherited classes.
        
        # Recall that this is where we store baseline attribute of a class. For example:
            class Cat: 
                def __init__(self, weight: float, breed: str, food: str):
                    self.weight = weight
                    self.breed = breed
                    self.food = food
                    
        # What attributes are we initializing here in Parser? 
        """
        
        self.filename = filename

    def get_record(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        Returns a sequencing record that will either be a tuple of two strings (header, sequence)
        or a tuple of three strings (header, sequence, quality). 

        """
        return self._get_record(f_obj)

    def __iter__(self):
        """
        This is an overriding of the Base Class Iterable function. Here, for the purposes of this
        assignment, we are defining how this class and all inherited classes interact with loops.

        # Usage

        ```
        parser_obj = Parser(filename)
        for record in parser_obj:
            # do something
        ```

        The code above calls `__iter__` and for every record it returns, does something with it.

        You may notice we use the keyword `yield` instead of `return` for this function. This is
        because our `__iter__` is what is known as a generator function, which generates an
        output then waits until it is called again to resume. In our case, it just reads in a
        record, outputs it, then waits to read the next record.

        In comparison, functions with `return` simply restart when they are called again, so we
        would just be reading from the beginning of the file.

        Generator functions are very useful for many bioinformatic tools where you don't need 
        everything loaded at once and instead are interested in interacting with the stream 
        (i.e. you need every value once and won't need it again after you use it). This saves
        quite a bit of memory, especially when you are working with billions of sequences and don't 
        need to keep all of them in memory. 
        
        """
        with open(self.filename, "r") as f_obj:
            while True:
                try:
                    rec = self.get_record(f_obj)
                    if rec is None:
                        break
                    yield rec
                except StopIteration:
                    break 

    def _get_record(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        a method to be overridden by inherited classes.
        """
        raise NotImplementedError(
                """
                This function is not meant to be called by the Parser Class.
                It is expected to be overridden by `FastaParser` and `FastqParser`
                """)


class FastaParser(Parser):
    """
    Fasta Specific Parsing.
    """
    def _get_record(self, f_obj: io.TextIOWrapper) -> Tuple[str, str]:
        """
        TODO: returns the next fasta record as a 2-tuple of (header, sequence)
        """
        header = None # Initialize the header variable to None
        sequence_lines = [] # List to accumulate sequence lines
        
        for line in f_obj: # Iterate over each line in the file object
            line = line.strip() # Remove leading/trailing whitespace from the line
            if line.startswith('>'): # Check if the line is a header (starts with '>')
                if header: # If there's an existing header, return the previous record
                    return (header, ''.join(sequence_lines)) # Return the tuple of header and joined sequence
                header = line[1:]  # Remove '>' from header
                sequence_lines = [] # Reset sequence lines for the new record
            else:
                sequence_lines.append(line) # Append the line to the sequence list
        
        if header: # Check if there was a header for the last record in the file
            return (header, ''.join(sequence_lines)) # Return the last record as a tuple
        
        return None # Return None if no record was found

class FastqParser(Parser):
    """
    Fastq Specific Parsing 
    """
    def _get_record(self, f_obj: io.TextIOWrapper) -> Tuple[str, str, str]: # Read the header line and remove whitespace
       header = f_obj.readline().strip() # Read the header line and remove whitespace
       if not header: # Check if the header is empty (end of file)
        return None  # Return None if we've reached the end of the file
       sequence = f_obj.readline().strip() # Read the sequence line and remove whitespace
       f_obj.readline() # Skip the '+' line, which is a placeholder in FASTQ format
       quality = f_obj.readline().strip() # Read the quality line and remove whitespace

       if header.startswith('@'): # Check if the header starts with '@', indicating a valid FASTQ format
        return (header[1:], sequence, quality) # Return a tuple of header (without '@'), sequence, and quality
       else:
        raise ValueError("Invalid FASTQ format: Missing '@' in header") # Raise an error if the format is invalid
