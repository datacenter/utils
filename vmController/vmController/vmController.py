#!/usr/bin/env python

from vmfusion import vmrun
from cmd import Cmd
import paramiko
import scp
import sys
import argparse
try:
    import readline
    # The following is required for command completion on Mac OS
    import rlcompleter
    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")
except:
    try:
        import pyreadline
    except:
        READLINE = False


class VmController(Cmd):

    def __init__(self, ip, user, password, vmx):
        Cmd.__init__(self)
        self.vmx = vmrun.list()['machines'][vmx] if type(vmx) == int else vmx
        self.ssh = None
        self.scp = None
        self.ip = ip
        self.user = user
        self.password = password
        self.file = None
        self.destination = None
        self.set_prompt()
        self.login_vm()

    def set_prompt(self):
        """
        Set the prompt to something like:
        VM@<ip_address>#
        """
        self.prompt = 'VM@'+self.ip+'$ '

    def login_vm(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, username=self.user, password=self.password)
        self.scp = scp.SCPClient(self.ssh.get_transport())

    def do_start(self, *args):
        " to start your virtual machine "
        vmrun.start(self.vmx)

    def do_stop(self, *args):
        " to stop your virtual machine "
        vmrun.stop(self.vmx)

    def do_reset(self, *args):
        " to reset your virtual machine "
        vmrun.reset(self.vmx)

    def do_suspend(self, *args):
        " to suspend your virtual machine "
        vmrun.reset(self.vmx)

    def do_pause(self, *args):
        " to pause your virtual machine "
        vmrun.pause(self.vmx)

    def do_unPause(self, *args):
        " to unpause your virtual machine "
        vmrun.unpause(self.vmx)

    def do_sendFile(self, args):
        """
        Send a file from local machine to the virtual machine
        Usage: sendFile <file-in-your-local-machine> <destination-in-the-virtual-machine>
        """
        args = args.strip().split(' ')
        if len(args) != 2:
            if args==['']:
                args=[]
            print ('do_sendFile() takes exactly 2 arguments (%s given).' % len(args))
            sys.exit()
        self.file = args[0]
        self.destination = args[1]
        self.scp.put(self.file, self.destination)

    def do_exit(self, args):
        " Exit the command mode "
        return -1

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Send a file from local machine to virtual machine.')
    parser.add_argument('ip_address', help='IP Address of the virtual machine.')
    parser.add_argument('user', help='User account in the virtual mathince.')
    parser.add_argument('password', help='Password that associates with the account.')
    parser.add_argument('-v', '--vmx', default=0, help='The virtual system that running in VMware Fusion. It could be an integer or the vmx of the virtual machine.')

    args = parser.parse_args()

    VC = VmController(args.ip_address, args.user, args.password, args.vmx)
    VC.cmdloop()