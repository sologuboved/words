def get_verdict(candidate, word):
    candidate = candidate.lower()
    if len(candidate) != len(word):
        return "Wrong lenth"
    masked = list('_' * len(word))
    incl = list()
    excl = set()
    for indx in range(len(candidate)):
        letter = candidate[indx]
        if word[indx] == letter:
            masked[indx] = letter
            continue
        if letter in word:
            incl.append(letter)
        else:
            excl.add(letter)
    return ''.join(masked), incl, excl


if __name__ == '__main__':
    print(get_verdict('skate', 'place'))


