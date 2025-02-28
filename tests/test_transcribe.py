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
    """
    Write your unit test for the
    transcribe function here.
    """
    seq = 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
    seq_t = 'ACUAACUUAGAAAACUCCCAGUGCCGGGCCUUCGGUCUUAAAGCCCCAGGAGACACCUAUAAUUAGCUCGGGUGUGCCACACUCAAGUCGCCGGGGGCGU'
    assert transcribe(seq) == seq_t


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    seq = 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
    seq_rev_t = 'UGCGGGGGCCGCUGAACUCACACCGUGUGGGCUCGAUUAAUAUCCACAGAGGACCCCGAAAUUCUGGCUUCCGGGCCGUGACCCUCAAAAGAUUCAAUCA'
    assert reverse_transcribe(seq) == seq_rev_t

