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