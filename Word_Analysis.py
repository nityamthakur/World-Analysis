f=open('rev1.txt','r')
vowel=0
con=0
up=0
low=0
reader=f.read()
v=['a','e','i','o','u']
c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
words=reader.split()
count=0
for i in words:
    count+=1

for i in reader:
    if i in v:
        vowel+=1
    if i in c:
        con+=1
    if i.isupper()==True:
        up+=1
    if i.islower()==True:
        low+=1
print(count,' total words')
print(vowel,' vowels')
print(con,' consonants')
print(up,' uppercase letters')
print(low,' lowercase letters')
