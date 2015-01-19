from __future__ import division
from gg_ref import run
from gg_ref_count import run_count
import operator
result = {}
# part for running based on amount of strikes
def testing(tactic, times):
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
    print "Testing %d..." % tactic
    while tactic <= max_test:
        test = testing(tactic, times)
        result[tactic] = test
        if test > 0:
            print "Average result:", test
        tactic += 1
        if tactic <= max_test:
            print "Testing %d..." % tactic
        else:
            print "Done! Thank you for your patience."

def run_strikes():
    times = int(raw_input("How many times do you want to simulate? "))
    test_all(15, times)

# part for running based on points
def test_countto(tactic, times):
    i = 0
    saved = 0
    while i < times:
        saved += run_count(tactic)
        i += 1
    saved = saved / times
    return saved

#print test(1, 5)

def test_all_countto(max_test, times):
    tactic = 1
    print "Testing %d..." % tactic
    while tactic <= max_test:
        test = test_countto(tactic, times)
        result[tactic] = test
        if test > 0:
            print "Average result:", test
        tactic += 1
        if tactic <= max_test:
            print "Testing %d..." % tactic
        else:
            print "Done! Thank you for your patience."

def run_countto():
    times = int(raw_input("How many times do you want to simulate? "))
    up_to = int(raw_input("How high do you want to go? "))
    test_all_countto(up_to, times)

print """Which strategy do you want to test?
1: Amount of strikes with the die
2: Which sum to step down at"""
which_one = int(raw_input())
if which_one == 1:
    run_strikes()
elif which_one == 2:
    run_countto()
else:
    print "Please give me '1' or '2'"

highest = max(result.iteritems(), key=operator.itemgetter(1)) [0]
print "The highest value of: %f\nis received with number: %d" % (result[highest], highest)