# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    dna_to_rna = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}  # N represents any unknown base; establsihes the dictionary for RNA transcript
    return ''.join([dna_to_rna[base] for base in seq]) # This outputs the RNA transcript by joining each complementary base for each base in the DNA sequence

def reverse_transcribe(seq: str) -> str:
    dna_to_rna = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}  # N represents any unknown base
    rna_sequence =  ''.join([dna_to_rna[base] for base in seq]) # Instead of returning the RNA strand, store it in a vairable
    return rna_sequence[::-1] # Use the stored variable in rna_sequence to then return the RNA transcript in reverse, starting from the -1 position of the RNA sequence