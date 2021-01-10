# -*- coding:utf-8 -*-

from subprocess import Popen
 
proceso = Popen(['ls', '-lha'])
proceso.wait()

# proceso2 = Popen(['clear'])
# proceso2.wait()


