from __future__ import division
from gg_ref import run

def test(tactic, times):
    i = 0
    saved = 0
    while i < times:
        saved += run(tactic)
        i += 1
    saved = saved / times
    return saved

#print test(1, 5)

def test_all(max_test, times):
    tactic = 1
    while tactic <= max_test:
        print "testing %d..." % tactic
        print test(tactic, times)
        tactic += 1
test_all(15, 100)