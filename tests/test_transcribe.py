# write tests for transcribes
import pytest
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
    assert transcribe("ACTGAACCC") == "UGACUUGGG", "Basic transcription failed"
    assert transcribe("GCAT") == "CGUA", "Simple sequence transcription failed"
    
    # Test sequences with repeated nucleotides
    assert transcribe("AAAA") == "UUUU", "A transcription failed"
    assert transcribe("TTTT") == "AAAA", "T transcription failed"
    assert transcribe("GCGC") == "CGCG", "GC transcription failed"
    
    # Test empty sequence
    assert transcribe("") == "", "Empty sequence should return empty string"
    
    # Test case insensitivity
    assert transcribe("actg") == "UGAC", "Lower case input failed"
    assert transcribe("AcTg") == "UGAC", "Mixed input failed"


def test_reverse_transcribe():
    # Test basic reverse transcription cases
    assert reverse_transcribe("ACTGAACCC") == "GGGUUCAGU", "Basic reverse transcription failed"
    assert reverse_transcribe("GCAT") == "AUGC", "Simple sequence reverse transcription failed"
    
    # Test sequences with repeated nucleotides
    assert reverse_transcribe("AAAA") == "UUUU", "A reverse transcription failed"
    assert reverse_transcribe("TTTT") == "AAAA", "T reverse transcription failed"
    
    # Test empty sequence
    assert reverse_transcribe("") == "", "Empty sequence should return empty string"
    
    # Test case insensitivity
    assert reverse_transcribe("actg") == "CAGU", "Lower case input failed"
    assert reverse_transcribe("AcTg") == "CAGU", "Mixed input failed"

def test_transcribe_negative():
    with pytest.raises(ValueError):
        transcribe("AXCT")  # X is not a valid nucleotide
    
    with pytest.raises(ValueError):
        transcribe("AC T")  # Space is not valid
        
    with pytest.raises(ValueError):
        transcribe("AC-T")  # Dash is not valid
        
    with pytest.raises(ValueError):
        transcribe("AC1T")  # Numbers are not valid

def test_reverse_transcribe_negative():
    """
    Negative test cases for reverse_transcribe function.
    Tests error handling and invalid inputs.
    """
    # Test invalid nucleotides
    with pytest.raises(ValueError):
        reverse_transcribe("AXCT")
        
    # Test invalid characters
    with pytest.raises(ValueError):
        reverse_transcribe("AC T")