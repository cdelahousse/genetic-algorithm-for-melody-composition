from constants import *

def absToOctaveIdx(abs_note):
    assert isinstance(abs_note, ( int, long ) )
    octave_idx = abs_note // NUM_DIATONIC_REST
    assert 0 <= octave_idx < NUM_OCTAVES
    return octave_idx

def absToLetterIdx(abs_note):
    assert isinstance(abs_note, ( int, long ) )
    octave_idx = absToOctaveIdx(abs_note)
    letter_idx = abs_note - (octave_idx * NUM_DIATONIC_REST)
    assert 0 <= letter_idx < NUM_DIATONIC_REST
    return letter_idx

def absToLetter(abs_note):
    return DIATONIC_REST[absToLetterIdx(abs_note)]

def getOctaveIdx(chromosone):
    return chromosone[1]

def getLetterIdx(chromosone):
    return chromosone[0]

def getAbsNote(chromosone):
    return chromosone[2]

def getDuration(chromosone):
    return chromosone[3]

def chromosoneToPsNote(chromosone):
    letter_idx = getLetterIdx(chromosone)
    octave_idx = getOctaveIdx(chromosone)
    letter = DIATONIC_REST[letter_idx]
    octave = OCTAVES[octave_idx]
    if letter in REST:
        octave = ''
    lo = str(letter) + str(octave)
    dur = getDuration(chromosone)
    return (lo, dur)

def dnaToPsSong(dna):
    song_list = [ chromosoneToPsNote(chromosone) for chromosone in dna ]
    return tuple(song_list)


