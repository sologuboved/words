from itertools import permutations


def pick(initial_masked, incl, excl, sample_size=float('inf')):
    suitables = set()
    incl += ['_' for _ in range(initial_masked.count('_') - len(incl))]
    for perm in permutations(incl, initial_masked.count('_')):
        masked_candidate = get_masked_candidate(initial_masked, perm)
        suitables |= find_suitables(masked_candidate, excl, sample_size)
        if len(suitables) >= sample_size:
            break
    print(f"Found {len(suitables)}")
    for suitable in suitables:
        print(f"\t{suitable}")


def get_masked_candidate(initial_masked, perm):
    masked_candidate = ''
    indx = 0
    for char in initial_masked:
        if char == '_':
            masked_candidate += perm[indx]
            indx += 1
        else:
            masked_candidate += char
    return masked_candidate


def find_suitables(masked, excl, sample_size):
    suitables = set()
    with open('english.txt') as handler:
        for word in handler:
            word = word[:-1]
            if is_suitable(masked, excl, word):
                suitables.add(word)
                if len(suitables) == sample_size:
                    break
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
    # pick('_____', [], {'i', 'g', 'h', 't', 'p', 'a', 'c', 'e'}, 5)
    # pick('__o__', ['l', 'n'], {'i', 'g', 'h', 't', 'p', 'a', 'c', 'e', 'b', 'w'})
    pick('____e', ['o'], {'y', 'x', 'p', 'l', 'a', 'c', 'b', 'i', 'n', 'g', 'd', 'u', 's'}, 5)
