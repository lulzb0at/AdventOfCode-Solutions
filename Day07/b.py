with open('input.txt','r') as fh: lines = fh.read()

cwd = '/'
lsof = []

for line in lines.splitlines()[1:]:
 
    if line.startswith('$ cd'):
        ## Back out one level 
        if line.split()[-1] == '..':
            cwd = '/'.join(cwd.split('/')[:-2]) + '/'

        ## cd into a dir
        else:
            cwd += '%s/' % line.split()[-1]

    ## Add dir
    elif line.startswith('dir'):
        dir_name = cwd + line.split()[1]
        lsof.append((0, dir_name + '/'))

    ## Add file
    elif line.split()[0].isdigit():      
        file_name = cwd + line.split()[1]
        lsof.append((line.split()[0], file_name))

dirs = []
for row in lsof:
    print(row)
    if row[0] == 0:
        dirs.append(row[1])

used_space = 0
for _file in lsof:
    used_space += int(_file[0])

free_space = 70000000 - used_space #28587170
need_space = 30000000 - free_space # 1412830

dir_sizes = []

for _dir in dirs:
    total  = 0 
    for _file in lsof:
        if _file[1].startswith(_dir):
            total += int(_file[0])

    dir_sizes.append( (total, _dir) )

dir_sizes.sort(key = lambda _: int(_[0]))

for _dir in dir_sizes:
    if _dir[0] >= need_space:
        print('dir: %s, size: %s' % (_dir[1], _dir[0]))
        break
