
# Create By....: Giovani Winter Pacheco
# Version......: 1.0
# last Update..: 02/03/2023
# Function Name: valEmail
# Notes........: All functions are available to be used not commercially but to contribute to the data governance and quality community.
# last changes.:
#              --- 01/03 - Function that aims to validate the email returning a data score. 
#                          This function is not intended to perform data cleaning, but to validate and 
#                          return a score that makes it possible to measure the quality of the data.  
# 


def valEmail(input):
  # 1.1 Import modules
  import re

  # 1.2 Function Data cleasing

  def trim(text):  
    rtrim = text.rstrip(" .,*-+ ")  
    trim = rtrim.lstrip(" .,*-+ ")  
    return trim


  # 1.3 Variables setup and cleasing
  email = trim(input)

  pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
  valPattern = bool(re.match(pattern,email))

  i = email.index('@') + 1 # identifies the position of the element @   
  p1 = email[:i]           # first part of email
  p2 = email[i:]           # secound part of email

  # 1.4 Scrolls through the dictionary to validate the email domain.
  for key,value in dic.items():
    result = bool(key == p2)
  
    if result == True:
      vEmail = p1+value
    else:
      email

  if (email == vEmail and valPattern == True):
    score = '001' # Email with valid format and domain
    rtrn = email
  elif (email != vEmail and valPattern == True):
    score = '002' # Email with valid format and correct domain
    rtrn = vEmail
  elif (email != vEmail and result == False and valPattern == True):
    score = '003' # Email with unregistered domain, but valid format
    rtrn = email
  elif (email != vEmail and valPattern == False):
    score = '020' # Email with invalid domain and format.
    rtrn = email
  else:
    score = '099' # Unmapped error.
    rtrn = email

  return(score,rtrn)
