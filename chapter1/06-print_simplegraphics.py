# 简单打印图形1

#for i in range(0,5):
#    for i in range(0,5):
#        print('*', end=' ')
#    print('\n')

for i in range(0,5):
    print('*' * 5)
    print()

# 简单打印图形2

#for i in range(0, 4):
#    for j in range(0, 5):
#        if i == 0 or i == 3:
#            print('* ', end="")
#        else:
#            print('*       *')
#            break
#    print()

for i in range(0, 4):
    if i == 0 or i == 3:
        print('* ' * 5)
    else:
        for j in range(5):
            if j == 0 or j == 4:
                print('* ', end='')
            else:
                print('  ', end='')
        print()

# 简单图形打印3
'''
*
* *
* * *
* * * *
'''

for i in range(1, 5):
    for j in range(i):
        print('* ', end='')
    print()

# 简单图形打印4
'''
*
* *
*   *
*     *
* * * * *
'''

for i in range(1, 6):
    for j in range(i):
        if j == 0 or j == i-1 or i == 5:
            print('* ', end='')
        else:
            print('  ', end='')
            
    print()

# 简单图形打印5
'''
* * * * *
* * * * 
* * *
* *
*
'''

#for i in range(5):
#    for j in range(5-i):
#        print('* ', end='')
#    print()

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print('* ', end='')
    print()

# 简单图形打印6
# 打印空三角
'''
* * * * *
*     *
*   *
* *
*
'''

for i in range(5):
    for j in range(5-i):
        if j == 0 or j == 4-i or i == 0:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

# 简单图形打印7
'''

    *
   * *
  * * *
 * * * *
* * * * *
'''

for i in range(5):
    for j in range(5-i):
        print(' ', end='')
        
    for m in range(i+1):
        print('* ', end='')
    print()

# 简单图形打印8
'''
    *
   * *
  *   *
 *     *
* * * * *
'''

for i in range(1,6):
    for j in range(6-i, 1, -1):
        print(' ', end='')
    
    for k in range(i):
        if k == 0 or k == i-1 or i == 5:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
