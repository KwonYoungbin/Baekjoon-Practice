croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
string = input()

for i in croa:
    string = string.replace(i,'*')
        
print(len(string))