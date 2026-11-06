# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.

# Print True, if A is a strict superset of each of the  sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

# Example
# Set([1,3,4]) is a strict superset of set([1,3]).
# Set([1,3,4]) is not a strict superset of set([1,3,4]).
# Set([1,3,4]) is not a strict superset of set(1,3,5).

# Input Format

# The first line contains the space separated elements of set A.
# The second line contains integer n, the number of other sets.
# The next  lines contains the space separated elements of the other sets.

# Output Format

# Print True if set A is a strict superset of all other N sets. Otherwise, print False.


main_set=set(map(int, input().split()))
print(main_set)
no_of_subsets=int(input())

result=True

for _ in range(no_of_subsets):
    subset=set(map(int, input().split()))

    if not main_set > subset:
        result=False

print(result)