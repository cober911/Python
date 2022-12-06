# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 1\n')


colors = [' red', 'green', 'blue123 ']
data = open('file.txt', 'w')
data.write('\nLINE 2\n')
data.write('LINE 3\n')
data.close()


exit()
patch = 'file.txt'
data = open(patch, 'r')
for line in data:
        print(line)
data.close()