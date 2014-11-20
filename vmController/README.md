vmController
====================

# Description

The vmController is a set of python libraries that allow users to control VMware fusion by CLI.
User can start, stop, restart, pause, unpause and suspend the current running VMware. As well, user can send files from local machine to virtual machine.


# Installation

## Environment

Required

* Python 2.7+
* [setuptools package](https://pypi.python.org/pypi/setuptools)

## Downloading

Option A:

If you have git installed, clone the repository

    git clone https://github.com/datacenter/acitoolkit.git

Option B:

If you don't have git, [download a zip copy of the repository](https://github.com/datacenter/utils/archive/master.zip) and extract.


## Installing

After downloading, move it to your favor location before installing it. Then: 

    cd <path-to-vmController>
    sudo python install.py

# Usage
To run the script, try:
 
    vmController <virtual-machine-ip-address> <user-in-the-virtual-machine> <password>

Once you have started running the script, you can always use "tab" button to see what commands are available.

# License

Copyright 2014 Cisco Systems, Inc.
