"""
helper functions
"""

import re
def sanitize(phrase, substitute):
  return re.sub(r'[^A-Za-z0-9 ]+', substitute, phrase)