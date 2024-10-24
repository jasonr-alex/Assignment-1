# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    # Positive Test Case
    dna_sequence = "ATGCGTACGTTAGC"  # Define a valid DNA sequence.
    expected_rna_sequence = "UACGCAUGCAAUCG"  # Expected RNA sequence after transcription (A -> U, T -> A, C -> G, G -> C).
    
    # Use assert to check if the transcription result matches the expected RNA sequence
    assert transcribe(dna_sequence) == expected_rna_sequence, f"Expected {expected_rna_sequence} but got {transcribe(dna_sequence)}"
    # If the assertion fails, raise an AssertionError with a message indicating the expected and actual outputs.

    print("Positive test case passed.")  # Print confirmation of passing the positive test case.

    # Negative Test Case
    invalid_dna_sequence = "ATGCGTACGTXYZ"  # Define an invalid DNA sequence containing invalid characters X, Y, Z.
    
    try:
        result = transcribe(invalid_dna_sequence)  # Attempt to transcribe the invalid DNA sequence.
        print("Negative test case failed: No error raised on invalid input.")  # Print message if no error was raised.
    except KeyError as e:
        print("Negative test case passed. Caught an error:", e)  # Print the error message indicating the negative test case passed.


def test_reverse_transcribe():
    # Positive Test Case
    rna_sequence = "UACGCAUGCAAUCG"  # Define a valid RNA sequence.
    expected_reverse_sequence = "ATGCGTACGTAGC"  # Expected DNA sequence after reverse transcription (A -> T, U -> A, C -> G, G -> C).
    
    # Use assert to check if the reverse transcription result matches the expected DNA sequence
    assert reverse_transcribe(rna_sequence) == expected_reverse_sequence, f"Expected {expected_reverse_sequence} but got {reverse_transcribe(rna_sequence)}"
    # If the assertion fails, raise an AssertionError with a message indicating the expected and actual outputs.

    print("Positive test case passed.")  # Print confirmation of passing the positive test case.

    # Negative Test Case
    invalid_rna_sequence = "UACGCAUGXYZ"  # Define an invalid RNA sequence containing invalid characters X, Y, Z.
    
    try:
        result = reverse_transcribe(invalid_rna_sequence)  # Attempt to reverse transcribe the invalid RNA sequence.
        print("Negative test case failed: No error raised on invalid input.")  # Print message if no error was raised.
    except KeyError as e:
        print("Negative test case passed. Caught an error:", e)  # Print the error message indicating the negative test case passed.


