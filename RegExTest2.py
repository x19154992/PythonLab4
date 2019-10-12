import re


def re_show(pat, s):
    print(re.compile(pat, re.M).sub("{\g<0>}", s.strip()))

s = """Special charaters must be escaped.*"""


re_show(r".*", s)
# re_show(r".*", s)
# re_show(r".*", s)
# re_show(r".*", s)


