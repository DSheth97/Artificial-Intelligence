import copy
init=[[' ','5','2'],['1','8','3'],['4','7','6']]
goal=[['1','2','3'],['4','5','6'],['7','8',' ']]

def retindx(l,s):
    for m in range(len(l)):
        for n in range(len(l[m])):
            if l[m][n]==s:
                return [m,n]
            
def up(l,i,j):
    temp=copy.deepcopy(l)
    t1=l[i][j]
    t2=l[i-1][j]
    temp[i][j]=t2
    temp[i-1][j]=t1
    return(temp)

def down(l,i,j):
    temp=copy.deepcopy(l)
    t1=l[i][j]
    t2=l[i+1][j]
    temp[i][j]=t2
    temp[i+1][j]=t1
    return(temp)

def left(l,i,j):
    temp=copy.deepcopy(l)
    t1=l[i][j]
    t2=l[i][j-1]
    temp[i][j]=t2
    temp[i][j-1]=t1
    return(temp)

def right(l,i,j):
    temp=copy.deepcopy(l)
    t1=l[i][j]
    t2=l[i][j+1]
    temp[i][j]=t2
    temp[i][j+1]=t1
    return(temp)
  
def man(l):
  dist=0
  for i in range(len(l)):
    for j in range(len(l[i])):
      [m,n]=retindx(goal,l[i][j])
      [a,b]=retindx(l,l[i][j])
      dist=dist+abs(a-m)+abs(n-b)
  return(dist)

def ham(l):
  dist=0
  for i in range(len(l)):
    for j in range(len(l[i])):
      [m,n]=retindx(goal,l[i][j])
      [a,b]=retindx(l,l[i][j])
      if([m,n]!=[a,b]):
        dist=dist+1
  return(dist)

def astar(st,gl):
    q=[]
    i=0
    t=[]
    d=[]
    q.append(st)
    while(True):
        dictq={}
        newdict={}
        [j,k]=retindx(q[i],' ')
        if([j,k]==[0,0]):
            temp=right(q[i],j,k)
            t.append(temp)
            temp=down(q[i],j,k)
            t.append(temp)
            

        elif([j,k]==[0,len(q[0])-1]):
            temp=left(q[i],j,k)
            t.append(temp)
            temp=down(q[i],j,k)
            t.append(temp)

        elif([j,k]==[len(q[0])-1,0]):
            temp=right(q[i],j,k)
            t.append(temp)
            temp=up(q[i],j,k)
            t.append(temp)

        elif([j,k]==[len(q[0])-1,len(q[0])-1]):
            temp=left(q[i],j,k)
            t.append(temp)
            temp=up(q[i],j,k)
            t.append(temp)

        elif(j==0):
            temp=left(q[i],j,k)
            t.append(temp)
            temp=down(q[i],j,k)
            t.append(temp)
            temp=right(q[i],j,k)
            t.append(temp)

        elif(k==0):
            temp=up(q[i],j,k)
            t.append(temp)
            temp=down(q[i],j,k)
            t.append(temp)
            temp=right(q[i],j,k)
            t.append(temp)

        elif(j==len(q[0])-1):
            temp=left(q[i],j,k)
            t.append(temp)
            temp=up(q[i],j,k)
            t.append(temp)
            temp=right(q[i],j,k)
            t.append(temp)

        elif(k==len(q[0])-1):
            temp=left(q[i],j,k)
            t.append(temp)
            temp=up(q[i],j,k)
            t.append(temp)
            temp=down(q[i],j,k)
            t.append(temp)

        else:
            temp=left(q[i],j,k)
            t.append(temp)
            temp=up(q[i],j,k)
            t.append(temp)
            temp=down(q[i],j,k)
            t.append(temp)
            temp=right(q[i],j,k)
            t.append(temp)
            
        for ite in t:
          dist=ham(ite)
          d.append(dist)
        
        
        for ite in range(len(t)):
          ky=d[ite]
          vl=t[ite]
          if ky not in dictq:
            dictq[ky]=[vl]
          else:
            dictq[ky].append(vl)
          
        for ite in sorted(dictq.keys()):
          newdict[ite]=dictq[ite]
          
        s=0
        
        if(bool(newdict)==False):
          i=i+1
        else:
          for ite in newdict:
            for obj in newdict[ite]:
              if obj not in q:
                q.insert(s,obj)
                s=s+1
          
        d=[]
        t=[]
        print(q[i])
        if q[i] == gl:
            break 
        #i=i+1
           
astar(init,goal)

    
