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


# Do all of the lines get passed in as they are supposed to? Yes
def chck(line, j, k):
    z = line[(j+1): (k)]
    # b = line[(k): (k)+1]
    # print(b)
    print(z)
    check = 0
    ###### THIS IS WHERE THE ERROR IS ####
    for a in range(0, len(ftag)):
        # print(a)
        # Where the error should be handled
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
        # print(line)
        for j in range(0, len(line)):
            if line[j] == '"':
                iter(line, j)
                break

a=0
for x in range(0, len(params)):
    for y in range(0, len(list)):
        if(list[y] == params[x]):
            a += 1

with open('Corrected-5432--3pkts-out.json', 'w') as f:
    for i in range(0, len(fline)):
        # Opening Brackets
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

# with open('json-transforms.csv', 'r') as f:
#     lines = f.readlines()
#     # for line in lines:
#     for i in range(1, len(lines)):
#         line = lines[i]
#         for j in range(0, len(line)):
#             if line[j] == ',':
#                 params.append(line[:j])
#                 break
#             else:
#                 j += 1
            # elif line[j] == ',':
            #     params.append(line[:j])
            #     print(i)
    # f.close()


# print(params)
    # line = lines
    # for i in range(0, len(params)):
    #     for x in range(0, len(list)):
    #         y = file[list[x] - 2]
    #         z = len(y)
    #         a = y[z - 2]
    #         # if x == 0:
    #         #     b = 2
    #         # else: b = list[x]
    #         # print(list[x])
    #         if a == comma:
    #             ntxt = file[list[x] - 2][0:(z - 2)]
    #             file[list[x] - 2] = ntxt
