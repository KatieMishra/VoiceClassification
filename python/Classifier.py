"""Katie Mishra | July 2019 | krmishra@stanford.edu
Takes in JSON dictionary files and matches new entry to best fit within existing entries
usinig least means squared. """

import numpy as np
import json
import os

# will only print initial string if program somehow didn't classify to a given voice
closest_voice = "failed to classify"
closest_voice_score = 0;

# compare to one chosen voice
with open('possible_voices/chosen_voice.json') as test_file:
    test_data = json.load(test_file)

    # loop over all possible classification voices
    for filename in os.listdir('possible_voices'):
        # open data file for each individual voice
        with open(os.path.join('possible_voices', filename)) as compare_file:
            compare_data = json.load(compare_file)
            total_score = 0;
            # get least means squared distance of chosen voice from current api voice we're looking at
            for phenome in compare_data:
                duration = abs(float(test_data[phenome]["duration"] - compare_data[phenome]["duration"])/(compare_data[phenome]["duration"]**2))
                acsr = abs(float(test_data[phenome]["acsr"] - compare_data[phenome]["acsr"])/(compare_data[phenome]["acsr"]**2))
                total_score += duration + acsr
            # if current voice is closer, set to be the best voice
            if (closest_voice_score == 0 or total_score < closest_voice_score):
                closest_voice_score = total_score;
                closest_voice = filename

print(closest_voice)
