from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    # Create instance of FastaParser
    fasta_parser = FastaParser('data/test.fa')  # Ensure 'data/test.fa' is a valid file path.
    
    # Create instance of FastqParser
    fastq_parser = FastqParser('data/test.fastq')  # Ensure 'data/test.fastq' is a valid file path.

    # For each record of FastaParser, Transcribe the sequence and print it to console
    print("Transcribed Fasta Records:")
    for header, sequence in fasta_parser:
        rna_sequence = transcribe(sequence)  # Transcribe the sequence
        print(f"{header}: {rna_sequence}")  # Print header and corresponding RNA sequence

    # For each record of FastqParser, Transcribe the sequence and print it to console
    print("\nTranscribed Fastq Records:")
    for header, sequence, quality in fastq_parser:
        rna_sequence = transcribe(sequence)  # Transcribe the sequence
        print(f"{header}: {rna_sequence}")  # Print header and corresponding RNA sequence

    # For each record of FastaParser, Reverse Transcribe the sequence and print it to console
    print("\nReverse Transcribed Fasta Records:")
    for header, sequence in fasta_parser:
        reverse_rna_sequence = reverse_transcribe(transcribe(sequence))  # Reverse Transcribe the RNA
        print(f"{header}: {reverse_rna_sequence}")  # Print header and corresponding reversed RNA sequence

    # For each record of FastqParser, Reverse Transcribe the sequence and print it to console
    print("\nReverse Transcribed Fastq Records:")
    for header, sequence, quality in fastq_parser:
        reverse_rna_sequence = reverse_transcribe(transcribe(sequence))  # Reverse Transcribe the RNA
        print(f"{header}: {reverse_rna_sequence}")  # Print header and corresponding reversed RNA sequence


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
