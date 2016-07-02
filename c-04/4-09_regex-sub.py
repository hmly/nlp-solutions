# Chapter 4, ex. 9a
# Main
str = ' The Python   World of   today. '
print 'String:', str
print ' '.join(str.split()), '\n'

# Chapter 4, ex. 9b
# Main
import re
str = re.sub(r'^ | $', r'', str)
print re.sub(r' +', r' ', str)
