import webbrowser
import time

break_time = 4
break_ct = 0
while break_ct < break_time:
	webbrowser.open('https://www.youtube.com/watch?v=Py2f38iPBeI')
	time.sleep(2)
	print(time.ctime())
	break_ct += 1
