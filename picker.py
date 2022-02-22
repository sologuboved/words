from itertools import permutations


def pick(initial_masked, incl, excl):
    suitables = list()
    incl += ['_' for _ in range(initial_masked.count('_') - len(incl))]
    for perm in permutations(incl, len(initial_masked)):
        masked_candidate = get_masked_candidate(initial_masked, perm)
        suitables.extend(find_suitables(masked_candidate, excl))
    print(f"Found {len(suitables)}")
    for suitable in suitables:
        print(f"\t{suitable}")


def get_masked_candidate(initial_masked, perm):
    return ''.join(
        initial_masked[indx] if initial_masked[indx] != '_' else perm[indx] for indx in range(len(initial_masked))
    )


def find_suitables(masked, excl):
    suitables = list()
    with open('english.txt') as handler:
        for word in handler:
            word = word[:-1]
            if is_suitable(masked, excl, word):
                suitables.append(word)
    return suitables


def is_suitable(masked, excl, word):
    if len(word) != len(masked):
        return False
    if set(word) & excl:
        return False
    for item in zip(masked, word):
        if len(set(item) - {'_'}) > 1:
            return False
    return True


if __name__ == '__main__':
    pick('_____', ['r', 't', 'h', 'o', 'n'], {'e', 'a', 'u', 'm', 'f', 'i', 'y'})
