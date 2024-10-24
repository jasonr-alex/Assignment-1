# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    dna_to_rna = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}  # N represents any unknown base
    return ''.join([dna_to_rna[base] for base in seq])

def reverse_transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA then reverses
    the strand
    """
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t