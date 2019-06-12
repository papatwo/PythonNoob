# A=[1,0,2,0,0,2]
A=[1,4,7,3,2,1]

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    def cal_bin(A):
        temp = 0
        for a in A:
            if a < 0 or a > 10000:
                return False
            else:
                temp+=2**a
        return temp
        
    def d2b(num):
        b=[]
        while num>1:
            b.insert(0,num%2)
            num = num//2
        if num == 1:
            b.insert(0,1)
        return b
            
            
    if not A:
        return False
    else:
        if len(A) > 100000:
            return False
        num = cal_bin(A)
        print(num)
        binary = d2b(num)
        B = []
        print(binary)
        for i,b in enumerate(binary):
            if b == 1:
                B.append(i+1)
        print(B)
        
        print(len(B)) 

if __name__ == '__main__':
    solution(A)
            