# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    complement_map = {
        'A': 'U',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    
    # this part is to make sure we don't make mistakes if the sequence is written in lowercase
    seq = seq.upper()
    
    invalid_bases = set(seq) - set(complement_map.keys())
    if invalid_bases:
        raise ValueError(f"Invalid nucleotides found in sequence: {invalid_bases}")
    
    return ''.join(complement_map[base] for base in seq)

def reverse_transcribe(seq: str) -> str:
    # First, we transcribe
    rna_seq = transcribe(seq)
    # then we use this to reverse the sequence (thanks stackoverflow!)
    return rna_seq[::-1]
