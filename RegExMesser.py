import re

string = """Mary had a little lamb,
And everywhere that Mary,
went, the lamb as sure
to go"""


# print(re.compile(pat, re.M).sub("{\g<0>}", s.strip()))
pattern = r"lamb"
prog = re.compile(pattern)
prog.sub("a","c")

result = prog.match(string)

# result = re.match(pattern, string)
print(result)
print(type(pattern))
print(type(prog))
print(type(result))
