# Programming for Everybody (Getting Started with Python) Last Assignment
'''
largest = None
smallest = None
numlist=[]
while True:
    try:
        num = input("Enter a number: ")
        if num != "done":
            num=int(num)
            numlist.append(num)
        elif num == "done":
            break
        
    except:
         print("Invalid input")



largest=max(numlist)
smallest=min(numlist)
print("Maximum is", largest)
print("Minimum is", smallest)
'''
'''
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname,'r')
for i in fh:
    i=i.rstrip()
    print(i)
'''

#Python Data Structures 3주 차
'''
total=0
count=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        l=line[line.find(':')+1:]
        total += float(l)
        count+=1
value=total/count

print(value)
'''
#Python Data Structures 4주 차
'''
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    line=line.split()
    lst.append(line)
lst=lst[0]+lst[1]+lst[2]+lst[3]
lst.sort()
lst=list(set(lst))
print(lst)
'''
'''
fname = input("Enter file name: ")
fh = open(fname)
count = 0
mail=[]
for line in fh:
    if not line.startswith("From"): continue
    elif line.startswith("From:"): continue
    else:
        line=line.split()
        mail.append(line[1])
        count+=1
        print(line[1])
print("There were", count, "lines in the file with From as the first word")
'''

name = input("Enter file name: ")
f = open(name)
mail=dict()
for line in f:
    if not line.startswith("From"): continue
    elif line.startswith("From:"): continue
    else:
        email=line.split()
        emailline=email[1]
        mail[emailline]=mail.get(emailline,0)+1
        print(mail)
bigcount=None
bigemail=None
for email,count in mail.items():
    if bigcount==None or count>bigcount:
        bigcount=count
        bigemail=email
print("{0} {1}".format(bigcount,bigemail))