from tkinter import *
import md5
import base64
try:
	from Crypto import Random
	from Crypto.Cipher import AES
except:
	print ("")
try:
	from Cryptodome import Random
	from Cryptodome.Cipher import AES
except:
	print ("")

	
BLOCK_SIZE=16

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master

    def init_window(self):
        self.master.title("encrypt and decryption")
        self.pack(fill=BOTH, expand=1)
        Label(self, text="data").place(x=100,y=50)
        data = Entry(self)
        data.place(x=150,y=50)
        Label(self, text="key").place(x=100,y=100)
        key = Entry(self)
        key.place(x=150,y=100)
        encButton = Button(self, text="encrypt",command=lambda: self.encrypt(data,key))
        encButton.place(x=150, y=250)
        decButton = Button(self, text="decrypt",command=lambda: self.decrypt(data,key))
        decButton.place(x=300, y=250)

    def showText(self,result):
        text = Label(self, text="encrypted/decrypted text: \n")
        text.place(x=140, y=150)
        v = StringVar()
        final = Entry(self,width=75,textvariable=v)
        final.place(x=20,y=170)
        v.set(result)
       
    def trans(self,key):
     return md5.new(key).digest()

    def encrypt(self,data,key):
        message=data.get()
        passphrase=key.get()
        passphrase = self.trans(passphrase)
        IV = Random.new().read(BLOCK_SIZE)
        aes = AES.new(passphrase, AES.MODE_CFB, IV)
        result=base64.b64encode(IV + aes.encrypt(message))
        self.showText(result)

    def decrypt(self,data,key):
        encrypted=data.get()
        passphrase=key.get()
        passphrase =self.trans(passphrase)
        encrypted = base64.b64decode(encrypted)
        IV = encrypted[:BLOCK_SIZE]
        aes = AES.new(passphrase, AES.MODE_CFB, IV)
        result= aes.decrypt(encrypted[BLOCK_SIZE:])
        self.showText(result)
        
root=Tk()
root.geometry("500x300")
app=Window(root)
app.init_window()
root.mainloop()
