import qrcode as qr
import subprocess
import cv2

sn = str(subprocess.call(['sudo', 'dmidecode', '-s', 'system-serial-number' ]))
print (sn)
image = qr.make(sn)
type(image)  # qrcode.image.pil.PilImage
image.save("serial_number_qrcode.png")

#tentando sem salvar o arquivo, usando o que esta atriburido por = qr.make('PXF005')


# path
path = r'/home/jimmy/Desktop/Pytho Projects/serial_number_qrcode.png'
  
# Reading an image in default mode
image = cv2.imread(path)
  
# Window name in which image is displayed
window_name = 'Qr'
  
# Using cv2.imshow() method
# Displaying the image
cv2.imshow(window_name, image)
  
# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)
  
# closing all open windows
cv2.destroyAllWindows()
