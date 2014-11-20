import os

os.system('python setup.py install')
path = os.getcwd()
# We set a soft link called "vmController" at the /usr/bin pointing to the vmController.py.
# If vmController.py is moved, the soft link need to be set again.
os.chdir('/usr/bin')
os.system('sudo ln -s ' + path + '/vmController/vmController.py vmController')

