"""
Copyright (C) 2018 August Feng <au.fengster@gmail.com>
"""

from . import rudiments, utils

def generate_251(key, quality="major"):

	if quality == "minor":
		progression = [rudiments.Chord(key+rudiments.Interval("M2"),"m7b5"), rudiments.Chord(key+rudiments.Interval("P5"),"7"), rudiments.Chord(key, "min7")]
	elif quality == "major":
		progression = [rudiments.Chord(key+rudiments.Interval("M2"),"min7"), rudiments.Chord(key+rudiments.Interval("P5"),"7"), rudiments.Chord(key, "maj7")]

	return progression
