def find_Min_Diff(l, p):
    subsets = []
    n = len(l)

    def generate_subsets(index, subset):
        if len(subset) == p:
            subsets.append(subset.copy())
            return
        if index >= n:
            return
        subset.append(l[index])
        generate_subsets(index + 1, subset)
        subset.pop()
        generate_subsets(index + 1, subset)
 
    generate_subsets(0,[])

    min_diff = float('inf')

    for subset in subsets:
        subset_min = min(subset)
        subset_max = max(subset)
        diff = subset_max - subset_min
        min_diff = min(min_diff, diff)

    return min_diff
