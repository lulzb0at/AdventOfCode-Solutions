with open('input.txt','r') as fh: lines = fh.read()

cwd = '/'
lsof = []

for line in lines.splitlines()[1:]:
    if line.startswith('$ cd'):
        if line.split()[-1] == '..':
            cwd = '/'.join(cwd.split('/')[:-2]) + '/'
        else:
            cwd += '%s/' % line.split()[-1]
    elif line.startswith('dir'):
        dir_name = cwd + line.split()[1]
        lsof.append((0, dir_name + '/'))
    elif line.split()[0].isdigit():      
        file_name = cwd + line.split()[1]
        lsof.append((line.split()[0], file_name))

dirs = []
for row in lsof:
    print(row)
    if row[0] == 0:
        dirs.append(row[1])

ans = 0 
for _dir in dirs:
    total  = 0 
    for _file in lsof:
        if _file[1].startswith(_dir) and _file[0] != 0:
            total += int(_file[0])

    if total < 100000:
        ans+= total

print(ans)
