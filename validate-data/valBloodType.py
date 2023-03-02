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


def valBloodType(type):
    # 1.1 Import Libs
    import re

    # 1.2 setup regex format
    pattern = "(A|B|AB|O)[+-]$"

    # 1.3 check the status os type
    status_match = re.match(pattern,type.upper())

    if status_match:
        result = "valid"
    else:
        result = "invalid"
    return result