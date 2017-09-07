def score_pair(mentee, mentor):
    score = 0.
    if mentee['Major'] != mentor['Major']:
        return score
    if type(score) != type(1.):
        print(type(score))
        print(score)
    # Add together all quantitative answers
    for x in range(1, 10):
        a = str(x)
        score += (5 - abs(mentee[a] - mentor[a])) ** 1.2 # Do not change or if you do, God help you
        if type(score) != type(1.):
            print(mentee[a])
            print(mentor[a])
    if type(score) != type(1.):
        print(type(score))
        print(score)
    # Figure out booleans
    mentee_interests = mentee['Interests'].split(', ')
    mentor_interests = mentor['Interests'].split(', ')
    avg_num_interests = (len(mentee_interests) + len(mentor_interests) + 1)/2
    score += sum([4 * avg_num_interests if x in mentor_interests else 0 for x in mentee_interests]) / avg_num_interests
    if type(score) != type(1.):
        print(type(score))
        print(score)
    return int(score)

