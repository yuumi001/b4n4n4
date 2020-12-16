from PIL import Image
import base64
with open('qr.png','rb') as qrimg:
    qrdata = qrimg.read()
with open('MissingBits.png','rb') as mbimg:
    mbdata = mbimg.read()
mbdatarev = mbdata[::-1]
with open('newimg.png','wb') as newimg:
    newimg.write(qrdata+mbdatarev)
with open('newimg.png','rb') as test:
    testdata = test.read()
with open('test.png','wb') as testimg:
    testimg.write(testdata[::-1])
