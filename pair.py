#!/usr/local/bin/anaconda3/bin/python3

import numpy as np
import pandas as pd
from score_pair import score_pair
from itertools import permutations
import operator

def pair(mentor_csv, mentee_csv):
    mentors = pd.read_csv(mentor_csv)
    mentees = pd.read_csv(mentee_csv)

    mentors.fillna(3, inplace=True)
    mentees.fillna(3, inplace=True)

    mentee_pairing_options = {k: {} for k in mentees['UT NetID']}
    mentor_pairs = {k: [] for k in mentors['UT NetID']}
    """
    if len(mentees['UT NetID']) > 2 * len(mentors['UT NetID']):
        print("Error! We have {} mentees but only {} mentors".format(len(mentees['UT NetID']), len(mentors['UT NetID'])))
        return
        """

    for i, mentee in mentees.iterrows():
        for j, mentor in mentors.iterrows():
            mentee_pairing_options[mentee['UT NetID']][mentor['UT NetID']] = score_pair(mentee, mentor)

    print(mentee_pairing_options)

    # Now run our exhaustive search over the sample space
    # NAY! Simulated annealing to the rescue
    available_mentors = list(mentors['UT NetID'])
    available_mentors.extend(mentors['UT NetID'])
    g = {k: '' for k in mentees['UT NetID']}
    config_score = 0

    for menteenid in g:
        for mentornid, score in sorted(mentee_pairing_options[menteenid].items(), key=operator.itemgetter(1), reverse=True):
            if mentornid in available_mentors:
                g[menteenid] = mentornid
                available_mentors.remove(mentornid)
                config_score += score
                break
    for k in g:
        print("{}: {}".format(k, g[k]))
    print("Total Config Score: {}".format(config_score))




"""
for key, val in mentee_pairing_options.items():
    print(key)
    for netID, score in val.items():
        print("\t{:.2f}".format(score), " -- ", netID)
    print()
"""
if __name__=="__main__":
    pair("mentor-long.csv", "mentee-long.csv")
