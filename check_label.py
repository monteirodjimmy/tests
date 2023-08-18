# Copyright 2012 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.


import os
import logging

#---------------------------necessarias-------------------------------------------

import qrcode as qr #biblioteca necessaria que esteja na imagem de teste da maquina
import time

from cros.factory.test import device_data #biblioteca que da acesso ao serial number
from cros.factory.test import test_case #biblioteca presete na maioria dos testes
from cros.factory.test import test_ui #biblioteca com funcoes especificas para manibular a interface GUI do Google Chromium OS Factory Software Platform
from cros.factory.utils.arg_utils import Arg #Biblioteca que permite definir argumentos no JSON

_PASS_TEST_MESSAGE = '<h1 style="color:green;font-size:200px;font-family:arial">PASS</h1>'
_FAIL_TEST_MESSAGE = '<h1 style="color:red;font-size:200px;font-family:arial">FAIL</h1>'

class CheckLabel (test_case.TestCase):
 # 
  ARGS = [
      Arg('qr_color', str,
          'Parameter to change the color'
          ' if the color is not given', default="black"),
          Arg('timeout', int,
          'Parameter to change the timeout of the Pass ou Fail '
          ' if the timeout is not given', default=2),
          Arg('pass_key', str,
          'Parameter to choose the PASS key '
          ' if the Key is not set', default="Y"),
          Arg('fail_key', str,
          'Parameter to choose the FAIL key'
          ' if the Key is not set', default="F")
          ]
  

  def setUp(self):
    # Initialize properties
    #Getting the serial_number usig the Google Chromium OS Factory Software Platform lib devive_data

    sn = device_data.GetSerialNumber('serial_number')

    """Creating a  QR to save on _static folder of the test """

    #Is necessary to use the class QRCOde for more control 
    qr_sn =  qr.QRCode (version = 1, box_size = 25,  border = 2) #variavel para armazenar o sn no qrcode a ser manipulado pela biblioteca QRCode
    #Adding data to the instance 'qr'
    qr_sn.add_data(sn)
    #This method with (fit=True) ensures that the entire dimension of the QR Code is utilized, even if the input data could fit into less number of boxes
    qr_sn.make(fit = True)

    image= qr_sn.make_image( fill_color=self.args.qr_color,back_color="white")

    path_image = r'/usr/local/factory/py/test/pytests/check_label_static/serial_number_qrcode.png'  #path to the folder _static 

    image.save(path_image)
    self.ui.ShowElement('qr_image')
 
   
  
  def runTest(self):

    self.ui.BindKey(self.args.fail_key,self.OnFailPressed)
    self.ui.BindKey(self.args.pass_key,self.OnPassPressed)
    self.WaitTaskEnd()

  def OnFailPressed(self,event):
    self.ui.SetState(_FAIL_TEST_MESSAGE )
    self.Sleep(self.args.timeout)
    self.FailTask('Tags com avaria, tag errada ou falha ao lero QRCode')
  def OnPassPressed(self,event):
    self.ui.SetState(_PASS_TEST_MESSAGE)
    self.Sleep(self.args.timeout)
    self.PassTask()

