T=int(input())

for x in range(0,T):

    a=input().split()
    b=input().split()
    c=input().split()
    d=input().split()
    e=input().split()

    f=input().split()

    g=[a[0],b[0],c[0],d[0],e[0]]
    h=[a[1],b[1],c[1],d[1],e[1]]
    i=[a[2],b[2],d[2],e[2]]
    j=[a[3],b[3],c[3],d[3],e[3]]
    k=[a[4],b[4],c[4],d[4],e[4]]

    l=[a[0],b[1],d[3],e[4]]
    m=[a[4],b[3],d[1],e[0]]
    n=[a[0],a[4],e[0],e[4]]

    c.remove(c[2])

    for y in range(0,75):
        try:
            a.remove(f[y])
        except:
            pass
        try:
            b.remove(f[y])
        except:
            pass
        try:
            c.remove(f[y])
        except:
            pass
        try:
            d.remove(f[y])
        except:
            pass
        try:
            e.remove(f[y])
        except:
            pass
        try:
            g.remove(f[y])
        except:
            pass
        try:
            h.remove(f[y])
        except:
            pass
        try:
            i.remove(f[y])
        except:
            pass
        try:
            j.remove(f[y])
        except:
            pass
        try:
            k.remove(f[y])
        except:
            pass
        try:
            l.remove(f[y])
        except:
            pass
        try:
            m.remove(f[y])
        except:
            pass
        try:
            n.remove(f[y])
        except:
            pass        
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(g)==0 or len(h)==0 or len(i)==0 or len(j)==0 or len(k)==0 or len(l)==0 or len(m)==0 or len(n)==0:
            print(y+1)
            break
        
            



