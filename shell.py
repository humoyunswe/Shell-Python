import sys
import os
import subprocess
import time
from datetime import datetime


class Terminal:
    def __init__(self):
        self.current_dir = os.getcwd()
        self.history = []
        self.start_time = time.time()
        
    def get_prompt(self):
        """
        Makes beautiful prompt:
        Like this: -> humoyunswe@terminal:~/Desktop/Projects/Shell-Python$ 

        display_path -> will seen /home/user/Desktop → ~/Desktop like that format.
        """
        user = os.getenv('USER', os.getenv('USERNAME', 'user'))
        hostname = 'terminal'
        
        home = os.path.expanduser('~')
        if self.current_dir.startswith(home):
            display_path = self.current_dir.replace(home, '~')
        else:
            display_path = self.current_dir
            
        return f"{user}@{hostname}:{display_path}$ "
    
    def execute_command(self, command_line):
        """
        Will execute all internal commands which I created as separated functions,
        All of which works after one operaton, they are:
         -> exit, cd, pwd, echo, type, help, history, clear, ls, cat, mkdir, touch, rm, cp,
        date, whoami, uptime. You can read in detail from functions and also in README.md file.

        All prompted commands here will saved in history.
        """
        command_line = command_line.strip()
        if not command_line:
            return True
            
        self.history.append(command_line)
        
        parts = command_line.split()
        command = parts[0]
        args = parts[1:] if len(parts) > 1 else []
        
        if command == "exit":
            return self.cmd_exit(args)
        elif command == "cd":
            return self.cmd_cd(args)
        elif command == "pwd":
            return self.cmd_pwd(args)
        elif command == "echo":
            return self.cmd_echo(args)
        elif command == "type":
            return self.cmd_type(args)
        elif command == "help":
            return self.cmd_help(args)
        elif command == "history":
            return self.cmd_history(args)
        elif command == "clear":
            return self.cmd_clear(args)
        elif command == "ls":
            return self.cmd_ls(args)
        elif command == "cat":
            return self.cmd_cat(args)
        elif command == "mkdir":
            return self.cmd_mkdir(args)
        elif command == "touch":
            return self.cmd_touch(args)
        elif command == "rm":
            return self.cmd_rm(args)
        elif command == "cp":
            return self.cmd_cp(args)
        elif command == "date":
            return self.cmd_date(args)
        elif command == "whoami":
            return self.cmd_whoami(args)
        elif command == "uptime":
            return self.cmd_uptime(args)
        else:
            return self.execute_external(command, args)
        
    def cmd_exit(self, args):
        """
        Exit from terminal
        """
        exit_code = 0
        if args:
            try:
                exit_code = int(args[0])
            except:
                print("exit: need number")
                return True
        
        print("See you again!")
        sys.exit(exit_code)
        return False
    
    def cmd_cd(self, args):
        """
        Changes directory
        """
        if not args:
            new_dir = os.path.expanduser('~')
        else:
            new_dir = args[0]
            
        if not os.path.isabs(new_dir):
            new_dir = os.path.join(self.current_dir, new_dir)
        
        new_dir = os.path.normpath(new_dir)
        
        if os.path.isdir(new_dir):
            self.current_dir = new_dir
            os.chdir(new_dir)
        else:
            print(f"cd: {new_dir}: Not found yet")
        
        return True
    
    def cmd_pwd(self, args):
        """
        Shows current path
        """
        print(self.current_dir)
        return True
    
    def cmd_echo(self, args):
        """
        Withdraws text
        """
        print(' '.join(args))
        return True
    
    def cmd_type(self, args):
        """
        Shows type of command
        """
        if not args:
            print("type: need name of cammand")
            return True
            
        command = args[0]
        builtin_commands = ['exit', 'cd', 'pwd', 'echo', 'type', 'help', 
                           'history', 'clear', 'ls', 'cat', 'mkdir', 
                           'touch', 'rm', 'cp', 'date', 'whoami', 'uptime']
        
        if command in builtin_commands:
            print(f"{command} - inner command")
    
        else:
            print(f"{command}: not found")
        
        return True

    def cmd_help(self, args):
        """
        Shows reference
        """
        print("Available commands:")
        print("  cd [folder]   - Changes directory")
        print("  pwd           - Shows current folder")
        print("  ls [folder]   - List of files")
        print("  cat [file]    - Shows up file")
        print("  mkdir [folder] - Creates new folder")
        print("  touch [file]  - Creates new file")
        print("  rm [file]     - Removes file")
        print("  cp [from] [to] - Copies")
        print("  echo [text]   - Withdraws text")
        print("  date          - Shows date")
        print("  whoami        - Shows user")
        print("  uptime        - Working hours")
        print("  history       - History of command")
        print("  clear         - Cleans display")
        print("  help          - This reference")
        print("  exit [code]   - Exit")
        return True
    
    def cmd_history(self, args):
        """
        Shows history of command

        For instance:
        If you have typed:
        - cd Desktop,
        - pwd,
        - echo Hello World!

        You will take response in that format:
        1 cd Desktop
        2 pwd
        3 echo Hello World!
        """
        if not self.history:
            print("History is empty!")
            return True
            
        recent = self.history[-20:]
        for i, cmd in enumerate(recent, 1):
            print(f"{i:3d}  {cmd}")
        
        return True
    
    def cmd_clear(self, args):
        """
        Clearing history
        """
        os.system('clear')
        return True

    def cmd_ls(self, args):
        """
        Gives list of files 
        """
        path = args[0] if args else self.current_dir
        
        try:
            items = os.listdir(path)
            items.sort()
            
            for item in items:
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    print(f"{item}/") 
                else:
                    print(item)
        except Exception as e:
            print(f"ls: Error - {e}")
        
        return True
    
    def cmd_cat(self, args):
        """
        Shows content of file
        """
        if not args:
            print("cat: need name of file")
            return True
            
        for filename in args:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    print(file.read())
            except Exception as e:
                print(f"cat: {filename} - {e}")
        
        return True
    
    def cmd_mkdir(self, args):
        """
        Creates file
        """
        if not args:
            print("mkdir: need name of file")
            return True
            
        for dirname in args:
            full_path = os.path.join(os.getcwd(), dirname)
            try:
                if not os.path.isdir(full_path):
                    os.makedirs(dirname)
                    print(f"Created file: {dirname}")
                else:
                    print(f"Already exists file: {dirname}")
            except Exception as e:
                print(f"mkdir: {dirname} - {e}")
        
        return True
    
    def cmd_touch(self, args):
        """
        Creates an empty file
        """
        if not args:
            print("touch: need file name")
            return True
            
        for filename in args:
            try:
                with open(filename, 'a'):
                    pass  
                print(f"Created file: {filename}")
            except Exception as e:
                print(f"touch: {filename} - {e}")
        
        return True
    
    def cmd_rm(self, args):
        """
        Remove file
        """
        if not args:
            print("rm: need file name")
            return True
            
        for filename in args:
            try:
                if os.path.isfile(filename):
                    os.remove(filename)
                    print(f"Removed file: {filename}")
                else:
                    print(f"rm: {filename} not found")
            except Exception as e:
                print(f"rm: {filename} - {e}")
        
        return True
      
    def run(self):
        """
        Main loop of terminal
        """
        print("=== Terminal ===")
        print("Type 'help' for reference")
        print()
        
        while True:
            try:
                prompt = self.get_prompt()
                command = input(prompt)
                
                if not self.execute_command(command):
                    break
                    
            except KeyboardInterrupt:
                print("\n^C")
                continue
            except EOFError:
                print("\nExit...")
                break
    
def main():
    """Start Terminal"""
    try:
        terminal = Terminal()
        terminal.run()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()