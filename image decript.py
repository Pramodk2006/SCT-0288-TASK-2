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