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
		print(' [5] - дублирование указанного файда')
		print(' [6] - удаление всех файлов с окончанием dupl')
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
		elif do == 5:
			k = ''
			while k != 'N':
				print('Дублирование файла, выбранного пользователем')
				file_list = os.listdir() 
				if k == '':
					print(file_list)
				else:
					pass
				i = int(input('Введите номер файла: ')) - 1
				newfile = file_list[i] + '.dupl'
				shutil.copy(file_list[i], newfile)
				file_list = os.listdir()
				print('Отлично, вот новый список файлов: ', file_list)
				k = input('Продолжим? N\Y: ')
		elif do == 6:
			print('Удаление всех файлов с окончанием dupl')
			dir_name = input('Введите путь к директории([C] - текущая директория: ')
			if dir_name == 'C':
				dir_name = os.getcwd()
			if not dir_name.endswith('/'):
				dir_name = dir_name + '/'

			file_list = os.listdir(dir_name)
			i = 0
			for file_name in file_list:
				if file_name.endswith('.dupl'):
					os.remove(dir_name + file_name)
				#i =+ 1
			print(os.listdir(dir_name))
	elif answer == 'N':
		print("Vi yvoleni")	
	elif answer == 'q':
		print('vihod')
	else:
		print("Neizvestniu vibor")
