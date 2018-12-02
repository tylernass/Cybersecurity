params = [] # from json-transforms file

list = []
ln=[]
paren = []

ftag = [] # list with tag
fline = [] # list with line numbers

final = []
i=k=0


check = None

x = 0

def chck(line, i, j, k):
    z = line[(j+1): (k)]
    # for c in range(0, len(b)+1):
    #     if c == '}' or c == ',':
    #         print(c)
    #         end += 1

    # if end == 0:
    #     print(b)
    # print(k)
    # y = a[(j+1): (k)]
    # print(z)
    # print(y)

    for a in range(0, len(ftag)):
        # print(a)
        if z == ftag[a]:
            check = 1
        # else:
        #     check = 0
        a += 1
    return check

def iter(line, i, j):
    for k in range(j+1, len(line)):
        if line[k] == '"':
            chck(line, i, j, k)
            if(chck(line, i, j, k) == 1):
                fline.append(line[0:len(line)-1])
                # print(fline[k])
                # print(line[(j+1): (k)])
                # print('bad')
                break
            # if(chck(line, i, j, k) == 2):
            #     fline.append(line[0:len(line) - 2])
            # Detect line near end of object
            else:
                break
    # for k in range(0, len(line)):
    #     if line[k] == '}':
    #         print('1')


with open('5432-3pkts.json', 'r') as g:
    lines = g.readlines()
    for i in range(0, len(lines)):
        line = lines[i]

        ln.append(lines[i])
        for j in range(0, len(line)):
            # if line[j] == '}':
            #     print(i)
            if line[j] == '"':
                iter(line, i, j)
                break

with open('json-transforms.csv', 'r') as f:
    lines = f.readlines()
    # for line in lines:
    for i in range(1, len(lines)):
        line = lines[i]
        for j in range(0, len(line)):
            if line[j] == ',':
                ftag.append(line[:j])
                break
            else:
                j += 1
    f.close()

a=0
for x in range(0, len(params)):
    for y in range(0, len(list)):
        if(list[y] == params[x]):
            a += 1

with open('Corrected-5432--3pkts-out.json', 'w') as f:
    print(fline)
    for i in range(0, len(fline)):
        # Opening Brackets
        print(fline[i])
        if fline[i][0:] == '}' or ',':
            print(fline[i][0:])
        if fline[i][6:11] == "index":
            f.write("{\n")
            f.write(fline[i] + "\n")
        # Close brackets
        if fline[i][11:23] == "pgsql.status":
            f.write(fline[i] + "\n")
            f.write("}\n\n")
        # Normal write
        if fline[i][6:11] != "index" and fline[i][11:23] != "pgsql.status":
            f.write(fline[i] + "\n")

    f.close()
