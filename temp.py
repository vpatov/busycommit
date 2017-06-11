import os,sys,random,subprocess

dir = 'C:\\Users\\Vasia\\Documents\\PycharmProjects\\'
p = subprocess.Popen(['dir'],shell=True,cwd=dir)
p.wait()
p = subprocess.Popen(['dir'],shell=True,cwd=dir)
p.wait()