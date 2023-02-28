def validateGender(gender):
    import re

    # Regex to check valid GENDER
    regex = "(?:m|M|male|Male|f|F|female|Female|FEMALE|MALE)$"

    # Compile the ReGex
    result = re.match(regex, gender)

    # If the string is empty return false
    if (gender == None):
        return False

    # Return if the string matched the ReGex
    if result:
        score = '001'  # Domain gender code identified in the list and valid
    else:
        score = '020'  # Domain not identified in the list

    return score