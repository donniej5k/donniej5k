import re

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."

# Corrected regex pattern with case-insensitivity
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

print(emails)
