##  Rod cutting...

##  The bad way...
def cutRodBadWay(p,n):
    if n==0:
        return 0
    q=0
    for i in range(1, n):
        q=max(q,p[i]+cutRodBadWay(p[:n-i],n-i))
    return q

def memoizedCutRodAux(p,n,r):
    if r[n]>=0:
        return r[n]
    q=0
    for i in range(1,n+1):
       q=max(q,p[i]+memoizedCutRodAux(p,n-i,r))
    r[n]=q
    return q

def memoizedCutRod(p,n):
    q=0
    r=[-1 for i in range(1,len(p))]
    r[0]=0
    for i in range(1,len(p)):
        q=max(q,p[i]+memoizedCutRodAux(p,n-i-1,r))
    return q

def bottomUpCutRod(p,n):
    r=[-1 for i in range(n)]
    r[0]=0
    for i in range(1,n):
        q=0
        for j in range(1,i+1):
            q=max(q,p[j]+r[i-j])
        r[i]=q
    return r[-1]

##  Input must have a zero (or anything) as the 0th index...
p=[0,1,5,8,9,11,13,16,18,20,25]
print('Costs are as the following: {}'.format(p[1:]))
#best_cost=cutRodBadWay(p,len(p))
#best_cost=memoizedCutRod(p,len(p))
best_cost=bottomUpCutRod(p,len(p))
print(best_cost)