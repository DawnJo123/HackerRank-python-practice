# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.

# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.

# Input Format
# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.

# Output Format
# Output True or False for each test case on separate lines.

no_of_testcases=int(input())
for _ in range(no_of_testcases):
    no_of_elements_A=int(input())
    set_A=set(map(int, input().split()))
    
    no_of_elements_B=int(input())
    set_B=set(map(int, input().split()))
    
    print(set_A.issubset(set_B))
    