import os 
import psutil  #сторонний модуль, требует установки 
import sys

print("Программа в который раз")
print("Привет, программист")

name = input("Ваше имя: ")

print(name,', добро пожаловать в мир Python.')

answer = input("Давайте поработаем? (Y/N)")

if answer == 'Y':
	print("Molodec")
	print("YA ymeu")
	print(' [1] - vivedy spisok failov')
	print(' [2] - vivedy informaciu o sisteme')
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
elif answer == 'N':
	print("Vi yvoleni")	
else:
	print("Neizvestniu vibor")

