# -*- coding: utf-8 -*-

import webbrowser
from ftplib import FTP 

# webbrowser.open_new_tab("http://www.seritium.es")

ftp = FTP() 
ftp.connect('ftp.uniovi.es', 21, -999) 
ftp.login('', '') 
print ftp.getwelcome() 
print ftp.dir()
ftp.close()
