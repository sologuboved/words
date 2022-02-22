def get_verdict(candidate, word):
    candidate = candidate.lower()
    masked = list('_' * len(word))
    incl = list()
    excl = set()
    if len(candidate) == len(word):
        for indx in range(len(candidate)):
            letter = candidate[indx]
            if word[indx] == letter:
                masked[indx] = letter
                continue
            if letter in word:
                incl.append(letter)
            else:
                excl.add(letter)
    else:
        print("Wrong lenth")
    return ''.join(masked), incl, excl


if __name__ == '__main__':
    print(get_verdict('skate', 'place'))
