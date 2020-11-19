f = open('log1.txt', 'r')

datalist = f.readlines()
for i in datalist:
    split_list = i.split(",")
    if("-" in i):
        print(split_list[1])
f.close()
