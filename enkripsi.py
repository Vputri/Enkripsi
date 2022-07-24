from tkinter import * 
import time 
import datetime 

root = Tk() 
root.geometry("700x500") 
root.title("Encryption and Decryption") 
  
Tops = Frame(root, width = 1600, relief = SUNKEN) 
Tops.pack(side = TOP) 
  
f1 = Frame(root, width = 800, height = 700, relief = SUNKEN) 
f1.pack(side = LEFT)

localtime = time.asctime(time.localtime(time.time())) 
  
lblInfo = Label(Tops, font = ('helvetica', 15, 'bold'), 
          text = "QWERTY ENCRIPT \n By : \n Rifqy Adli Damhuri (55417203) \n Vika Putri Ariyanti (56417094)", 
                     fg = "Blue", bd = 10, anchor='w') 
                       
lblInfo.grid(row = 0, column = 0) 
  
lblInfo = Label(Tops, font=('arial', 12, 'bold'), 
             text = localtime, fg = "Steel Blue", 
                           bd = 10, anchor = 'w') 
                          
lblInfo.grid(row = 1, column = 0) 
Msg = StringVar()  
Result = StringVar()
mode = StringVar()

def qExit(): 
    root.destroy()
def Reset(): 
    Msg.set("") 
    Result.set("")
    mode.set("") 

lblMsg = Label(f1, font = ('arial', 12, 'bold'), 
         text = "MESSAGE", bd = 12, anchor = "w") 
           
lblMsg.grid(row = 1, column = 3)
  
txtMsg = Entry(f1, font = ('arial', 12, 'bold'), 
         textvariable = Msg, bd = 8, insertwidth = 4, 
                bg = "powder blue", justify = 'right') 
                  
txtMsg.grid(row = 1, column = 4)


lblmode = Label(f1, font = ('arial', 12, 'bold'), 
          text = "MODE(e or d)", 
                                bd = 12, anchor = "w") 
                                  
lblmode.grid(row = 3, column = 3) 
  
txtmode = Entry(f1, font = ('arial', 12, 'bold'), 
          textvariable = mode, bd = 8, insertwidth = 4, 
                  bg = "powder blue", justify = 'right') 
                    
txtmode.grid(row = 3, column = 4) 

lblService = Label(f1, font = ('arial', 12, 'bold'), 
             text = "The Result-", bd = 12, anchor = "w") 
               
lblService.grid(row = 4, column = 3) 
  
txtService = Entry(f1, font = ('arial', 12, 'bold'),  
             textvariable = Result, bd = 8, insertwidth = 4, 
                       bg = "powder blue", justify = 'right') 
                         
txtService.grid(row = 4, column = 4)

key = 'qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+~`1234567890-={}|:"<>?[]\;,./'
offset = 5
def encrypt(n, message):
    result = ''
    for l in message.lower():
        try:
            i = (key.index(l) + n) % 67
            result += key[i]
        except ValueError:
            result += l
    return result.lower()
    encrypted = encrypt(offset, message)


def decrypt(n, message):
    result = ''
    for l in message:
        try:
            i = (key.index(l) - n) % 67
            result += key[i]
        except ValueError:
            result += l
    return result
    dencrypted = decrypt(offset, message)


def Ref():
    print("Message= ", (Msg.get())) 
    clear = Msg.get() 
    m = mode.get() 
    if (m == 'e'): 
        Result.set(encrypt(offset, clear)) 
    else: 
        Result.set(decrypt(offset, clear)) 

btnReset = Button(f1, padx = 16, pady = 8, bd = 12, 
                  fg = "black", font = ('arial', 12, 'bold'), 
                    width = 6, text = "Reset", bg = "green", 
                   command = Reset).grid(row = 16, column = 4) 
btnExit = Button(f1, padx = 16, pady = 8, bd = 12,  
                 fg = "black", font = ('arial', 12, 'bold'), 
                      width = 8, text = "Exit", bg = "red", 
                  command = qExit).grid(row = 16, column = 5) 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 12, fg = "black", 
                        font = ('arial', 12, 'bold'), width = 10, 
                       text = "Show Message", bg = "powder blue", 
                         command = Ref).grid(row = 16, column = 3) 
root.mainloop() 
