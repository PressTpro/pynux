import os
import tkinter as tk
import subprocess
import pash
# The UI will not come with Pynux, you have to use the gui install command in Pynux
class PynuxUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pynux Desktop")
        self.create_terminal()
        self.create_turnoff_button()
        
    def create_terminal(self):
        self.terminal = tk.Frame(self.root)
        self.terminal.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.terminal_text = tk.Text(self.terminal, bg="black", fg="white")
        self.terminal_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Redirect stdout to the terminal text widget
        sys.stdout = self
        sys.stderr = self
        
        try:
            shell = pash.PASH(stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            self.shell = shell
            with shell:
                while True:
                    data = shell.stdout.readline()
                    if not data:
                        break
                    self.terminal_text.insert(tk.END, data.decode())
                    self.terminal_text.see(tk.END)
        except Exception as e:
            print(f"Error initializing PASH: {e}")
            self.root.quit()
    
    def create_turnoff_button(self):
        self.turnoff_button = tk.Button(self.root, text="Turn Off", command=self.turnoff)
        self.turnoff_button.pack(side=tk.BOTTOM, fill=tk.X)
        
    def turnoff(self):
        self.shell.do_exit(None)
        self.root.quit()
        
    def write(self, text):
        self.terminal_text.insert(tk.END, text)
        self.terminal_text.see(tk.END)
        
    def flush(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    pynux_ui = PynuxUI(root)
    root.mainloop()
