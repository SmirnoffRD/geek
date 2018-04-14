def change_dir():
    import os
    try:
        os.chdir(input('Input path to new w_dir: ', )) 
        print('Your cwd: ', os.getcwd())
    except:
        print("Wrong path")

def list_of_files():
    import os
    file_list = os.listdir(os.getcwd())
    list_w_index(file_list)
                
def cr_dir():
    import os
    while True:
        print_dir_in_cd()
        name = input('Enter directory name you want to create: ', )
        dir_path = os.path.join(os.getcwd(), '{}'.format(name))
        try:
            os.mkdir(dir_path)
            print("Dir {} created".format(name))
        except:
            print('Current directory allredy existed')
        commad = input("One more?[Y/N]", )
        if commad == 'N':
            break

def del_dir():
    import os
    while True:
        print_dir_in_cd()
        name = input('Enter directory name you want to delet: ', )
        dir_path = os.path.join(os.getcwd(), '{}'.format(name))
        try:
            os.rmdir(dir_path)
            print("Dir {} deleted".format(name))
        except:
            print('Current directory allredy deleted')
        commad = input("One more?[Y/N]", )
        if commad == 'N':
            break

def print_dir_in_cd():
    import os
    list_of_all = os.listdir(os.getcwd())
    list_of_dir = []
    i = 0
    while i < len(list_of_all):
        if os.path.isdir(list_of_all[i]):
            list_of_dir.append(list_of_all[i])
        i += 1    
    list_w_index(list_of_dir)

def list_w_index(list_in):
    align_step = len(max(list_in, key=len))
    for index, item in enumerate(list_in, start=1):
        if index < 10:
            print("{}.{} {:>{}}".format(
                index, " ", item, align_step
            ))
        else:
            print("{}. {:>{}}".format(
                index, item, align_step
            ))
