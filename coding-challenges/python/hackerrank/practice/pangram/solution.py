'''Normally I'd structure code better, but this calls for a cheeky one-liner.
'''
print 'pangram' if len(set(raw_input().lower())) == 27 else 'not pangram'
