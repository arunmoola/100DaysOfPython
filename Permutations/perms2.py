from itertools import combinations_with_replacement
from collections import defaultdict

def count_achievable_scores(ring_scores, num_arrows, min_score, max_score):
    achievable_scores = defaultdict(list)
    
    # Generate all possible combinations of arrow placements
    for combination in combinations_with_replacement(ring_scores, num_arrows):
        total_score = sum(combination)
        if min_score <= total_score <= max_score:
            achievable_scores[total_score].append(combination)
    
    # Count achievable scores within the given range
    count = sum(1 for score in range(min_score, max_score + 1) if score in achievable_scores)
    
    return count, achievable_scores

# Solve the specific problem in the image
ring_scores = [11, 7, 5, 1]
num_arrows = 6
min_score = 34
max_score = 68

count, achievable = count_achievable_scores(ring_scores, num_arrows, min_score, max_score)

print(f"Number of achievable scores between {min_score} and {max_score}: {count}")
print("Achievable scores and their combinations:")
for score in sorted(achievable.keys()):
    print(f"\nScore {score}:")
    for combination in achievable[score][:5]:  # Limiting to 5 combinations per score for brevity
        print(f"  {combination}")
    if len(achievable[score]) > 5:
        print(f"  ... and {len(achievable[score]) - 5} more combinations")

# Example of using the function with different inputs
custom_ring_scores = [10, 8, 6, 4, 2]
custom_num_arrows = 5
custom_min_score = 30
custom_max_score = 50

custom_count, custom_achievable = count_achievable_scores(custom_ring_scores, custom_num_arrows, custom_min_score, custom_max_score)

print(f"\nCustom example:")
print(f"Number of achievable scores between {custom_min_score} and {custom_max_score}: {custom_count}")
print("Achievable scores and their combinations:")
for score in sorted(custom_achievable.keys()):
    print(f"\nScore {score}:")
    for combination in custom_achievable[score][:5]:  # Limiting to 5 combinations per score for brevity
        print(f"  {combination}")
    if len(custom_achievable[score]) > 5:
        print(f"  ... and {len(custom_achievable[score]) - 5} more combinations")