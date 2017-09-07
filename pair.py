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
    
    if len(mentees['UT NetID']) >= 2 * len(mentors['UT NetID']):
        print("Error! We have {} mentees but only {} mentors".format(len(mentees['UT NetID']), len(mentors['UT NetID'])))

    for i, mentee in mentees.iterrows():
        for j, mentor in mentors.iterrows():
            mentee_pairing_options[mentee['UT NetID']][mentor['UT NetID']] = score_pair(mentee, mentor)

    # Now run our exhaustive search over the sample space
    # NAY! Simulated annealing to the rescue
    available_mentors_template = list(mentors['UT NetID'])
    available_mentors_template.extend(mentors['UT NetID'])
    # Number of cycles to run through
    # THIS IS THE NUMBER TO CHANGE TO RUN MORE ITERATIONS
    #   |
    #   V
    n = 100
    g = [{k: '' for k in mentees['UT NetID']} for x in range(n)]
    config_score = [0 for x in range(n)]
    carryover_term = 0
    for run in range(n): 
        # Implicit reshuffling of dictionary happens here
        # Recreate a fresh availalbe_mentors list
        available_mentors = list(available_mentors_template)
        for menteenid in g[run]:
            for mentornid, score in sorted(mentee_pairing_options[menteenid].items(), key=operator.itemgetter(1), reverse=True):
                if mentornid in available_mentors:
                    g[run][menteenid] = mentornid
                    available_mentors.remove(mentornid)
                    config_score[run] += score
                    break
        if config_score[run] > config_score[carryover_term]:
            carryover_term = run
    g = g[carryover_term]
    config_score = config_score[carryover_term]
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
