import re

def format_code(name):
  code = re.sub(r'\s+', '-', name.strip())
  return code