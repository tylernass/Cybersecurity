params = [] # from json-transforms file

list = []

ftag = [] # list with tag
fline = [] # list with line numbers

final = []
i=k=0

# Check for line in ftag



check = None

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

def iter(line, j):
    for k in range(j+1, len(line)):
        if line[k] == '"':
            chck(line, j, k)
            if(chck(line, j, k) == 1):
                fline.append(line[0:len(line)-1])
                # print(fline[k])
                # print(line[(j+1): (k)])
                # print('bad')
                break
            else:
                break


def chck(line, j, k):
    z = line[(j+1): (k)]
    b = line[(j+1): (k+1)]
    check = 0
    for a in range(0, len(ftag)):
        # print(a)
        if z == ftag[a]:
            check = 1
        # else:
        #     check = 0
        a += 1
    return check

with open('5432-3pkts.json', 'r') as g:
    lines = g.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        for j in range(0, len(line)):
            if line[j] == '"':
                iter(line, j)
                break

a=0
for x in range(0, len(params)):
    for y in range(0, len(list)):
        if(list[y] == params[x]):
            a += 1

# TODO Exclusion rule defined in JSON-filtering.pdf
# Create a function open
# Count the number for '{' parenthese
# Create a for loop that appropriately adds those parnetheses
# This is where the work needs to be done
# Store the closed brackets originally after opening bracket

def opn():
    frwd = 0
    c = 0
    # for a in range(0, len(fline)):
    #     for b in range(0, len(fline[a])):
    #         if fline[a][b] == '{':
    #            frwd += 1
    with open('Corrected-5432--3pkts-out.json', 'w') as f:
        for i in range(0, len(fline)-1):
            # for j in range(0, len(fline[i])):
                x = any(i in ',{' for i in fline[i])
                if fline[i][6:11] == "index":
                        f.write("{\n")
                        f.write(fline[i] + "\n")
                if x == False:
                    c += 1
                    f.write(fline[i])
                    f.write('\n')
                    f.write("        },\n")
                    print(i)
                if fline[i+1][6:11] == "index" and fline[i+2][6:11] != "index":
                    f.write('\n')
                    f.write("  }\n\n")
                elif x == True:
                    f.write(fline[i] + '\n')


