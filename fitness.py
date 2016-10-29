from misc import *
import collections

def octave_range_fitness(dna):
    octave_idx_per_note = [
        getOctaveIdx(chromosone) for chromosone in dna]

    counter = collections.Counter(octave_idx_per_note)
    #WHAT HAPPENS IF TOP TWO HAVE SAME NUMBER XXX
    common = counter.most_common(4)

    best_octave_score = common[0][1]
    # second_best_octave = common[1][1] #Number in best octave
    # second_best_octave_score = second_best_octave * 0.5

    #NUmber of notes in the best octave is score
    #Max possible score if all notes are in one octave
    return best_octave_score


#Are most notes monotonic?
def monotonic_notes_fitness(dna):
    def areMonotonic(abs_notes, start_idx, window_size):
        l = abs_notes[start_idx:start_idx+window_size]

        #Ignoring rests XXX
        is_inc = all(x<=y for x, y in zip(l, l[1:]))
        is_dec = all(x>=y for x, y in zip(l, l[1:]))

        return is_inc or is_dec

    WINDOW = 3

    #Add to make max score len(dna)
    score = WINDOW - 1
    max_iteration = len(dna) - WINDOW + 1
    abs_notes = [ getAbsNote(chromosone) for chromosone in dna]
    for i in range(max_iteration):
        if areMonotonic(dna, i, WINDOW):
          score += 1

    #MAX score is len(dna)
    return score

def no_jump_fitness(dna):
    def isJump(abs_notes, start_idx):
        MAX_JUMP = 4
        #Ignoring rests XXX
        f_note = abs_notes[start_idx]
        n_note = abs_notes[start_idx + 1]
        return abs(f_note - n_note) > MAX_JUMP


    #Add to make max score len(dna)
    score = 1
    max_iteration = len(dna) - 1
    abs_notes = [ getAbsNote(chromosone) for chromosone in dna]
    for i in range(max_iteration):
        if not isJump(abs_notes, i):
          score += 1

    return score

def isSignificantNote(chromosone):
    letter = getLetter(chromosone)
    return letter in CHORD_NOTES

#Is Down beat a significant note?
def down_beat_fitness(dna):
    score = 0
    for i in range(0, BEATS_PER_SECTION, BEATS_PER_BAR):
        chromosone = dna[i]
        if isSignificantNote(chromosone):
          score += BEATS_PER_BAR

    return score

#Is back beat a significant note?
def back_beat_fitness(dna):
    score = 0
    for i in range(1, BEATS_PER_SECTION, BEATS_PER_BAR/2):
        chromosone = dna[i]
        if isSignificantNote(chromosone):
          score += BEATS_PER_BAR

    return score
