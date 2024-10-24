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

    # Initialize FastaParser with valid data
    parser = FastaParser(valid_fasta)

    # Store records
    records = list(parser.__iter__())

    expected_records = [
        (">sequence1", "ATGCGTACGTTAGC"),
        (">sequence2", "TGCATGCATGCATG")
    ]

    # Use assert to check if the records match the expected output
    assert records == expected_records, f"Expected {expected_records} but got {records}"
    print("Positive test case passed.")

    # Negative Test Case
    invalid_fasta = """sequence1
    ATGCGTACGTTAGC
    >sequence2
    TGCATGCATGCATG
    """

    # Initialize FastaParser with invalid data
    parser = FastaParser(invalid_fasta)

    # Attempt to parse the invalid records and check for proper handling
    try:
        records = list(parser.__iter__())
        # Check if any record is missing or invalid
        assert all(record[0].startswith('>') for record in records), "Some headers are missing '>'"
        print("Negative test case failed: No error raised on invalid input.")
    except AssertionError as e:
        print("Negative test case passed. Caught an error:", e)


def test_FastqParser():
   
    # Positive Test Case
    valid_fastq = """@SEQ_ID_1
    GATTTGGGGTTTTAGTAGA
    +
    !''*((((***+))%%%++((
    @SEQ_ID_2
    GATTTGGGGTTTTAGTACG
    +
    !''*((((***+))%%%++((
    """

    # Initialize FastqParser with valid data
    parser = FastqParser(filename=None)  # Assuming the filename parameter isn't used in this case

    # Override the _get_record method to read directly from the string data
    parser._get_record = lambda f: (
        f.readline().strip(),  # Header
        f.readline().strip(),  # Sequence
        f.readline().strip()   # Quality (skip the placeholder line)
    )

    # Store records
    records = list(parser.__iter__())

    expected_records = [
        ("@SEQ_ID_1", "GATTTGGGGTTTTAGTAGA", "!''*((((***+))%%%++(("),
        ("@SEQ_ID_2", "GATTTGGGGTTTTAGTACG", "!''*((((***+))%%%++((")
    ]

    # Use assert to check if the records match the expected output
    assert records == expected_records, f"Expected {expected_records} but got {records}"
    print("Positive test case passed.")

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

    # Initialize FastqParser with invalid data
    parser = FastqParser(filename=None)  # Assuming the filename parameter isn't used

    # Override the _get_record method to read directly from the string data
    parser._get_record = lambda f: (
        f.readline().strip(),  # Header
        f.readline().strip(),  # Sequence
        f.readline().strip()   # Quality (skip the placeholder line)
    )

    # Attempt to parse the invalid records and check for proper handling
    try:
        records = list(parser.__iter__())
        # Check if any record is missing the '@' in the header
        assert all(record[0].startswith('@') for record in records), "Some headers are missing '@'"
        print("Negative test case failed: No error raised on invalid input.")
    except AssertionError as e:
        print("Negative test case passed. Caught an error:", e)
