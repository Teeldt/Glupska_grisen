# Glupska Grisen
# Teo Elmfeldt
from __future__ import division
from gg_ref import run_strikes, run_count
import operator
result = {} # where I will store all data

# part for running based on amount of strikes
def simulated_runs(tactic, times, which_one): # simulates the specified amount of loops for each test
    i = 0
    saved = 0
    if which_one == '1':
        while i < times:
            saved += run_strikes(tactic) # adds the points from simulated session
            i += 1
    elif which_one == '2':
        while i < times:
            saved += run_count(tactic)
            i += 1
    else:
        print "Failed"
    saved /= times # to get an average as output
    return saved

def test_all(max_test, times, which_one): # loops through each variation
    tactic = 1
    print "Testing %d..." % tactic
    while tactic <= max_test:
        test = simulated_runs(tactic, times, which_one)
        result[tactic] = test # adds the new result to the dictionary
        print "Average result:", test
        tactic += 1 # add one to the tested value and repeat
        if tactic <= max_test:
            print "Testing %d..." % tactic
        else:
            print "Done! Thank you for your patience."

times = int(raw_input("How many times do you want to simulate? "))
print """Which strategy do you want to test?
1: Finish after a certain number of strikes with the die.
2: Finish when a certain number is reached."""
which_one = raw_input()
if which_one == '1':
    test_all(15, times, '1') # change from default 15 in first argument to change scope
elif which_one == '2':
    test_all(40, times, '2') # change from default 30 in first argument to change scope
else:
    print "Please give me '1' or '2'"
    quit()

highest = max(result.iteritems(), key=operator.itemgetter(1)) [0]
print "The highest average of: %f\nis reached with number: %d\nusing setting: %s" % (result[highest], highest, which_one)