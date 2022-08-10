import re

pattern = r".+w.+"
text = """
The quick brown fox jumps over the lazy dog.
Python Exercises.
"""
res = re.search(pattern, text)
print(res.group())


import re

pattern = r".+w.+"
text ="""
wonderful
owner
"""
res = re.search(pattern, text)
print(res.group())

import re

pattern = r"42.+"
text = """23 street
42 meaning of life
"""
res = re.search(pattern, text)
print(res.group())


import re
text = '0770775596 -> +996770775596'
pattern = r'^0'

result = re.sub(pattern,"+996",text)
print(result)

import re

text = 'localhost:8888/ilovepython'
p = re.compile(r'[^localhost:8888/].+')
res = p.findall(text)
print(res)