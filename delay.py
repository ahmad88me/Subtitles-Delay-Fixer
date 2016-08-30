

import sys
from datetime import datetime, timedelta
import os

print 'File: '+sys.argv[1]
print 'Delay of: '+sys.argv[2]



def get_time(time_string, delay):
	hours, minutes, seconds_with_comma = time_string.split(':')
	seconds, comma = seconds_with_comma.split(',')
	hours = int(hours)
	minutes = int(minutes)
	seconds = int(seconds)
	current_time = datetime(year=2000, month=1, day=1,hour = hours, minute= minutes, second = seconds)
	target_time = current_time - timedelta(seconds=delay)
	return '%02d:%02d:%02d,%s' % (target_time.hour, target_time.minute, target_time.second, comma)


def delay_single_line(line, nsec):
	from_t, to_t = line.split('-->')
	new_from_t = get_time(from_t.strip(), nsec)
	new_to_t = get_time(to_t.strip(), nsec)
	return '%s --> %s' % (new_from_t, new_to_t)
	#res = '%s --> %s' % (new_from_t, new_to_t)
	#return res + os.linesep

#s = '00:02:15,968 --> 00:02:18,199   '
#print s
#print delay_single_line(s, 61)
def main():
	delay = int(sys.argv[2])
	f = open(sys.argv[1], 'r')
	new_sub = []
	for l in f.readlines():
		try:
			ss = delay_single_line(l, delay)
			new_sub.append(ss+os.linesep)
		except:
			#new_sub.append(l.strip()+os.linesep)
			new_sub.append(l.strip())
			new_sub.append(os.linesep)
	f.close()
	f = open('new_sub.srt', 'w')
	for s in new_sub:
		f.write(s)
	f.close()

main()


