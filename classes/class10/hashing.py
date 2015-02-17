##
## Some estimates about bitcoin mining
##

from __future__ import division

difficulty = 44455415962 # from https://blockchain.info/stats, 15 Feb 2015

def find_target(difficulty):
    return 2 ** 224 / difficulty

success_probability = find_target(difficulty) / 2**256
expected_hashes = 1.0 / success_probability # don't divide by 2, not looking for one key

def nanoseconds_to_years(ns):
    return ns / (10**9 * 60 * 60 * 24 * 365.25)

time_to_hash = 760 * 2 # ns, as measured on EC2 node

years_needed = nanoseconds_to_years(expected_hashes * time_to_hash)

print "Years: " + str(years_needed)





