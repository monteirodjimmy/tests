# Copyright 2012 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.


import os
import re
import codecs
import enum
import logging
import numbers
import os
import queue
import random
import uuid
from cros.factory.test.i18n import _
from cros.factory.test import session
from cros.factory.test import test_case
from cros.factory.test import test_ui
from cros.factory.test.utils import evdev_utils
from cros.factory.test.utils import touch_monitor
from cros.factory.utils.arg_utils import Arg
from cros.factory.utils import process_utils
from cros.factory.external.py_lib import evdev
#---------------------------necessarias-------------------------------------------

import qrcode as qr #biblioteca necessária que esteja na imagem de teste da máquina
import time

from cros.factory.test import device_data #biblioteca que da acesso ao serial number
from cros.factory.test import test_case #biblioteca presete na maioria dos testes
from cros.factory.test import test_ui #biblioteca com funções específicas para manibular a interface GUI do Google Chromium OS Factory Software Platform
from cros.factory.utils.arg_utils import Arg #Biblioteca que permite definir argumentos no JSON




class CheckLabel (test_case.TestCase):
 # 
  ARGS = [
      Arg('qr_color', str,
          'Touchpad input event id or evdev name. The test will probe'
          ' for event id if it is not given.', default="black")]
  

  def setUp(self):
    # Initialize properties
    #Getting the serial_number usig the Google Chromium OS Factory Software Platform lib devive_data

    sn = device_data.GetSerialNumber('serial_number')

    """Creating a  QR to save on _static folder of the test """

    #Is necessary to use the class QRCOde for more control 
    qr_sn =  qr.QRCode (version = 1, box_size = 25,  border = 4) #variável para armazenar o sn no qrcode a ser manipulado pela biblioteca QRCode
    #Adding data to the instance 'qr'
    qr_sn.add_data(sn)
    #This method with (fit=True) ensures that the entire dimension of the QR Code is utilized, even if the input data could fit into less number of boxes
    qr_sn.make(fit = True)

    image= qr_sn.make_image( fill_color=self.args.qr_color,back_color="white")

    path_image = r'/usr/local/factory/py/test/pytests/check_label_static/serial_number_qrcode.png'  #caminho para o qrcode gerado pelo método qr.make()
    #path_image = r'/usr/local/factory/py/test/pytests/serial_number_qrcode.png'  #caminho para o qrcode gerado pelo método qr.make()

    image.save(path_image)
    self.fullscreen = True
    self.ui.ShowElement('qr_image')


  
  def runTest(self):

    
    self.ui.WaitKeysOnce(test_ui.SPACE_KEY)
    self.ui.HideElement('qr_image')
    self.template.SetState('<h1 style="color:green;font-size:50px;font-family:arial"> PASS</h1>')
    self.Sleep(5)
    self.PassTask()
