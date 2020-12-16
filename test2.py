import qrcode
from PIL import Image
img = qrcode.make("ispclub{It'5_n0t_345y}")
img.save('qr.png')
