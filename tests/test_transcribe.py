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
    dna_sequence = "ATGCGTACGTTAGC"
    expected_rna_sequence = "UACGCAUGCAAUCG"  # A -> U, T -> A, C -> G, G -> C
    assert transcribe(dna_sequence) == expected_rna_sequence, f"Expected {expected_rna_sequence} but got {transcribe(dna_sequence)}"
    print("Positive test case passed.")

    # Negative Test Case
    invalid_dna_sequence = "ATGCGTACGTXYZ"  # X, Y, Z are invalid characters
    try:
        result = transcribe(invalid_dna_sequence)
        print("Negative test case failed: No error raised on invalid input.")
    except KeyError as e:
        print("Negative test case passed. Caught an error:", e)


def test_reverse_transcribe():
    # Positive Test Case
    rna_sequence = "UACGCAUGCAAUCG"
    expected_reverse_sequence = "ATGCGTACGTAGC"  # A -> T, U -> A, C -> G, G -> C
    assert reverse_transcribe(rna_sequence) == expected_reverse_sequence, f"Expected {expected_reverse_sequence} but got {reverse_transcribe(rna_sequence)}"
    print("Positive test case passed.")

    # Negative Test Case
    invalid_rna_sequence = "UACGCAUGXYZ"  # X, Y, Z are invalid characters
    try:
        result = reverse_transcribe(invalid_rna_sequence)
        print("Negative test case failed: No error raised on invalid input.")
    except KeyError as e:
        print("Negative test case passed. Caught an error:", e)

