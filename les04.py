import os 
import psutil  #сторонний модуль, требует установки 
import sys
import shutil

print("Программа в который раз")
print("Привет, программист")

name = input("Ваше имя: ")

print(name,', добро пожаловать в мир Python.')

answer = ''

while answer != 'q':
	answer = input("Давайте поработаем? (Y/N/q)")

	if answer == 'Y':
		print("Molodec")
		print("YA ymeu")
		print(' [1] - vivedy spisok failov')
		print(' [2] - vivedy informaciu o sisteme')
		print(' [3] - vivedy spisok prozesov')
		print(' [4] - prodybliryu faili v tekyshei dir')
		do = int(input("Ykazite nomer deistvia: "))

		if do == 1:
			print(os.listdir())
		elif do == 2:
			print("Current Dirrectory: ", os.getcwd())
			print('OS name: ', sys.platform)
			print('Encoding file system: ', sys.getfilesystemencoding())
			print('Login: ', os.getlogin())
			print("Cpu count: ", psutil.cpu_count())
		elif do == 3:
			print(psutil.pids)
		elif do == 4:
			print('+Дублирование файлов в текущей директории=')
			file_list = os.listdir()
			i = 0
			while i < len(file_list):
				newfile = file_list[i] + '.dupl'
				shutil.copy(file_list[i], newfile)
				i += 1
	elif answer == 'N':
		print("Vi yvoleni")	
	else:
		print("Neizvestniu vibor")

