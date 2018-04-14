
import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создаёт копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def change_dir():
    import os
    try:
        os.chdir(n_cwdir)
        print('Your cwd: ', os.getcwd())
    except:
        print("Wrong path")

def c_w_d():
    import os
    print(os.getcwd())


def del_file():
    import os
    dir_path = os.path.join(os.getcwd(), '{}'.format(name))
    try:
        os.remove(dir_path)
        print("Dir {} deleted".format(name))
    except:
        print('Current directory allredy deleted')

def copy_file():
    import shutil
    path_to = os.path.join(os.getcwd(), '{}'.format(name))
    newfile = path_to + '_copy'
    try:
        shutil.copy(path_to, newfile)
    except FileNotFoundError:
        print("File to copy not found")
    
do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": del_file,
    "cd": change_dir,
    "ls": c_w_d,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    n_cwdir = sys.argv[2]
except IndexError:
    n_cwdir = None

try:
    name = sys.argv[2]
except IndexError:
    name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None



if key:
    if do.get(key):
        do[key]()
    else:
        print("Wrong key")
        print("Key - 'help' for help")
