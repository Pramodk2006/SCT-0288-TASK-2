def encript(image):
    file=open(image,"rb")
    image=file.read()
    file.close()
    image=bytearray(image)
    key=int(input())
    for i,j in enumerate(image):
        image[i]=j^key
    en=open("encripted.jpg","wb")
    en.write(image)
    en.close()
def decript():
    file=open("encripted.jpg","rb")
    image=file.read()
    file.close()
    image=bytearray(image)
    key=int(input())
    for i,j in enumerate(image):
        image[i]=j^key
    en=open("decripted.jpg","wb")
    en.write(image)
    en.close()
image=input("Enter the filename which is to be encripted:")
i=input()
if i=="e":
    encript(image)
else:
    decript()