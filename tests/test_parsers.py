# write tests for parsers
import pytest
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
    # Initialize FastaParser with the test file
    parser = FastaParser("data/test.fa")
 
    # List to store the parsed records (I'm turning the generator into a list here)
    parsed_records = list(parser)

    print(parsed_records)

    # A couple snippets from the test file I manually wrote to test here!
    expected_output = [
        ('seq0', 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'),
        ('seq1', 'TCCGCCCGCTGTGCTGACGAGACTAGCAGGGAAATAAATAGAGGGTTTAGTTATACTCAGTAGGCAGTTCGATGGCTTATATCTAACTTCTTATTCCGAT')
    ]

    assert parsed_records[0] == expected_output[0]
    assert parsed_records[1] == expected_output[1]

def test_FastqParser():
    # Initialize FastqParser with the test file
    parser = FastqParser("data/test.fq")
    
    # List to store the parsed records
    parsed_records = list(parser)
    
    expected_output = [
        ('seq0', 
         'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG',
         '*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8(58&59>\'8!;28<94,0*;*.94**:9+7"94(>7=\'(!5"2/!%"4#32='),
        ('seq1',
         'CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCCATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG',
         '\'(<#/0$5&!$+,:=%7=50--1;\'(-7;0>=$(05*9,,:%0!<),%646<8#%"."-\'*-0:.+*&$5!\'8)(%3*+9/&/%=363*,6$20($97,"'),
        ('seq2',
         'GATAAACTTCTATCACGAATACTGCGGGACCATGCAGTTGTCCCTCACCTCGATAGTTCAGGTCTTTTGGTTCTGAGCGATATTGGGCGCGTCACCACTG',
         '1,758$,:7654/7<0%5/12%-3>-2.>$$443-,\'9,5$;\""%7**)-\'%:**&;<35(!<1\'.5>51)1%:9>4=(&+3$2!-.8!>=+1$:,*&9!')
    ]
    
    assert parsed_records[0] == expected_output[0]
    assert parsed_records[1] == expected_output[1]
    assert parsed_records[2] == expected_output[2]


def test_FastaParser_negative():
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        parser = FastaParser("nonexistent.fa")
        list(parser) # this apparently calls the generator
        
    # Test invalid file format
    with pytest.raises(ValueError):
        parser = FastaParser("data/invalid.fa")  # File without any '>' headers
        list(parser)

def test_FastqParser_negative():
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        parser = FastqParser("nonexistent.fq")
        list(parser)
        
    # Test mismatched sequence/quality lengths
    with pytest.raises(ValueError):
        parser = FastqParser("data/invalid.fq")  # File with mismatched lengths
        list(parser)
        
    # Test missing quality scores
    with pytest.raises(ValueError):
        parser = FastqParser("data/missing_quality.fq")  # File missing quality scores
        list(parser)