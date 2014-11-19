import os

os.system('python setup.py install')
path = os.getcwd()
os.chdir('/usr/bin')
os.system('sudo ln -s ' + path + '/vmController/vmController.py vmController')

