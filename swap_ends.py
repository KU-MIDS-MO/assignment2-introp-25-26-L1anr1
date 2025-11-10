def swap_ends(L, k):
    if len(L)/2 < k or len(L) == 0 or k <= 0:
        return (L.copy(),0)  
    else:
        new_list = L[-k:] + L[k:-k] + L[:k]
        num_swaps = k
        return (new_list, num_swaps)
