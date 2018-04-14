def cr_dir():
    import os
    x = 1
    while x < 10:
        dir_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'dir_{}'.format(x))
        try:
            os.mkdir(dir_path)
        except:
            print('Current directory allredy existed')
        x += 1
        
def del_dir():
    import os
    print(os.getcwd())
    x = 1
    while x < 10:
        dir_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'dir_{}'.format(x))
        try:
            os.rmdir(dir_path)
        except:
            print('Current directory allredy deleted')
        x += 1

def print_dir_in_cd():
    import os
    list_of_all = os.listdir(os.path.dirname(
        os.path.abspath(__file__)))
    list_of_dir = []
    i = 0
    while i < len(list_of_all):
        if os.path.isdir(list_of_all[i]):
            list_of_dir.append(list_of_all[i])
        i += 1

    print(list_of_dir)

def  copy_cur_file(): #копировал именно файлы с расширением .ру
    import shutil
    import sys
    file_path = sys.argv
    file_name = file_path[0]
    newfile = (file_name[:-3] + '_copy.py')
    shutil.copy(file_path[0], newfile)
