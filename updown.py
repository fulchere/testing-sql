l = []
for i in range(10):
    l.append((i,i*2,i*i))

f = open("output.txt","w")
for item in l:
    f.write(str(item[0])+"\t"+str(item[1])+"\t"+str(item[2])+"\n")

f.close()
    
def get_list():
    l = []
    for i in range(100):
        l.append((i,i*2,i*i))
    return l
