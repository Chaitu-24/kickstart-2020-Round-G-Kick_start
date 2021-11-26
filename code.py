n=int(input())
for j in range(0,n):
    name=input()
    l=len(name)
    k=0
    final=0
    for i in range(0,l):
        if name[i:i+4]=="KICK":
            k+=1
        if name[i:i+5]=="START":
            final+=k
    print(f"Case #{j+1}: {final}")
