#!/usr/bin/env python
import cmd
import os

from lib import vmware


class PyvShell(cmd.Cmd):
    prompt = '>>> '

    def do_ls(self, line):
        vmware.ls(line)

    def do_stop(self, line):
        vmware.stop(line)

    def do_start(self, line):
        vmware.start(line)

    def do_poweron(self, line):
        args = line.split()
        vmware.poweron(args[0], args[1])

    def do_poweroff(self, line):
        args = line.split()
        vmware.poweroff(args[0], args[1])

    def do_shell(self, line):
        """
        Yes you can! shell is available thorough !

        >>> !uname -a
        running shell command: uname -a
        Linux lsanmartin 3.13.0-49-generic #83-Ubuntu SMP Fri Apr 10 20:11:33 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux

        """
        output = os.popen(line).read()
        print(output)
        self.last_output = output

    def do_EOF(self, line):
        return True

    def postloop(self):
        print

    def emptyline(self):
        """
        Overrides definition for emptyline
        """
        print("Do not type empty lines! type 'help' to get commands")

if __name__ == "__main__":
    shell = PyvShell()
    shell.cmdloop()
