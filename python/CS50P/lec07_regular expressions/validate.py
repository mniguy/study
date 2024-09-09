email = input("What's your email? ").strip()

# 01 => "@"만 있어도 valid표기
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

# 02
username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

# 03
# re library
# re.search(pattern, string, flags=0)
# pattern:
    # . any character except a newline
    # * 0 or more repetitions
    # + 1 or more repetitions
    # ? 0 or 1 repetition
    # {m} m repetitions
    # {m, n} m-n repetitions
    # ^ matches the start of the string
    # $ matches the end of the string
    # [] set of characters
    # [^] complementing the set
import re

email = input("What's your emil? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")