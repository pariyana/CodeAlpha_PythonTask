import re

text = """
abc@gmail.com
test@yahoo.com
sample123@gmail.com
"""

emails = re.findall(r'\S+@\S+', text)

print("Email addresses found:")
for email in emails:
    print(email)