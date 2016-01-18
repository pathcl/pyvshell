#!/usr/bin/env python
"""
Little class around cmd module
"""
import cmd
import os

from lib import vmware


class PyvShell(cmd.Cmd):
    """
    We'll create an object named PyvShell
    """

    prompt = '>>> '
    intro = '''
    Welcome to PyvShell. Please type 'help' in order to view all available.\t
    For example:

    >>> help
    >>> help ls
    '''

    def do_ls(self, line):
        """
        Get all VM's on vCenter or ESXi.
        It will ask you an username and valid password.
        Usage example and output:

        >>> ls esxi.domain.tld
        Please enter your username: root
        Password:
        ----------------------------------------------------------------------
        Name:                    syslog02.domain.tld
        Instance UUID:           523589d3-60fd-b49a-0dc1-c66b0b42b394
        CPUs:                    2
        MemoryMB:                4096
        Guest PowerState:        running
        Guest Full Name:         Ubuntu Linux (64-bit)
        Guest Container Type:    ubuntu64Guest
        Container Version:       vmx-07
        **********************************************************************
        You have a total of 1 VM in esxi.domain.tld

        """
        vmware.ls(line)

    def do_stop(self, line):
        """
        >>> stop someesxi.domain.tld
        Please enter your username: root
        Password:
        You're connected to someesxi.domain.tld
        ----------------------------------------------------------------------
        Hosts available here:

        DC0_C0_H0
        DC0_C0_H1
        DC0_C0_H2
        DC0_C0_H3
        DC0_C0_H4
        DC0_C0_H5
        DC0_C0_H6
        DC0_C0_H7
        DC0_C1_H0
        DC0_C1_H1
        DC0_C1_H2
        DC0_C1_H3
        DC0_C1_H4
        DC0_C1_H5
        DC0_C1_H6
        DC0_C1_H7
        ----------------------------------------------------------------------
        Host regex?: DC0_C1.*
        Powered off/total (vcenter) VirtualMachines:  |################| 48/48

        """
        vmware.stop(line)

    def do_start(self, line):
        """
        >>> start someesxi.domain.tld
        Please enter your username: root
        Password:
        You're connected to someesxi.domain.tld
        ----------------------------------------------------------------------
        Hosts available here:

        DC0_C0_H0
        DC0_C0_H1
        DC0_C0_H2
        DC0_C0_H3
        DC0_C0_H4
        DC0_C0_H5
        DC0_C0_H6
        DC0_C0_H7
        DC0_C1_H0
        DC0_C1_H1
        DC0_C1_H2
        DC0_C1_H3
        DC0_C1_H4
        DC0_C1_H5
        DC0_C1_H6
        DC0_C1_H7
        ----------------------------------------------------------------------
        Host regex?: ^DC0.*
        Powered on/total (vcenter) VirtualMachines:  |################| 48/48

        """
        vmware.start(line)

    def do_poweron(self, line):
        """
        >>> poweron someesxi.domain.tld DC0_C0_RP5_VM0
        Please enter your username: user
        Password:
        DC0_C0_RP5_VM0 is already powered on!!

        """
        args = line.split()
        vmware.poweron(args[0], args[1])

    def do_poweroff(self, line):
        """
        >>> poweroff someesxi.domain.tld DC0_C0_RP5_VM0
        Please enter your username: user
        Password:
        DC0_C0_RP5_VM0 is now powered off

        """
        args = line.split()
        vmware.poweroff(args[0], args[1])

    def do_shell(self, line):
        """
        Yes you can! shell is available through !

        >>> !uname -a
        running shell command: uname -a
        Linux lsanmartin 3.13.0-49-generic #83-Ubuntu SMP Fri Apr 10 20:11:33
        UTC 2015 x86_64 x86_64 x86_64 GNU/Linux

        """
        output = os.popen(line).read()
        print(output)
        self.last_output = output

    def do_EOF(self, line):
        """
        It allows Ctrl+d
        """
        return True

    def postloop(self):
        """
        Greets when you Ctrl+d
        """
        print("\nBye!")

    def emptyline(self):
        """
        Warns you to not type empty lines

        """
        print("Do not type empty lines! type 'help' to get commands")

if __name__ == "__main__":
    shell = PyvShell()
    shell.cmdloop()
