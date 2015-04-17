# song = (
  # ('c7', 1), ('e', 4), ('g', 4),
  # ('g*', 2), ('g5', 4),
  # ('g5*', 4), ('r', 4), ('e5', 4),
  # ('e5*', 4) 
# )


POPULATION = 50
from constants import *
from misc import *
from fitness import octave_range_fitness, monotonic_notes_fitness, no_jump_fitness
import random
import pysynth_b

def gen_population(pop_size, dna_size):
    return [ gen_dna(dna_size) for _ in range (pop_size) ]

def gen_dna(dna_size):
    return [ gen_chromosone() for _ in range (dna_size) ]

def gen_chromosone():
    octave_idx = random.choice(OCTAVE_IDX)
    note_idx = random.choice(NOTE_IDX)

    # which octave * size of octave  + note in that octave
    abs_note = octave_idx * NUM_DIATONIC_REST + note_idx
    duration = DEFAULT_DURATION
    return (note_idx, octave_idx, abs_note, duration)

def run_genetic_algo():
    population = gen_population(POPULATION, BEATS_PER_SECTION)
    for dna in population:
        octave_range_ = octave_range_fitness(dna)
        monotonic_score = monotonic_notes_fitness(dna)
        no_jump_score = no_jump_fitness(dna)
        print no_jump_score
    # print population
    # return 

if __name__ == "__main__":
    dna = run_genetic_algo()
    # print dna

    # tune = dnaToPsSong(dna)
    # print tune

    # rest_lists = [ ('r',4) ]
    # tune_plus_rest = tuple(list(tune) + rest_lists)

    # pysynth_b.make_wav(tune, fn = "output.wav", leg_stac = .7, bpm = 180)
