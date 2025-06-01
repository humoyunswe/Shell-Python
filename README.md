# Shell-Python

A lightweight, cross-platform terminal emulator built from scratch in Python. Features 17+ built-in commands, command history, and support for external programs.

![Shell-icon](/project_photos/shell-icon.png)


## Features

- **17+ Built-in Commands** - Complete set of essential terminal operations
- **Beautiful Prompt** - Shows `user@hostname:path$` format 

  For example:
`humoyunswe@terminal:~/Desktop/Projects/Shell-Python$`
- **Command History** - Track and review all executed commands
- **Cross-Platform** - Works on Windows, Linux, and macOS
- **External Programs** - Execute system commands via PATH lookup
- **File Operations** - Create, read, copy, and delete files/directories
- **Session Management** - Track uptime and command statistics

## Quick Start

### Prerequisites

- Python 3.6 or higher
- No additional dependencies required

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/humoyunswe/Shell-Python.git
   cd Shell-Python
   ```

2. **Run the terminal**
   ```bash
   python terminal.py
   ```

3. **Start using commands**
   ```bash
   humoyunswe@terminal:~$ help
   humoyunswe@terminal:~$ ls
   humoyunswe@terminal:~$ echo "Hello, World!"
   ```

## Available Commands

### File & Directory Operations
| Command | Description | Example |
|---------|-------------|---------|
| `ls [path]` | List files and directories | `ls`, `ls /home` |
| `cd [directory]` | Change directory | `cd Documents`, `cd ..` |
| `pwd` | Show current directory | `pwd` |
| `mkdir [name]` | Create directory | `mkdir new_folder` |
| `touch [file]` | Create empty file | `touch hello.txt` |
| `cat [file]` | Display file contents | `cat readme.txt` |
| `rm [file]` | Delete file | `rm unwanted.txt` |
| `cp [source] [dest]` | Copy file | `cp file.txt backup.txt` |

### System Information
| Command | Description | Example |
|---------|-------------|---------|
| `whoami` | Show current user | `whoami` |
| `date` | Show current date/time | `date` |
| `uptime` | Show session statistics | `uptime` |

### Terminal Control
| Command | Description | Example |
|---------|-------------|---------|
| `echo [text]` | Print text to screen | `echo "Hello World"` |
| `clear` | Clear terminal screen | `clear` |
| `history` | Show command history | `history` |
| `help` | Display help information | `help` |
| `type [command]` | Show command type | `type ls` |
| `exit [code]` | Exit terminal | `exit`, `exit 0` |

## Usage Examples

### Basic Navigation
```bash
user@terminal:~$ pwd
/home/user

user@terminal:~$ ls
Documents  Downloads  Pictures

user@terminal:~$ cd Documents
user@terminal:~/Documents$ pwd
/home/user/Documents
```

### File Operations
```bash
humoyunswe@terminal:~$ mkdir my_project
Created directory: my_project

humoyunswe@terminal:~$ cd my_project
humoyunswe@terminal:~/my_project$ touch README.md
Created file: README.md

humoyunswe@terminal:~/my_project$ echo "# My Project" > README.md
humoyunswe@terminal:~/my_project$ cat README.md
# My Project
```

### System Information
```bash
humoyunswe@terminal:~$ whoami
john

humoyunswe@terminal:~$ date
2024-12-07 14:30:25

humoyunswe@terminal:~$ uptime
Runtime: 00:05:23
Commands executed: 12
```

### Command History
```bash
humoyunswe@terminal:~$ history
  1  ls
  2  cd Documents
  3  pwd
  4  mkdir test
  5  touch file.txt
```

## Architecture

The terminal is built with a clean, modular architecture:

```
Terminal Class
├── Command Parser
├── Built-in Commands (17+)
├── External Program Executor
├── History Manager
└── Session Tracker
```

### Key Components

- **`Terminal`** - Main class handling command execution
- **`get_prompt()`** - Generates beautiful command prompt
- **`execute_command()`** - Parses and routes commands
- **Built-in Commands** - 17+ implemented as separate methods
- **External Execution** - Handles system programs via PATH


## Customization

### Adding New Commands

1. **Add command to execute_command()**
   ```python
   elif command == "newcommand":
       return self.cmd_newcommand(args)
   ```

2. **Implement the command method**
   ```python
   def cmd_newcommand(self, args):
       """Your new command description"""
       # Command implementation here
       return True
   ```

3. **Update help text**
   ```python
   def cmd_help(self, args):
       # Add your command to the help list
   ```
