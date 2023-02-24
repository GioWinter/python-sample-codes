import re

# convert a list to lowercase
def lower_case(my_list):
  return [x.lower() for x in my_list]

# convert a list to uppercase
def upper_case(my_list):
  return [x.upper for x in my_list]


def trim(text):
  # remove caracters e espação a direita.
  rtrim = text.rstrip(" .,*-+ ")
  # remove caracters e espação a direita.
  ltrim = rtrim.lstrip(" .,*-+ ")
  return ltrim


def check_domain_email(email, ldomain):
    # set lista with invalid doamins

    index = email.index('@')
    domain = email[index:]

    # Convert a list to lowercase.
    invalidDomain = lower_case(ldomain)

    # Check if the email domain exists in the invalid list.
    if domain.lower() not in invalidDomain:
        result = 'valid'
    else:
        result = 'invalid'
    return result


def check_pattern_email(email):
    # set the pattern of regex to validate email
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    statusMatch = re.match(pattern, email)

    if statusMatch:
        rMatch = 'valid'
    else:
        rMatch = 'invalid'

    return rMatch

def validateEmail(email,domain):
  l1 = lambda a,b : True if (a != b) else False

  if (check_domain_email(email,domain) == 'valid' and check_pattern_email(email) == 'valid'):
    score = '001' # Email with valid domain and email format.
  elif (check_domain_email(trim(email),domain) == 'valid' and check_pattern_email(trim(email)) == 'valid' and l1(trim(email),email) == True):
    score = '002' # Email with valid domain and format and minor corrections
  elif (check_domain_email(email,domain) == 'invalid' and check_pattern_email(email) == 'invalid'):
    score = '021' # Email with domain and format invalid
  elif (check_domain_email(email,domain) == 'invalid' and check_pattern_email(email) == 'valid'):
    score = '022' # Email with domain invalid but format valid.
  elif (check_domain_email(email,domain) == 'valid' and check_pattern_email(email) == 'invalid'):
    score = '023' # Email with domain valid and format invalid.

  return score, trim(email)