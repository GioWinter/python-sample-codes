import re

def checkBloodType(type):
    pattern = "(A|B|AB|O)[+-]$"
    status_match = re.match(pattern,type.upper())

    if status_match:
        result = "valid"
    else:
        result = "invalid"
    return result