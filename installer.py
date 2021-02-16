from subprocess import call, Popen
from tkinter import *
from tkinter.messagebox import askyesno, showerror
from getpass import getuser

try:
    import tkmacosx
except:
    try:
        call('pip3 install tkmacosx')
    except:
        call('pip install tkmacosx')

root = Tk()
root.geometry('400x400')

def installs():
    hint['text'] = '下载中 / Installing'
    try:
        call('git clone https://github.com/AccessRetrieved/Project-Pios', cwd='/Users/{}/Desktop'.format(getuser()), shell=True)
        try:
            call('pip3 install -r r.txt', cwd='/Users/{}/Desktop/Project-Pios'.format(getuser()), shell=True)
        except:
            call('pip install -r r.txt', cwd='/Users/{}/Desktop/Project-Pios'.format(getuser()), shell=True)

        call('mv project_pios ..', cwd='/Users/{}/Desktop/Project-Pios'.format(getuser()), shell=True)
        call('rm -rf Project-Pios', cwd='/Users/{}/Desktop'.format(getuser()), shell=True)
        ask = askyesno(message='下载成功，运行？\n\nInstall successful, run?')
        hint['text'] = '下载Project-Pios / Project-Pios Installer'
        if ask == True:
            try:
                Popen('python3 main.py', cwd='/Users/{}/Desktop/project_pios'.format(getuser()), shell=True)
                root.destroy()
            except:
                Popen('python main.py', cwd='/Users/{}/Desktop/project_pios'.format(getuser()), shell=True)
                root.destroy()
        else:
            root.destroy()
    except:
        showerror(message='下载失败\n\nInstall failed')
        hint['text'] = '下载Project-Pios / Project-Pios Installer'


hint = Label(root, text='下载Project-Pios / Project-Pios Installer', font=("Arial", 15))
hint.place(relx=0.5, rely=0.2, anchor=CENTER)

start = tkmacosx.Button(root, text='开始/Start', borderless=1, bg='black', fg='white', activebackground='white', activeforeground='black', command=installs)
start.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()