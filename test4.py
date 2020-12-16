from PIL import Image
img = Image.open('MissingBits.png')
w,h = img.size
bindata=""
for y in range(h):
    for x in range(w):
        currentpixel = img.getpixel((x,y))
        if (currentpixel == (0,0,0)):
            bindata += "0"
        else:
            bindata += "1"
print(bindata)
