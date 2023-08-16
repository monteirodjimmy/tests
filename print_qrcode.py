import qrcode as qr
import subprocess
import cv2

#sn = str(subprocess.call(['sudo', 'dmidecode', '-s', 'system-serial-number' ]))
sn = subprocess.run('wmic bios get serialnumber',capture_output=True,text=True)
sn = str(sn.stdout)
print (sn[15:25])
sn = sn[15:25]
image = qr.make(sn)

#formatando o qrcode
# Data to encode
 
#Creating an instance of QRCode class
qr_sn = qr.QRCode(version = 1, box_size = 25,  border = 3)
 
#Adding data to the instance 'qr'
qr_sn.add_data(sn)
 

qr_sn.make(fit = True)

image2 = qr_sn.make_image( fill_color=(55, 95, 35),back_color=(255, 195, 235))

path = r'C:\Users\mateus.rodrigues\Documents\AFT Chromebook\check_label_static\serial_number_qrcode.png'
path_2 = r'C:\Users\mateus.rodrigues\Documents\AFT Chromebook\check_label_static\serial_number_qrcode_colorido.png'
#------------------------

image.save(path)
image2.save(path_2)

  
# Reading an image in default mode
image = cv2.imread(path)
image2 = cv2.imread(path_2) 
# Window name in which image is displayed
window_name = 'Qr'
window_name_2 = 'colorido'
  
# Using cv2.imshow() method
# Displaying the image
cv2.imshow(window_name, image)
cv2.imshow(window_name, image2)
  
# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)
  
# closing all open windows
cv2.destroyAllWindows()

# Data to encode