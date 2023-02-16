import cmd
import os

class PASH(cmd.Cmd):
    prompt = "root@pynux~$ "
    intro = "Welcome to PASH"

    def do_ls(self, arg):
        "List files in the current directory"
        print(os.listdir(os.getcwd()))

    def do_cd(self, path):
        "Change the current working directory"
        try:
            os.chdir(path)
        except FileNotFoundError:
            print(f"No such file or directory: {path}")

    def do_shutdown(self, arg):
        "Exit the PASH shell"
        print("Exiting PASH...")
        return True
    def do_exec(self, file):
        "Execute a Python File"
        try:
            os.system(f"py {file}")
            if file == "":
                print("pash: invalid usage")
        except FileExistsError:
            print("File does not exist")
        if file is None:
            pass
            

    def do_help(self, arg):
        "List available commands"
        cmd.Cmd.do_help(self, arg)
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

if __name__ == '__main__':
    with PASH() as pash:
        pash.cmdloop()