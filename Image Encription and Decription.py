def encript(image):
    file=open(image,"rb")
    image=file.read()
    file.close()
    image=bytearray(image)
    key=int(input("Enter a key value: "))
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
    key=int(input("Enter the key : "))
    for i,j in enumerate(image):
        image[i]=j^key
    en=open("decripted.jpg","wb")
    en.write(image)
    en.close()

i=input("Enter e for encription or d for decription: ")
if i=="e":
    image=input("Enter the filename which is to be encripted:")
    encript(image)
    print("Encripted successfully!!!")
else:
    decript()
    print("Decripted successfully!!!")
