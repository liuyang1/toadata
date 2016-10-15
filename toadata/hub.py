import StringIO


def loadMediaInfoLine(s):
    colon = s.index(':')
    a = s[:colon]
    b = s[colon + 1:]
    return a.strip(), b.strip()


def loadMediaInfo(s):
    c = s.split('\n')
    cnt, key, chk = [], None, None
    for l in c:
        if "" == l:
            if key and chk:
                cnt.append((key, chk))
                chk = None
        elif ":" not in l:
            key, chk = l, None
            chk = []
        else:
            k, v = loadMediaInfoLine(l)
            chk.append((k, v))
    return cnt


def sanity(s):
    l = ["_", "*"]
    for i in l:
        s = s.replace(i, '\\' + i)
    return s


def maxlen(ss):
    return max([len(i) for i in ss])


def just(ss):
    l = maxlen(ss)
    return [i.ljust(l) for i in ss]


def outputMakrdownLst(lst):
    lst = [(sanity(a), sanity(b)) for a, b in lst]
    rlst = zip(*lst)
    ks, vs = rlst[0], rlst[1]
    ks = just(ks)
    vs = just(vs)
    o = StringIO.StringIO()
    for k, v in zip(ks, vs):
        print >>o, "| %s | %s |" % (k, v)
    r = o.getvalue()
    o.close()
    return r


def outputMarkdown(lst, level=0):
    o = StringIO.StringIO()
    for k, v in lst:
        o.write("#" * level)
        o.write("# %s\n" % k)
        if isinstance(v, str):
            o.write("%s\n" % (v))
        elif isinstance(v, list):
            o.write("\n%s\n" % outputMakrdownLst(v))
    r = o.getvalue()
    o.close()
    return r


def MediaInfo2Markdown(s, level=0):
    o = StringIO.StringIO()
    # o.write("# MediaInfo\n\n")
    r = outputMarkdown(s, level=level + 1)
    o.write(r)
    r = o.getvalue()
    o.close()
    return r


def loadMarkdown(s):
    c = s.split('\n')
    cnt = []
    k, v = None, []
    for l in c:
        # only parse first level of markdown
        if len(l) >= 2 and l[0] == '#' and l[1] != "#":
            if k:
                cnt.append((k, v))
            k = l[1:].strip()  # skip prefix \# symbol
            v = ""
        else:
            v += l + "\n"
    return cnt
