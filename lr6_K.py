key=input("Input key \n")
f=open('text.txt')
text=f.read()
f.close()
text=text.replace(' ', '')
text=text.replace('\n', '')
text=text.lower()
alphabet="abcdefghijklmnopqrstuvwxyz";
def longKey(key,text):
    return key*int(len(text)/len(key))+key[0:len(text)%len(key)]
key=longKey(key,text)
chip_text=""
for i in range(len(text)):
    chip_text+=alphabet[(alphabet.index(text[i])+int(key[i]))%(len(alphabet) - 1)]
f=open("code.txt","w")
f.write(chip_text)
f.close()
print(chip_text)
