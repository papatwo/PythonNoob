# different input in python
import sys

def py_input():
    words = input("请输入内容(单独输入':w'保存退出):")

    while words != ':w':

        line = lines.append(words)
        words = input()

    print(lines)
    
def py_input_iter():
    try:
        for line in map(input, repeat('请输入内容（单独输入':w'保存退出):')):
            lines.append(line) 
    print(lines)

def sys_input():
    for l in sys.stdin:

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
        lines.append(l)
        lines.append(list(map(int, l.split(" ")))
    print(lines)
    for i, v in enumerate(lines):
         print("line[{0}]: {1}".format(i, v))
