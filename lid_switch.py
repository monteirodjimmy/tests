# Copyright 2012 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Tests lid switch aterado para testes by Mateus Monteiro ."""

import datetime
import os
import time

from cros.factory.test import test_case
from cros.factory.test import test_ui


class LidSwitchTest(test_case.TestCase):
 # Será a futura class para exibir PASS or FAIL 
  def runTest(self):
    self.ui.SetState('<h1 style="font-size:60px;"><font color="green">PASS</font></h1>')
    self.ui.SetState('<h1 style="font-size:60px;"><font color="green">PASS</font></h1>')

"""
status = False

class PrintPass(test_case.TestCase):
  def statusFlag(self,status):
    if status:
      self.ui.SetState('<h1 style="font-size:60px;"><font color="green">PASS</font></h1>')
      
    else:
      self.ui.SetState('<h1 style="font-size:60px;"><font color="red">FAIL</font></h1>')
    self.Sleep(2)
"""

