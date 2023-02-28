def checkBirthDate(birthDate):
    from datetime import date, datetime
    import re

    format = '%d-%m-%Y'
    pattern = "^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$"
    result = re.match(pattern, birthDate)

    if result:
        result = True
    else:
        result = False

    d1 = datetime.today()
    d2 = datetime.strptime(birthDate, format)

    # Calculate the number of day beteween to dates.
    qtdDays = abs((d2 - d1).days)

    if (result == True and qtdDays > 0):
        score = '001'  # Valid date format and number of days greater than one.
    elif (result == True and qtdDays < 1):
        score = '020'  # Valid date format, but number of days less than one.
    elif (result == False and qtdDays < 1):
        score = '021'  # Date format and number of days less than one.
    else:
        score = '099'  # Unmapped error message

    return score