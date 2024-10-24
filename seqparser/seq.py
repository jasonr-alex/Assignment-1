# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    dna_to_rna = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}  # N represents any unknown base
    return ''.join([dna_to_rna[base] for base in seq])

def reverse_transcribe(seq: str) -> str:
    dna_to_rna = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}  # N represents any unknown base
    rna_sequence =  ''.join([dna_to_rna[base] for base in seq])
    return rna_sequence[::-1]