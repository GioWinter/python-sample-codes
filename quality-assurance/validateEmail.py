import re

def check_domain_email(email):
  # set lista with invalid doamins
  invalidDomain = ['@@gmail.com','@@@gmail.com','@@@@gmail.com','@gmail.com.br','@@outlook.com','@outlook.com.br']
  
  index = email.index('@')
  domain = email[index:]

  # Check if the email domain exists in the invalid list.
  if domain not in invalidDomain:
    result = 'valid'
  else:
    result = 'invalid'
  return result


def check_pattern_email(email):
  # set the pattern of regex to validate email
  pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
  statusMatch = re.match(pattern,email)

  if statusMatch:
    rMatch = 'valid'
  else:
    rMatch = 'invalid'
  
  return rMatch



def validateEmail(email):
  domainStatus = check_domain_email(email)
  patternStatus = check_pattern_email(email)

  if domainStatus == 'valid' and patternStatus == 'valid':
    result = True
  elif domainStatus == 'valid' or patternStatus == 'invalid':
    result = False
  else:
    result = False
  return result