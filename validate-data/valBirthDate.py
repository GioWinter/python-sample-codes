# Create By....: Giovani Winter Pacheco
# Version......: 1.0
# Function Name: valBirthDate
# last Update..: 01/03/2023
# Notes........: All functions are available to be used not commercially but to contribute to the data governance and quality community.
# last changes.:
#              --- 01/03 - Function that aims to validate the date of birth by validating format and returning a data score. 
#                          This function is not intended to perform data cleaning, but to validate and return a score that makes it possible to measure the quality of the data.  
#


def valBirthDate(input):

  # 1 .1 Import Libs
  from datetime import date, datetime
  import re

  # 1.2 Creating a dictionary with the formats to be validated.
  regDict = {'^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$':'%d/%m/%Y',
             '^([0-2][0-9]|(3)[0-1])(-)(((0)[0-9])|((1)[0-2]))(-)\d{4}$':'%d-%m-%Y',
             '^(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/[0-9]{4}$':'%m/%d/%Y',
             '^(\d{4}(-?\d\d){2})[tT]?((\d\d:?){1,2}(\d\d)?(.\d{3})?([zZ]|[+-](\d\d):?(\d\d)))?$':'%Y-%m-%d',
             '^(19[5-9][0-9]|20[0-4][0-9]|2050)[-\/](0?[1-9]|1[0-2])[-\/](0?[1-9]|[12][0-9]|3[01])$':'%Y/%m/%d'}

  # 1.3 Instantiates the variable with the date format that will be used to validate and format the data output.
  tgtFormat = "%Y-%m-%d"


  # 1.4 Traverses the data dictionary to validate the data regex structure and return the value of dict. 
  for key,value in regDict.items():
    rslt = bool(re.match(key,input))

    if rslt == True:
     srcFormt = value
     statusFormat = rslt
     break

  # 1.5 Converts the date format as defined in item 1.2
  try:
    dataObject  = datetime.strptime(input, srcFormt).strftime(tgtFormat)
  except ValueError:
    msgErro = '099'

  # 1.6 Convert string to datetime format. 
  d1 = datetime.strptime(dataObject,tgtFormat)
  d2 = datetime.today()

  # 1.7 calculates the number of days between two dates
  qtd = abs((d2 - d1).days)

  # 1.8 Realized logical test to validate the status os information. 
  if (statusFormat == True and qtd > 0):
    score = '001' # Valid date format and number of days greater than one.
  elif (statusFormat == True and qtd < 1):
    score = '020' # Valid date format, but number of days less than one.
  elif (statusFormat == False and qtd < 1):
    score = '021' # Date format and number of days less than one.
  else:
    score = '099' # Unmapped error message

  return score 
