from itertools import product, permutations

def find_permutations_sum_6():
    # Generate all possible combinations of 4 numbers from the set
    combinations = product(range(7), repeat=4)
    
    # Filter combinations that sum to 6
    valid_combinations = [comb for comb in combinations if sum(comb) == 6]
    
    # Generate all permutations for each valid combination
    result = set()
    for comb in valid_combinations:
        result.update(permutations(comb))
    
    return sorted(result)

# Find and print the results
results = find_permutations_sum_6()
print(f"Number of permutations: {len(results)}")
print("Permutations:")
for perm in results:
    print(perm)