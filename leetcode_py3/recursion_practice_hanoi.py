def hanoi(num_disk, frm, buf, to):
    if num_disk <= 0:
        return 

    hanoi(num_disk-1, frm, to, buf)
    print('move ', num_disk,'th ', frm, '->', to)
    hanoi(num_disk-1, buf, frm, to)

if __name__ == '__main__':
    hanoi(3, 'a', 'b', 'c')