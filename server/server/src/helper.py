"""
helper functions
"""

import re
def sanitize(phrase, substitute):
  return re.sub(r'[^가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9]+', substitute, phrase)