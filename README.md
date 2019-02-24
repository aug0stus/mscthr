# mscthr - Unofficial Fork of musthe

This is a fork of [musthe](https://github.com/gciruelos/musthe), an implementation of music theory w/ Python.

The purpose of this fork is to accommodate the features required by www.practicemusic.org, a project I am working on to help musicians drill music theory.

# How to install

This fork is not on PyPi, meaning that you will specify this GitHub repository explicitly.

Please just clone and use "pip install ." 

# How to use (slightly different than musthe's [README.md](https://github.com/gciruelos/musthe/blob/master/README.md) )


It is very simple, everything is coded in a object-oriented style, for example:

    $ python
    >>> from mscthr import rudiments
    >>> a = rudiments.Note('A')  #Default A4
    >>> a
    Note("A4")
    >>> str(a)
    'A'


Suppose you want to create tension, so you want the perfect fifth or the minor seventh of that A, so you do:

    >>> fifth = rudiments.Interval('P5')
    >>> seventh = rudiments.Interval('m7')
    >>> a+fifth
    Note("E5")
    >>> str(a+fifth)
    'E'
    >>> str(a+seventh)
    'G'

Though it is important to see that the octaves of those notes are different:

    >>> a.octave
    4
    >>> (a+seventh).octave
    5

Now let's see basic chord usage:

	>>> rudiments.Chord(Note('A'), 'M')
	Chord(Note('A'), 'M')
	>>> rudiments.Chord(Note('A'), 'M').notes
	[Note("A4"), Note("C#5"), Note("E5")]
	>>> rudiments.Chord(Note('Bb'), 'dim').notes
	[Note("Bb4"), Note("Db5"), Note("Fb5")]

You can use a string to construct a chord:

    >>> rudiments.Chord('C#aug7') == rudiments.Chord(Note('C#'), 'aug7')
    True

Default chord type is 'M' (Major).

Now lets try scales:

    >>> s = rudiments.Scale(Note('B'), 'major')
    >>> [s[i] for i in range(len(s))]
    [Note('B4'), Note('C#5'), Note('D#5'), Note('E5'), Note('F#5'), Note('G#5'), Note('A#5')]
    >>> s[0]
    Note('B4')
    >>> s[-11]
    Note('E3')

It return a list of Note instances, so if you want a cleaner result should do something like:

    >>> s = rudiments.Scale(Note('B'), 'major')
    >>> [str(s[i]) for i in range(len(s))]
    ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']

To check if notes and chords are contained in a given scale:

    >>> rudiments.Note('D#3') in s
    True
    >>> rudiments.Note('F3') in s
    False
    >>> rudiments.Chord('C#m') in s
    True
    >>> rudiments.Chord('CM') in s
    False

Now let's try some advanced stuff: given a list of chords, find all scales that contain those:

    >>> chords = [rudiments.Chord('Cm'), rudiments.Chord('Fm7'), rudiments.Chord('Gm')]
    >>> for scale in rudiments.all.scales():
    ...     if chords in scale:
    ...         print(scale)
    ...
    C natural_minor
    Eb major

## Specifics to mscthr

Chord voicing feature:

	>>> from mscthr import rudiments,
	>>> chord = rudiments.Chord('Amaj7')
	>>> chord.notes
	[Note('A4'), Note('C#5'), Note('E5'), Note('G#5')]
	>>> chord.drop2
	[Note('E5'), Note('A4'), Note('C#5'), Note('G#5')]

Chord inversions:

	>>> from mscthr import rudiments
	>>> chord = rudiments.Chord('Amaj7', inversion='second')
	>>> chord.notes
	[Note('E5'), Note('G#5'), Note('A5'), Note('C#6')]

Randomizer:

	>>> from mscthr import rudiments,utils
	>>> chord = utils.random_items(rudiments.all.chords())
	>>> chord
	Chord(Note('G#4'), 'maj7')
	>>> chord = utils.random_items(rudiments.all.chords())
	>>> chord
	C

