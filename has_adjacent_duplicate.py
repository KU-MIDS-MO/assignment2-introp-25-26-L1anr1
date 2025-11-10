def has_adjacent_duplicate(L):
    for i in range (1, len(L)):
        if L[i-1] == L[i]:
            return True
    return False
