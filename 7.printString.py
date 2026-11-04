# The included code stub will read an integer,n, from STDIN.

# Without using any string methods, try to print the following:
# 1234...n

# Note that "" represents the consecutive values in between.
# Example
# n=5

# Print the string 12345.

n = int(input())
string=""
for i in range(1,n+1):
    string+=str(i)
    
print(string)