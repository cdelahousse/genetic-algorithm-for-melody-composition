# Genetic Algorithm for Melody Composition

I decided to explore a genetic algorithm to compose simple pleasurable melodies.
Music composition is one the oldest human artistic pursuits. People spend years
developing the talent and we prize the ones who do it best. Let us see if we can
crack the secret of beautiful melodies in a few hundred lines of code?

To simplify the problem, I opted to restrict the choice of notes to the C major
scale. That means all the white keys on a piano. At a minimum, this will give me
music a tonic feel and thankfully removes the resulting melody from the realm of
twelve tone serial music. This key and scale is used for an nauseating amount
of music: from Ravel's Bolero to The Beatles' All You Need Is Love to the set of
tunes interpreted by every 8 year old budding piano player.

The project is implemented in Python 2.7 using PySynth
(https://github.com/mdoege/PySynth), a simple music
synthesizer. Any rendered genome gets converted into a variation of DOT notation
that's compatible with PySynth.

For more details, checkout `report.odt`.

## Set Up

* Clone PySynth in to the projects root directory. Make sure that is resides in
  the `pysynth/` directory.
* Run `python setup.py install` within the pysynth dir
* Run `main.py`
* Play `output.wav`
