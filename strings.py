x = 'hello'
y = "hello"


print(x == y)

for i in x:
    print(i)

# Remove extra spaces from a string
s = 'Hello   v musheer  khan         jjj jb j j j'
y=''
for i in range(len(s)):
    if s[i] == ' ' and s[i+1] == ' ':
        continue
    else:
        y += s[i]
#print(y)


print('Hello\b Musheer\f Khan Ahmad 1212')

print(x.maketrans('aeiou', '12345'))
