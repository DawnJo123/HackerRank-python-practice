
import re

no_of_emails=int(input())

pattern=r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'

def matcher(pattern, email):
    return bool(re.match(pattern,email))

valid_emails=[]

for _ in range(no_of_emails):
    email=str(input())
    
    if matcher(pattern, email):
        valid_emails.append(email)

valid_emails.sort()

print(valid_emails)