Q1
import sys

def make_input(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
    # print('loooook',argv)
    input_str = []
    for i, v in enumerate(argv):
        # print("argv[{0}]: {1}".format(i, v))
        input_str.append(v)
    return input_str

def MED(input_s):
  # print(len(input_s))
  if len(input_s) > 2:
    sys.exit(1)
  elif len(input_s) < 2:
    print(len(input_s[0]))
  else:
    s1 = input_s[0]
    s2 = input_s[1]
    # print(s1,s2)
    
    if s1 and not s2:
      print(len(s1))
    elif s2 and not s1:
      print(len(s2))

    

    len1 = len(s1)
    len2 = len(s2)

    if len1 > 1000 or len2 > 1000:
      sys.exit(1)

    accumulator = [[0 for x in range(len2+1)] for y in range(len1+1)]
    
    for i in range(len1+1):
      accumulator[i][0] = i
    for j in range(len2+1):
      accumulator[0][j] = j
    # print(accumulator)
  
    for i in range(1, len1+1):
      chr1 = s1[i-1]
      for j in range(1, len2+1):
        chr2 = s2[j-1]
        if chr1 == chr2:
          accumulator[i][j] = accumulator[i-1][j-1]
        else:
          accumulator[i][j] = min(accumulator[i][j-1],accumulator[i-1][j],accumulator[i-1][j-1]) + 1

    print(accumulator[i][j])


if __name__ == '__main__':
    input_str = make_input(sys.argv[1:])
    # print(input_str)
    MED(input_str)




Q2
import sys

def check_s_g(maze):
  check_s_flag=0
  check_g_flag=0
  for i, path in enumerate(maze):
    # print(i, path)
    for j, step in enumerate(path):
      # print(j, step)
      if step not in ['s','g','.','#']:
        print(-1)
        sys.exit(-1)
      if step == 's':
        start = [i, j]
        check_s_flag+=1

      if step == 'g':
        goal = [i, j]
        check_g_flag+=1
        if i == 0 and j ==0:
          if maze[i][j+1] == '#' or maze[i+1][j] == '#':
            print(-1)
  
  if check_g_flag <2 and check_s_flag<2:
    return start, goal
  else:
    print(-1)


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    maze = []
    for i, v in enumerate(lines):
        # print("line[{0}]: {1}".format(i, v))
        if i == 0:
          # print(v)
          v = v.split(" ")
          H = int(v[0])
          W = int(v[1])

          if 1 > H or H > 300 or 1 > W or W > 300:

            print(-1)
            return
        else:
          maze.append(list(v))

    start, goal = check_s_g(maze)
    s_x, s_y = start[0], start[1]
    g_x, g_y = goal[0], goal[1]

    res = 0
    for x, y in [[0,1],[0,-1],[1,0],[-1,0]]:
      nx = x+s_x
      ny = y+s_y
      while 0<=nx <H and 0<=ny<W:
        if maze[nx][ny] == '#':
          res += 1
          break
        nx += x 
        ny += y 
    # print(res)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)




Q3
import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    line1 = lines[0].split(" ")
    V, E, X, Y = int(line1[0]), int(line1[1]), int(line1[2]), int(line1[3])
    n = list(map(int, lines[1].split(" ")))
    m = list(map(int, lines[2].split(" ")))
    edge = []
    adj_mat = [[0 for i in range(V)] for j in range(V)]
    for i in range(V):
      for j in range(V):
        if i == j:
          adj_mat[i][j] = 1
    # print(adj_mat)
    # print(edge)
    for i, v in enumerate(lines):
      if i >= 3:
        # print("line[{0}]: {1}".format(i, v))
        edge.append(list(map(int, v.split(" "))))
    # print(edge)
    for e in edge:
      x, y = e
      adj_mat[x-1][y-1] = 1
    # print(adj_mat)

    status = [0 for i in range(V)]
    infect = [0 for i in range(V)]
    for i, ppl in enumerate(n):
      infect[ppl-1] = 1
      status[ppl-1] = m[i]

    # print('iiiiiinnnnnnnniiiii',status)
    # print('iiiiiinnnnnnnniiiii',infect)
    


    for i in range(Y): # time T
      for idx, ppl in enumerate(n):
        if i == m[idx]:
          infect[ppl-1] = 0
          status[ppl-1] -= 1
        for v in range(V):
          if idx != v:
            if adj_mat[idx][v] == 1:
              infect[v]=1
              status[v]=m[idx]
    # print(infect)
    print(sum(infect))



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
