from collections import defaultdict

def pre(val):
    global preorder
    if val == '.':
        return
    
    preorder += val
    pre(dic[val][0])
    pre(dic[val][1])

def inor(val):
    global inorder
    if val == '.':
        return
    
    inor(dic[val][0])
    inorder += val
    inor(dic[val][1])
    
def post(val):
    global postorder
    if val == '.':
        return
    
    post(dic[val][0])
    post(dic[val][1])
    postorder += val

N = int(input())
dic = defaultdict(list)

preorder = ''
inorder = ''
postorder = ''

for _ in range(N):
    root, left, right = input().split()
    dic[root].append(left)
    dic[root].append(right)
    
pre('A')
inor('A')
post('A')

print(preorder)
print(inorder)
print(postorder)