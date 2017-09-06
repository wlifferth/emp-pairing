def score_pair(mentee, mentor):
    score = 0
    if mentee['Major'] != mentor['Major']:
        return 0
    """
    if mentee['Concentration'] == mentors['Concentration']:
        score += 10
        """
    # Add together all quantitative answers
    for x in range(1, 10):
        a = str(x)
        score += (5 - abs(mentee[a] - mentor[a])) ** 1.2
    # Figure out booleans
    mentee_interests = mentee['Interests'].split(', ')
    mentor_interests = mentor['Interests'].split(', ')
    avg_num_interests = (len(mentee_interests) + len(mentor_interests) + 1)/2
    score += sum([4 * avg_num_interests if x in mentor_interests else 0 for x in mentee_interests]) / avg_num_interests
    return score

