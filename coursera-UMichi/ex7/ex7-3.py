# https://www.py4e.com/html3/07-files

fname = input('enter the file name: ')
count = 0
if fname == 'na na boo boo':
	print('NA NA BOO BOO TO YOU - You have been punk d!')

else:
	if fname == 'mail.txt':
		file = open(fname)
		for line in file:
			count += 1
		print('there were ', count, 'subject lines in ', fname)
	else:
		print('File cannot be opened: ', fname)



