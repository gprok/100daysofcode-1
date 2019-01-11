import re

def firstNumber(string):
    """This function returns at least one matching digit."""
    pattern = re.compile(r"\d{1,}") # For brevity, this is the same as r"\d+"
    result = pattern.match(string)
    if result:
        return  result.group()
    return None

def allNumbers(string):
    """This function returns all matching digit."""
    pattern = re.compile(r"\d{1,}") # For brevity, this is the same as r"\d+"
    result = pattern.findall(string)
    if result:
        return  result
    return None

# Call our function, passing in our string
print(firstNumber("007 James Bond 000"))
print(allNumbers("007 James Bond 000"))
