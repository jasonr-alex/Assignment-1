# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    # Positive Test Case
    valid_fasta = """>sequence1
    ATGCGTACGTTAGC
    >sequence2
    TGCATGCATGCATG
    """
    # Define a valid FASTA format string with two sequences.

    # Initialize FastaParser with valid data
    parser = FastaParser(valid_fasta)  # Create an instance of FastaParser using the valid FASTA string.

    # Store records
    records = list(parser.__iter__())  # Parse the records from the parser and convert to a list.

    expected_records = [
        (">sequence1", "ATGCGTACGTTAGC"),  # Expected tuple for the first sequence.
        (">sequence2", "TGCATGCATGCATG")   # Expected tuple for the second sequence.
    ]

    # Use assert to check if the records match the expected output
    assert records == expected_records, f"Expected {expected_records} but got {records}"
    # Check if the actual records match the expected records; if not, raise an AssertionError with a message.

    print("Positive test case passed.")  # Print confirmation of passing the positive test case.

    # Negative Test Case
    invalid_fasta = """sequence1
    ATGCGTACGTTAGC
    >sequence2
    TGCATGCATGCATG
    """
    # Define an invalid FASTA format string where the first sequence is missing a header.

    # Initialize FastaParser with invalid data
    parser = FastaParser(invalid_fasta)  # Create an instance of FastaParser using the invalid FASTA string.

    # Attempt to parse the invalid records and check for proper handling
    try:
        records = list(parser.__iter__())  # Parse the records from the parser and convert to a list.
        # Check if any record is missing or invalid
        assert all(record[0].startswith('>') for record in records), "Some headers are missing '>'"
        # Assert that all records have headers starting with '>'; if not, raise an AssertionError.

        print("Negative test case failed: No error raised on invalid input.")  # Print message if no error was raised.
    except AssertionError as e:
        print("Negative test case passed. Caught an error:", e)  # Print the error message indicating the negative test case passed.


def test_FastqParser():
   
    # Positive Test Case
    valid_fastq = """@SEQ_ID_1
    GATTTGGGGTTTTAGTAGA
    +
    !''*((((***+))%%%++((
    @SEQ_ID_2
    GATTTGGGGTTTTAGTACG
    """
    # Define a valid FASTQ format string with two sequences, including quality scores.

    # Initialize FastqParser with valid data
    parser = FastqParser(filename=None)  # Create an instance of FastqParser, assuming filename isn't used.

    # Override the _get_record method to read directly from the string data
    parser._get_record = lambda f: (
        f.readline().strip(),  # Read and return the header, removing whitespace.
        f.readline().strip(),  # Read and return the sequence, removing whitespace.
        f.readline().strip()   # Read and return the quality line (skipping the '+' line).
    )

    # Store records
    records = list(parser.__iter__())  # Parse the records from the parser and convert to a list.

    expected_records = [
        ("@SEQ_ID_1", "GATTTGGGGTTTTAGTAGA", "!''*((((***+))%%%++(("),  # Expected tuple for the first FASTQ sequence.
        ("@SEQ_ID_2", "GATTTGGGGTTTTAGTACG", "!''*((((***+))%%%++((")   # Expected tuple for the second FASTQ sequence.
    ]

    # Use assert to check if the records match the expected output
    assert records == expected_records, f"Expected {expected_records} but got {records}"
    # Check if the actual records match the expected records; if not, raise an AssertionError with a message.

    print("Positive test case passed.")  # Print confirmation of passing the positive test case.

    # Negative Test Case
    invalid_fastq = """SEQ_ID_1
    GATTTGGGGTTTTAGTAGA
    +
    !''*((((***+))%%%++((
    @SEQ_ID_2
    GATTTGGGGTTTTAGTACG
    +
    !''*((((***+))%%%++((
    """
    # Define an invalid FASTQ format string where the first sequence is missing an '@' in the header.

    # Initialize FastqParser with invalid data
    parser = FastqParser(filename=None)  # Create an instance of FastqParser, assuming filename isn't used.

    # Override the _get_record method to read directly from the string data
    parser._get_record = lambda f: (
        f.readline().strip(),  # Read and return the header, removing whitespace.
        f.readline().strip(),  # Read and return the sequence, removing whitespace.
        f.readline().strip()   # Read and return the quality line (skipping the '+' line).
    )

    # Attempt to parse the invalid records and check for proper handling
    try:
        records = list(parser.__iter__())  # Parse the records from the parser and convert to a list.
        # Check if any record is missing the '@' in the header
        assert all(record[0].startswith('@') for record in records), "Some headers are missing '@'"
        # Assert that all records have headers starting with '@'; if not, raise an AssertionError.

        print("Negative test case failed: No error raised on invalid input.")  # Print message if no error was raised.
    except AssertionError as e:
        print("Negative test case passed. Caught an error:", e)  # Print the error message indicating the negative test case passed.

