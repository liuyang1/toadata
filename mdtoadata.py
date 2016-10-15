#! /usr/bin/env python2

import hub
import os
import subprocess


def mediainfo(fn):
    s = subprocess.check_output(["mediainfo", fn])
    r = hub.loadMediaInfo(s)
    return hub.MediaInfo2Markdown(r)


def mergeComment(cnt, oldcnt):
    for k, v in oldcnt:
        if k == "comment":
            cnt = [("comment", v)] + cnt
    return cnt


def toadatamd(fn):
    md = fn + ".md"
    oldcnt = []
    if os.path.exists(md):
        print >> sys.stderr, "find exists %s, loading..." % (md)
        oldcnt = hub.loadMarkdown(open(md).read())
    cnt = []
    mi = mediainfo(fn)
    cnt.append(("MediaInfo", mi))
    cnt = mergeComment(cnt, oldcnt)
    r = hub.outputMarkdown(cnt)
    return r

if __name__ == "__main__":
    import sys
    fn = sys.argv[1]
    r = toadatamd(fn)
    open(fn + ".md", "w").write(r)
