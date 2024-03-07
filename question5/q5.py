import math

# Part (a)
def expected_rolls_for_sqrt_k(k):
    # Since the die is unbiased, the expected number of rolls to see a specific number is k
    return k

# Part (b)
def expected_rolls_to_see_all_faces(k):
    # Coupon Collector's Problem
    return k * sum([1/n for n in range(1, k+1)])

# Part (c)
def expected_rolls_biased_die():
    # For k=3 with the given probabilities, we calculate the expected rolls
    # to see all numbers at least once.
    
    # Probability to roll each number for the first time
    p1 = 1  # Always 1 since we start with 0 numbers seen
    p2 = 3/4  # Probability of rolling a number we haven't seen when we've seen 1 out of 3
    p3 = 1/2  # Probability of rolling the last unseen number when we've seen 2 out of 3
    
    # Expected rolls to see each new number
    e1 = 1/p1
    e2 = 1/p2
    e3 = 1/p3
    
    return e1 + e2 + e3

# Example usage
k = 542689137  # Example value for k
print(f"(a) Expected rolls to see number ⌊√{k}⌋: {expected_rolls_for_sqrt_k(math.floor(math.sqrt(k)))}")
print(f"(b) Expected rolls to see all faces for a {k}-faced die: {expected_rolls_to_see_all_faces(k)}")
print(f"(c) Expected rolls for biased 3-faced die to see all faces: {expected_rolls_biased_die()}")
