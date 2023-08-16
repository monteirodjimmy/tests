# Copyright 2012 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import subprocess # bibliotetea muito provavelmente nativa do python3
import qrcode as qr #biblioteca necessária que esteja na imagem de teste da máquina
import time


from cros.factory.test import test_case #biblioteca presete na maioria dos testes
from cros.factory.test import test_ui #biblioteca com funções específicas para manibular a interface GUI do Google Chromium OS Factory Software Platform



sn = subprocess.run(['factory', 'device-data','|' ,'grep' , 'serial_number ' ]) #O comando shell factory deve está funcionado e ser nativo do Google Chromium OS Factory Software Platform
subprocess.check_output(['factory', 'device-data']).decode("utf-8") 
sn = str(sn.stdout) #obriga a saida do subprocess.run a ser convertida para string
print (sn.stdout)
sn = sn[13:]
image_1 = qr.make(sn)

#Is necessary to use the class QRCOde for more control 
qr_sn =  qr.QRCode (version = 1, box_size = 25,  border = 3) #variável para armazenar o sn no qrcode a ser manipulado pela biblioteca QRCode
#Adding data to the instance 'qr'
qr_sn.add_data(sn)
#This method with (fit=True) ensures that the entire dimension of the QR Code is utilized, even if the input data could fit into less number of boxes
qr_sn.make(fit = True)

image_2 = qr_sn.make_image( fill_color=(55, 95, 35),back_color=(255, 195, 235))

path_image_1 = r'/usr/local/factory/py/test/pytests/check_label_static/serial_number_qrcode_1.png' #caminho para o qrcode gerado pelo métido qr.make()
path_image_2 = r'/usr/local/factory/py/test/pytests/check_label_static/serial_number_qrcod_2.png'  #caminho para o qrcode gerado pelo método qr.make()

image_1.save(path_image_1)
image_2.save(path_image_2)

class CheckLabel (test_case.TestCase):
 # 
  def runTest(self):
    self.ui.SetState('<img src = "usr/local/factory/py/test/pytests/check_label_static/serial_number_qrcode_1.png" alt="Error: QRcode Not Found" width="500" height="500">')
    #self.ui.SetState('<img src = "usr/local/factory/py/test/pytests/check_label_static/serial_number_qrcode_2.png" alt="Error: QRcode Not Found" width="500" height="500">')

    self.Sleep(20)