from PIL import Image
flag = 'ispclub{Dr4w_t0_th3_3Nd}'
fd = []
coordinate = [(12,16),(56,23),(98,78),(12,36),(65,45),(48,78),(45,32),(19,84),(84,98),(84,14),(15,35),(45,87),(15,65),(45,15),(46,15),(15,62),(12,98),(12,78),(12,65),(12,35),(23,65),(32,98),(45,98),(78,45)]
for i in flag:
    fd.append(ord(i))
print(fd)
print(coordinate)
img = Image.new('RGB',(100,100),'white')
for i in range(24):
    img.putpixel(coordinate[i],(fd[i],fd[i],fd[i]))
img.save('chall.png')
