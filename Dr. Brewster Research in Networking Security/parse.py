# Description: Used to parse a JSON File line by line and remove improper formats such as extraenous commas
# Technologies used: JSON, Python


i=x=0
list = []
file = []
# Get the line where there is a bracket

for line in open('5432.json', 'r'):
    file.append(line)
    i +=1
    if '}' in line:
        list.append(i)


print(file[1])
#
# for i in range(0, len(list)-1):
#     x = ""
#     if i == 0:
#         i = 1
#         print('no')
#         print(str(list[0]) + ' commas' + str(file[list[0]]))
#     elif file[list[i-1]].find(","):
#         print(str(list[i-1]) + ' commas' + str(file[list[i+1]]))

    # for list in open('5432.json', 'r'):
    #     if ',' in (list-1):
    #         print("BAD")
# with open('5432.json', 'r') as input:
#     line = input.readlines()
#     for line in input:
#         if brack in line:
#             print("YES")
#             break
#     input.close()
