# https://www.py4e.com/html3/07-files

fname = input('enter the file name: ')
file = open(fname)
count = 0
Sum = 0
for line in file:
	if line.startswith('X-DSPAM-Confidence: '):
		start = line.find(':')
		end = line.find('\n')
		num = float(line[start+1:end])
		Sum = Sum + num
		count += 1

avgConf = Sum/count
print('avg spam conf: ', avgConf)
