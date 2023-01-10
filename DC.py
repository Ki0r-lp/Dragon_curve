def dc(t)->int: # dragon curve
    if t == 0 : return [1],1
    dl,od,t=[1],{1:0,0:1},t-1
    while t>0:
        dl.append(1)
        for i in dl[0:len(dl)-1][-1::-1]:
            dl.append(od[i])
        t-=1
    return dl