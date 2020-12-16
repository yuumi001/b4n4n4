from PIL import Image
import math
with open('MissingBits.txt','r') as fd:
    data = fd.readline()

a = len(data)
a = math.sqrt(a)
a = math.ceil(a)
print (data)
data = data + '0'*(pow(a,2)-len(data))
print (data)
img = Image.new('RGB',size = (a, a), color = 'white')
height, width = img.size
i = 0
for y in range(height):
    for x in range(width):
        if (data[i]=='0'):
            img.putpixel((x, y),(0,0,0))
        i+=1
img.save('image.png')
