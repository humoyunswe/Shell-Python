 
   
    
    def cmd_history(self, args):
        """Показать историю команд"""
        if not self.history:
            print("История пуста")
            return True
            
        # Показать последние 20 команд
        recent = self.history[-20:]
        for i, cmd in enumerate(recent, 1):
            print(f"{i:3d}  {cmd}")
        
        return True
    
    def cmd_clear(self, args):
        """Очистить экран"""
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Linux/Mac
            os.system('clear')
        return True
    
    def cmd_ls(self, args):
        """Список файлов"""
        path = args[0] if args else self.current_dir
        
        try:
            items = os.listdir(path)
            items.sort()
            
            for item in items:
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    print(f"{item}/")  # Папки со слешем
                else:
                    print(item)
        except Exception as e:
            print(f"ls: ошибка - {e}")
        
        return True
    
    def cmd_cat(self, args):
        """Показать содержимое файла"""
        if not args:
            print("cat: нужно имя файла")
            return True
            
        for filename in args:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    print(f.read())
            except Exception as e:
                print(f"cat: {filename} - {e}")
        
        return True
    
    def cmd_mkdir(self, args):
        """Создать папку"""
        if not args:
            print("mkdir: нужно имя папки")
            return True
            
        for dirname in args:
            try:
                os.makedirs(dirname, exist_ok=True)
                print(f"Создана папка: {dirname}")
            except Exception as e:
                print(f"mkdir: {dirname} - {e}")
        
        return True
    
    def cmd_touch(self, args):
        """Создать пустой файл"""
        if not args:
            print("touch: нужно имя файла")
            return True
            
        for filename in args:
            try:
                with open(filename, 'a'):
                    pass  # Просто создать файл
                print(f"Создан файл: {filename}")
            except Exception as e:
                print(f"touch: {filename} - {e}")
        
        return True
    
    def cmd_rm(self, args):
        """Удалить файл"""
        if not args:
            print("rm: нужно имя файла")
            return True
            
        for filename in args:
            try:
                if os.path.isfile(filename):
                    os.remove(filename)
                    print(f"Удален файл: {filename}")
                else:
                    print(f"rm: {filename} не найден")
            except Exception as e:
                print(f"rm: {filename} - {e}")
        
        return True
    
    def cmd_cp(self, args):
        """Копировать файл"""
        if len(args) < 2:
            print("cp: нужно 2 аргумента - откуда и куда")
            return True
            
        try:
            import shutil
            shutil.copy2(args[0], args[1])
            print(f"Скопировано: {args[0]} -> {args[1]}")
        except Exception as e:
            print(f"cp: ошибка - {e}")
        
        return True
    
    def cmd_date(self, args):
        """Показать дату и время"""
        now = datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        return True
    
    def cmd_whoami(self, args):
        """Показать пользователя"""
        user = os.getenv('USER', os.getenv('USERNAME', 'неизвестно'))
        print(user)
        return True
    
    def cmd_uptime(self, args):
        """Время работы терминала"""
        uptime = int(time.time() - self.start_time)
        hours = uptime // 3600
        minutes = (uptime % 3600) // 60
        seconds = uptime % 60
        
        print(f"Работает: {hours:02d}:{minutes:02d}:{seconds:02d}")
        print(f"Команд выполнено: {len(self.history)}")
        return True
    
    def find_in_path(self, command):
        """Найти команду в PATH"""
        path_dirs = os.environ.get('PATH', '').split(os.pathsep)
        
        for path_dir in path_dirs:
            if not path_dir:
                continue
                
            full_path = os.path.join(path_dir, command)
            
            # Проверить файл
            if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                return full_path
            
            # На Windows проверить с расширениями
            if os.name == 'nt':
                for ext in ['.exe', '.cmd', '.bat']:
                    full_path_ext = full_path + ext
                    if os.path.isfile(full_path_ext):
                        return full_path_ext
        
        return None
    
    def execute_external(self, command, args):
        """Выполнить внешнюю команду"""
        # Найти команду в PATH
        cmd_path = self.find_in_path(command)
        
        if not cmd_path:
            print(f"{command}: команда не найдена")
            return True
        
        try:
            # Запустить команду
            result = subprocess.run(
                [cmd_path] + args,
                cwd=self.current_dir,
                capture_output=False,  # Показывать вывод сразу
                text=True
            )
            
            # Ничего не делаем с результатом - он уже выведен
            
        except Exception as e:
            print(f"{command}: ошибка - {e}")
        
        return True
    
    def run(self):
        """Главный цикл терминала"""
        print("=== Простой Терминал ===")
        print("Наберите 'help' для справки")
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
                print("\nВыход...")
                break


def main():
    """Запуск терминала"""
    try:
        terminal = Terminal()
        terminal.run()
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()