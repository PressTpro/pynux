import os
import sys
import subprocess
import pash

pynuxversion = 1.0

class Kernel:
    """
    A class to represent the Pynux kernel.
    """

    def boot(self):
        """
        Start the Pynux kernel.
        """
        print("Starting Up Pynux...")
        print(f"Pynux {pynuxversion}")
        print("Initializing PASH Terminal")

        try:
            shell = pash.PASH()
            with shell:
                shell.cmdloop()
        except Exception as e:
            print(f"Error initializing PASH: {e}")
        finally:
            self.shutdown()

    def shutdown(self):
        """
        Shutdown the Pynux kernel and kill any running subprocesses.
        """
        sys.exit()

    def reboot(self):
        """
        Reboot the Pynux kernel.
        """
        print("Rebooting Pynux...")
        python = sys.executable
        os.execl(python, python, *sys.argv)

if __name__ == "__main__":
    kernel = Kernel()
    kernel.boot()