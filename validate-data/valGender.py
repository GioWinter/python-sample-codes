# Create By.....: Giovani Winter Pacheco
# Version.......: 1.0
# Function Name.: valGender
# Notes.........: All functions are available to be used not commercially but to contribute to the data governance and quality community.
# last Update...: 01/03/2023
# Notes.........: All functions are available to be used not commercially but to contribute to the data governance and quality community.
# last changes..:
#                 --- 01/03 - Function that validate gender code based on a data dictionary with most common examples
#                             This function is not intended to perform data cleaning, but to validate and return a score 
#                             that makes it possible to measure the quality of the data.  
#


def valGender(gender):
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