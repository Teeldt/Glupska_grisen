from __future__ import division
from gg_36_fel import run_times

def test(times, tactic):
    i = 0
    while i < times:
        saved = 0
        saved += run_times(tactic, 1)
        i += 1
    
    #print saved
    return saved

def dif_tactics(times, max_test):
    i = 1
    while i <= max_test:
        result = test(times, i)
        #print result
        result = result / times
        #print result
        i = i + 1
        
dif_tactics(1, 6)