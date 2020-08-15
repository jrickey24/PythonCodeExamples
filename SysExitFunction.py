# This would print 'Hello' only, as the exit function executes prior to final print statement call
import sys
print('Hello')
sys.exit()
print('Goodbye')


