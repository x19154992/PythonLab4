import re


def re_show(pat, s):
    print(re.compile(pat, re.M).sub("{\g<0>}", s.strip()))


s = """Mary had a little lamb,
And everywhere that Mary,
went, the lamb as sure
to go"""


re_show(r"^Mary",s)
re_show(r"Mary$",s)
