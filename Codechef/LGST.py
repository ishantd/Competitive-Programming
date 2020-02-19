
n = input()
q = input()
d = []
    
for i in range(int(n)):
    ele = input()
    d.append(ele)
    
for i in range(int(q)):
    check = input()
    count = 0
    for k in range(int(n)):
        if check >= d[k]:
            count = count+1
    print(count)