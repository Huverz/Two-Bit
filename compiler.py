import random
import sys
import math

Array=[]
Output=[]
pushed=0

got=sys.stdin.readlines()

blah=0
for char in got:
    blah+=1
    if char.isdigit():
        char=int(char)
    if blah==1:
        pushed=char
    else:
        Array.append(char)

f=open("bank1.txt","r")
bank1=f.read()
f.close()
commands1=bank1.split("0")
print commands1


def nextarg(a,b):
    c=commands1[a+b:]#define the next sequence
    
    if c[0:1:]=='33':#check for simple number declaration, and return number if true
        del c[0,1]
        return int(c+1,3),a

    elif c=='32':#check for taking value from Array
        return Array[nextarg(c+b,1)],a

    elif c=='132':#randomize between next and 2nd
        return random.randint(nextarg(c+b,1),nextarg(c+b,2)),a

    elif c=='223':#gives pushed for use in nexts
        return pushed,a

    elif c=='311':#randomized between pushed and next
        if pushed<nextarg(a+b,1):
            return random.randint(pushed,nextarg(a+b,1)),a
        return random.randint(nextarg(a+b,1),pushed),a

    elif c=='312':#random truthy/falsy value
        return random.randint(0,1),a

    else:
        sys.stderr.write("POSSIBLE ERROR: Line " + str(linenum) + " command " + str(pos) + ", has insufficient arguments, using pushed")
        return pushed,a-1


def add(a,b,c,d):#Adds pushed to next, if there is no next, simply doubles pushed
    e,f=nextarg(a,1)
    return f+2, b+e, c, d

def subtract(a,b,c,d):#Subtracts next from pushed, pushes zero if no next
    e,f=nextarg(a,1)
    return f+2, b-e, c, d

def divide(a,b,c,d):#Divides pushed by next, pushes one if no next
    e,f=nextarg(a,1)
    return f+2, b/e, c, d

def multiply(a,b,c,d):#Multiplies pushed by next, pushed pushed squared if no next
    e,f=nextarg(a,1)
    return f+2, b*e, c, d

def Arrayreplace(a,b,c,d):#Replace the (next)th thing in array with the (2nd) thing
    c[nextarg(a,1)],f=nextarg(a,2)
    return f+3,b,c,d

def primecheck(a,b,c,d):#Returns 1 if prime, 0 if not
    for x in range((b/2)+1):
        for y in range((b/2)+1):
            if x*y==b:
                return a+1,0,c,d
    return a+1,1,c,d

def equalif(a,b,c,d):#Returns 1 if (next) and (2nd) are equal, otherwise 0
    e,f=nextarg(a,1)
    g,h=nextarg(f,2)
    if g==e:
        return a+3,1,c,d
    return h+3,0,c,d

def notequalif(a,b,c,d):#Returns 1 if (next) and (2nd) are not equal, otherwise 0
    e,f=nextarg(a,1)
    g,h=nextarg(f,2)
    if g!=e:
        return a+3,1,c,d
    return h+3,0,c,d

def greaterif(a,b,c,d):#Returns 1 if (next) is greater than (2nd), otherwise 0
    e,f=nextarg(a,1)
    g,h=nextarg(f,2)
    if g>=e:
        return a+3,1,c,d
    return h+3,0,c,d

def lesserif(a,b,c,d):#Returns 1 if (next) is less than (2nd), otherwise 0
    e,f=nextarg(a,1)
    g,h=nextarg(f,2)
    if g<=e:
        return a+3,1,c,d
    return h+3,0,c,d

def Arraycheck(a,b,c,d):#Pushes the (next) item in Array
    e,f=nextarg(a,1)
    return f+2,Array[e],c,d

def cube(a,b,c,d):#Pushes the cube of pushed
    return a+1,b**3,c,d

def nthpower(a,b,c,d):#Pushes the (next) power of pushed
    e,f=nextarg(a,1)
    return f+2,b**e,c,d

def nthroot(a,b,c,d):
    e,f=nextarg(a,1)
    return f+2,b**(1./e),c,d

def donextiftrue(a,b,c,d):#Does the next command only if the input isn't 0
    if b==0:
        a+=2
    else:
        a+=1
    return a,b,c,d

def sqroot(a,b,c,d):#Pushes the sqare root of pushed
    return a+1,b**(1./2),c,d

def cubroot(a,b,c,d):#pushes the cubic root of pushed
    return a+1,b**(1./3),c,d

def factorial(a,b,c,d):#pushes the factorial of pushed
    for x in range(b-1):
        b*=x
    return a+1,b,c,d

def rand2num(a,b,c,d):#Pushes a random integer between the next two numbers
    e,f=nextarg(a,1)
    g,h=nextarg(f,1)
    if e>g:
        return h+3,randint(e,g),c,d
    return h+3,randint(g,e),c,d

def pushnext(a,b,c,d):#Pushes (next)
    e,f=nextarg(a,1)
    return f+2,e,c,d

def Arrayempty(a,b,c,d):
    return a+1,b,[],d

def sine(a,b,c,d):
    return a+1,math.degrees(math.sin(b)),c,d

def cosine(a,b,c,d):
    return a+1,math.degrees(math.cos(b)),c,d

def tangent(a,b,c,d):
    return a+1,math.degrees(math.tan(b)),c,d

def increment(a,b,c,d):
    return a+1,b+1,c,d

def outputnext(a,b,c,d):
    e,f=nextarg(a,1)
    c.append(e)
    return f+2,b,c,d

def outputpushed(a,b,c,d):
    c.append(b)
    return a,b,c,d

def clearOut(a,b,c,d):
    return a,b,[],d

def reallybignum(a,b,c,d):
    b=9e9999999
    for a in range(9e99999999):
        b=b**b
    return a+1,b,c,d

def boolrand(a,b,c,d):
    return a+1,randint(0,1),c,d

def fibdex(a,b,c,d):
    e,f=nextarg(a,1)
    fib=[0,1]
    while len(fib)<e:
        fib.append(fib[len(fib)-1]+fib[len(fib)]-2)
    b=fib[len(fib)]
    return f+1,b,c,d

def pushArr0(a,b,c,d):
    return a+1,d[0],c,d

def makeArr0pushed(a,b,c,d):
    d[0]=b
    return a+1,b,c,d

def primefactor(a,b,c,d):
    n=b
    b=[]
    d=2
    while d*d<=n:
        while n%d==0:
            b.append(d)
            n//=d
        d+=1
    if n>1:
       b.append(n)
    return a+1,b,c,d

commands_mapping = {
    '1':add, '2':subtract, '3':multiply,
    
    '11':divide, '12':Arrayreplace, '13':primecheck,
    '21':equalbool, '22':notequalbool, '23':greaterbool,
    '31':lesserbool, '32':Arraycheck,
    
    '111':donextiftrue, '112':cube, '113':nthpower,
    '121':nthroot, '122':sqroot, '123':cubroot,
    '131':factorial, '132':rand2num, '133':pushnext,
    '211':Arrayempty, '212':sine, '213':cosine,
    '221':tangent, '222':increment, '223':outputnext,
    '232':outputpushed, '233':clearOut,
    '311':reallybignumber, '312':boolrand, '313':fibdex,
    '321':pushArr0, '322':makeArr0pushed, '323':primefactor,
}

def commandrun(comm,pos,pushed,Array,Output):
    return commands_mapping[comm](pos,pushed,Array,Output)

pos=0

while pos <= len(commands1):
    pos,pushed,Array,Output=commandrun(commands1[pos],pos,pushed,Array,Output)


if len(Output)>0:
    for x in Output:
        sys.stdout.write(str(x))
else:
    sys.stdout.write(str(pushed))

