def next_permutation(runs):
    # Step 1: Find the first pair (i, i+1) such that runs[i] < runs[i+1]
    i = len(runs) - 2
    while i >= 0 and runs[i] >= runs[i+1]:
        i -= 1
    
    if i == -1:
        # The array is in descending order, so reverse it to get the smallest permutation
        runs.reverse()
        return
    
    # Step 2: Find the rightmost element larger than runs[i]
    j = len(runs) - 1
    while runs[j] <= runs[i]:
        j -= 1
    
    # Step 3: Swap runs[i] and runs[j]
    runs[i], runs[j] = runs[j], runs[i]
    
    # Step 4: Reverse the subarray to the right of i
    runs[i+1:] = reversed(runs[i+1:])

# Example usage:
arr = [1, 2, 3]
next_permutation(arr)
print(arr)  # This will print [1, 3, 2]
