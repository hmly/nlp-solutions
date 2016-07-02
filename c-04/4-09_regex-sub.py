import re

str = ' The Python   World of   today. '
print('String:', str)
print(' '.join(str.split()), '\n')

str = re.sub(r'^ | $', r'', str)
print(re.sub(r' +', r' ', str))
