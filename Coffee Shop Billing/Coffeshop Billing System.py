from tkinter import *
from PIL import ImageTk,Image
import pandas
import pandas as pd
import datetime
from time import strftime

coffee_shop = Tk()
coffee_shop.geometry('900x600')
coffee_shop.resizable(0, 0)
coffee_shop.state('zoomed')
coffee_shop.title('Coffee Shop')
pelanggan_var = StringVar()

image_0 = Image.open("background1.png")
bck_end =ImageTk.PhotoImage(image_0)


label=Label(coffee_shop,image=bck_end)
label.place(x=0, y=0)
label.pack()

loginframe = Frame(coffee_shop,width= 950 , height=650,bg="#DAA520")
loginframe.place(x= 150, y=20)

heading = Label(loginframe,text="SELAMAT DATANG",fg= "black", bg="#DAA520", font=("helvetica",23,"bold"))
heading.place(x=325, y=45)

sideimage = PhotoImage(file="Logo samping.png")
Label(coffee_shop,image=sideimage,bg="#DAA520").place(x=150,y=100)

def on_enter(e):
    user.delete(0, 'end')    
def on_leave(e):
    user  =user.get()
    if user =='':
        user.insert(0, 'Nama')
        
user = Entry(loginframe, width=23,fg="black",textvariable= pelanggan_var ,border=0, bg="white", font=("helvetica",20))
user.place(x=525, y=250)
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
user.insert(0,"Nama Pelanggan")
userimage = PhotoImage(file="username_icon.png")
Label(coffee_shop,image=userimage,bg="#DAA520").place(x=640, y= 275)

usernameline = Canvas(width=300, height=2.0, bg="#000000", highlightthickness=0)
usernameline.place(x=675, y=304)

#realtime
def my_time():
   time_s = strftime("%H: %M: %S, %d %B %Y")
   l1.config(text="{}".format(time_s))
   l1.after(1000,my_time)
l1 = Label(coffee_shop, font=("Helvetica", 20, "bold"), bg="#DAA520")
l1.place(x=170,y=620)
my_time()

current_value = StringVar(value=0)
def return_value(pos):
    current_value.set(pos)
current_value1 = StringVar(value=0)
def return_value(pos):
    current_value1.set(pos)
current_value2 = StringVar(value=0)
def return_value(pos):
    current_value2.set(pos)
current_value3= StringVar(value=0)
def return_value(pos):
    current_value3.set(pos)
current_value4 = StringVar(value=0)
def return_value(pos):
    current_value4.set(pos)
current_value5 = StringVar(value=0)
def return_value(pos):
    current_value5.set(pos)
current_value6 = StringVar(value=0)
def return_value(pos):
    current_value6.set(pos)
current_value7 = StringVar(value=0)
def return_value(pos):
    current_value7.set(pos)
current_value8 = StringVar(value=0)
def return_value(pos):
    current_value8.set(pos)
current_value9 = StringVar(value=0)
def return_value(pos):
    current_value9.set(pos)
current_value10= StringVar(value=0)
def return_value(pos):
    current_value10.set(pos)
current_value11= StringVar(value=0)
def return_value(pos):
    current_value11.set(pos)
current_value12 = StringVar(value=0)
def return_value(pos):
    current_value12.set(pos)
current_value13= StringVar(value=0)
def return_value(pos):
    current_value13.set(pos)
current_value14= StringVar(value=0)
def return_value(pos):
    current_value14.set(pos)
current_value15= StringVar(value=0)
def return_value(pos):
    current_value15.set(pos)
current_value16= StringVar(value=0)
def return_value(pos):
    current_value16.set(pos)
current_value17= StringVar(value=0)
def return_value(pos):
    current_value17.set(pos)

def order ():
   loginframe = Frame(coffee_shop,width= 1280 , height=720,bg="#DAA520")
   loginframe.place(x= 0, y=0)
   Drink_label = Label(loginframe,text="Drink", font=("Times New Roman", 26, "bold"),bg="#DAA520")
   Drink_label.place(x=30,y=20)
   namaLabel = Label (loginframe,text=f"Halo {pelanggan_var.get()}",font=("Helvetica",17,"bold"),bg="#DAA520")
   namaLabel.place(x=470,y=650)
   #LATTE
   latteimage = ImageTk.PhotoImage(Image.open("latte.png"))
   label2 = Label(loginframe,image=latteimage,bg="#DAA520")
   label2.image = latteimage
   label2.place(x=20, y=65)
   latte_label = Label(loginframe,text="Latte\n Rp.15.000",bg="#DAA520",font=("helvetica",17, "bold"))
   latte_label.place(x=70,y=225)
   global current_value
   return_value(current_value)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value.get())
      print(current_value)
      
   
   latte_sb = Spinbox(from_=0,to=10, width=5, textvariable=current_value) 
   latte_sb.place(x=100, y=310)

   #GREEN TEA LATTE 
   glatteimage = ImageTk.PhotoImage(Image.open("green tea latte.png"))
   label3 = Label(loginframe,image=glatteimage,bg="#DAA520")
   label3.image = glatteimage
   label3.place(x=200, y=70)
   glatte_label = Label(loginframe,text="Green Tea\n Latte\n Rp.20.000",bg="#DAA520",font=("helvetica",17, "bold"))
   glatte_label.place(x=255,y=215)
   global current_value1
   return_value(current_value1)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value1.get())
      print(current_value1)
   glatte_sb = Spinbox(from_=0, to=10, width=5,textvariable=current_value1)
   glatte_sb.place(x=300, y=310)
   
   # BLACK TEA LATTE
   blatteimage = ImageTk.PhotoImage(Image.open("black tea latte.png"))
   label4 = Label(loginframe,image=blatteimage,bg="#DAA520")
   label4.image = blatteimage
   label4.place(x=380, y=60)
   blatte_label = Label(loginframe,text="Black Tea\n Latte\n Rp.20.000",bg="#DAA520",font=("helvetica",17, "bold"))
   blatte_label.place(x=470,y=215)
   global current_value2
   return_value(current_value2)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value2.get())
      print(current_value2)
   blatte_sb = Spinbox(from_=0, to=10, width=5,textvariable = current_value2)
   blatte_sb.place(x=510, y=310)
   # ESPRESSO
   espressoimage = ImageTk.PhotoImage(Image.open("espresso.png"))
   label5 = Label(loginframe,image=espressoimage,bg="#DAA520")
   label5.image = espressoimage
   label5.place(x=590, y=45)
   espresso_label = Label(loginframe,text="Espresso\n Rp.18.000",bg="#DAA520",font=("helvetica",17, "bold"))
   espresso_label.place(x=675,y=230)
   global current_value3
   return_value(current_value3)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value3.get())
      print(current_value3)
   espresso_sb = Spinbox(from_=0, to=10, width=5,textvariable = current_value3)
   espresso_sb.place(x=700, y=310)
   # AMERICANO
   americanoimage = ImageTk.PhotoImage(Image.open("americano.png"))
   label6 = Label(loginframe,image=americanoimage,bg="#DAA520")
   label6.image = americanoimage
   label6.place(x=800, y=65)
   americano_label = Label(loginframe,text="Americano\n Rp.18.000",bg="#DAA520",font=("helvetica",17, "bold"))
   americano_label.place(x=875,y=230)
   global current_value4
   return_value(current_value4)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value4.get())
      print(current_value4)
   americano_sb = Spinbox(from_=0, to=10, width=5,textvariable = current_value4)
   americano_sb.place(x=900, y=310)
   #CARAMEL MACCHIATO
   caramelm = ImageTk.PhotoImage(Image.open("caramel macchiato.png"))
   label7 = Label(loginframe,image=caramelm,bg="#DAA520")
   label7.image = caramelm
   label7.place(x=-50, y=300)
   caramelm_label = Label(loginframe,text="Caramel\n Macchiato\nRp.23.000",bg="#DAA520",font=("helvetica",17, "bold"))
   caramelm_label.place(x=60,y=470)
   global current_value5
   return_value(current_value5)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value5.get())
      print(current_value5)
   caramelm_sb = Spinbox(from_=0, to=10, width=5,textvariable = current_value5)
   caramelm_sb.place(x=100, y=580)
   # Cappuchino
   cappucino = ImageTk.PhotoImage(Image.open("cappucino.png"))
   label8 = Label(loginframe,image=cappucino,bg="#DAA520")
   label8.image = cappucino
   label8.place(x=200, y=300)
   cappucino_label = Label(loginframe,text="Cappucino\nRp.15.000",bg="#DAA520",font=("helvetica",17, "bold"))
   cappucino_label.place(x=255,y=480)
   global current_value6
   return_value(current_value6)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value6.get())
      print(current_value6)
   cappucino_sb = Spinbox(from_=0, to=10, width=5,textvariable = current_value6)
   cappucino_sb.place(x=300, y=580)
   #CARAMEL CREAM FRAPPUCCINO 
   ccf = ImageTk.PhotoImage(Image.open("caramel cream frappucino.png"))
   label9 = Label(loginframe,image=ccf,bg="#DAA520")
   label9.image = ccf
   label9.place(x=400, y=300)
   ccf_label = Label(loginframe,text="Caramel Cream\n Frappucino\nRp.25.000",bg="#DAA520",font=("helvetica",17, "bold"))
   ccf_label.place(x=455,y=470)
   return_value(current_value7)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value7.get())
      print(current_value7)
   ccf_sb = Spinbox(from_=0, to=10, width=5,textvariable = current_value7)
   ccf_sb.place(x=510, y=580)
   #GREEN TEA CREAM FRAPPUCCINO 
   gtcf = ImageTk.PhotoImage(Image.open("green tea cream frappucino.png"))
   label10 = Label(loginframe,image=gtcf,bg="#DAA520")
   label10.image = gtcf
   label10.place(x=600, y=300)
   gtcf_label = Label(loginframe,text="Green Tea Cream\n Frappucino\nRp.25.000",bg="#DAA520",font=("helvetica",17, "bold"))
   gtcf_label.place(x=655,y=470)
   global current_value8
   return_value(current_value8)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value8.get())
      print(current_value8)
   gtcf_sb = Spinbox(from_=0, to=10, width=5,textvariable = current_value8)
   gtcf_sb.place(x=710, y=580)
   # VANILLA CREAM FRAPPUCINO
   vcf = ImageTk.PhotoImage(Image.open("vanilla cream frappucino.png"))
   label11 = Label(loginframe,image=vcf,bg="#DAA520")
   label11.image = vcf
   label11.place(x=800, y=300)
   vcf_label = Label(loginframe,text="Vanilla Cream\n Frappuccino\nRp.25.000",bg="#DAA520",font=("helvetica",17, "bold"))
   vcf_label.place(x=875,y=470)
   global current_value9
   return_value(current_value9)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value9.get())
      print(current_value9)
   vcf_sb = Spinbox(from_=0, to=10, width=5,textvariable = current_value9)
   vcf_sb.place(x=910, y=580)
   
   # TOMBOL NEXT
   simpan = Button(loginframe, width=10, pady=7, text="Save", bg='#8B4513', fg='white',command=value_changed).place(x=1000, y=600)
   NEXT = Button(loginframe, width=10, pady=7, text="Next", bg='#8B4513', fg='white',command=order2).place(x=1100, y=600)
   
def test():     
   namaslur=pelanggan_var.get()               
   if namaslur=='Nama Pelanggan':         
      Label(loginframe, text='Silahkan Masukan Nama dengan Valid!',fg='red', bg='#DAA520').place(x=585, y=300)         
      return namaslur  
   else:         
      Label(loginframe, text='Data Yang Anda Masukan Valid, Silahkan Melanjutkan Memesan',fg='white', bg='#DAA520').place(x=520, y=300)     
   if namaslur=='':  
      Label(loginframe, text='Silahkan Masukan Nama dengan Valid!',fg='red', bg='white').place(x=585, y=300)        
      return namaslur 

   else:
      Label(loginframe, text='Data Yang Anda Masukan Valid, Silahkan Melanjutkan Memesan',fg='white', bg='#DAA520').place(x=700, y=5520)
      Button(loginframe, width=39,pady=7, text="Selanjutnya",bg='#8B4513', fg='white', command=order).place(x=550, y=520) 
pesan = Button(coffee_shop, width=39, pady=7, text="Pesan YUK", bg='#8B4513', fg='white',command=test).place(x=700, y=500)

def order2 ():
   orderframe = Frame(coffee_shop,width= 1280 , height=720,bg="#DAA520")
   orderframe.place(x= 0, y=0)
   snack_label = Label(orderframe,text="Snack", font=("Times New Roman", 26, "bold"),bg="#DAA520")
   snack_label.place(x=25,y=10)
   namaLabel = Label (orderframe,text=f"Halo {pelanggan_var.get()}",font=("Helvetica",17,"bold"),bg="#DAA520")
   namaLabel.place(x=470,y=650)
    #Apple And Cinnamon Crumble
   aacc = ImageTk.PhotoImage(Image.open("appel and cinnamon crumble.png"))
   label12 = Label(orderframe,image=aacc,bg="#DAA520")
   label12.image = aacc
   label12.place(x=40, y=45)
   aacc_label = Label(orderframe,text="Apple and\n Cinnamon Crumble\n Rp.24.000",bg="#DAA520",font=("helvetica",17, "bold"))
   aacc_label.place(x=20,y=215)
   global current_value10
   return_value(current_value10)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value10.get())
      print(current_value10)
   aacc_sb = Spinbox(from_=0, to=10, width=5,textvariable = current_value10)
   aacc_sb.place(x=100, y=320)
   # Chicken Sandwich
   cs = ImageTk.PhotoImage(Image.open("chicken sandwich.png"))
   label13 = Label(orderframe,image=cs,bg="#DAA520")
   label13.image = cs
   label13.place(x=300, y=35)
   cs_label = Label(orderframe,text="Chicken Sandwich\n Rp.25.000",bg="#DAA520",font=("helvetica",17, "bold"))
   cs_label.place(x=300,y=225)
   global current_value11
   return_value(current_value11)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value11.get())
      print(current_value11)
   cs_sb = Spinbox(from_=0, to=10, width=5,textvariable=current_value11)
   cs_sb.place(x=380, y=320)
   # Choco Chips Pistachio Pocket
   ccpp = ImageTk.PhotoImage(Image.open("choco chips pistachio pocket.png"))
   label14 = Label(orderframe,image=ccpp,bg="#DAA520")
   label14.image = ccpp
   label14.place(x=580, y=35)
   ccpp_label = Label(orderframe,text="Choco Chips\nPistachio Pocket\n Rp.22.000",bg="#DAA520",font=("helvetica",17, "bold"))
   ccpp_label.place(x=580,y=215)
   global current_value12
   return_value(current_value12)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value12.get())
      print(current_value12)
   ccpp_sb = Spinbox(from_=0, to=10, width=5,textvariable=current_value12)
   ccpp_sb.place(x=645, y=320)
   # Chocolate Croissant
   chocolatec = ImageTk.PhotoImage(Image.open("Chocolate Croissant.png"))
   label15 = Label(orderframe,image=chocolatec,bg="#DAA520")
   label15.image = chocolatec
   label15.place(x=800, y=35)
   chocolatec_label = Label(orderframe,text="Chocolate Croissant\n Rp.20.000",bg="#DAA520",font=("helvetica",17, "bold"))
   chocolatec_label.place(x=800,y=215)
   global current_value13
   return_value(current_value13)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value13.get())
      print(current_value13)
   chocolatec_sb = Spinbox(from_=0, to=10, width=5,textvariable=current_value13)
   chocolatec_sb.place(x=900, y=320)
   # Green Tea Swiss Roll
   gtsr =ImageTk.PhotoImage(Image.open("green tea swiss roll.png"))
   label16 = Label(orderframe,image=gtsr,bg="#DAA520")
   label16.image = gtsr
   label16.place(x=20, y=315)
   gtsr_label = Label(orderframe,text="Green Tea\nSwiss Roll\n Rp.20.000",bg="#DAA520",font=("helvetica",17, "bold"))
   gtsr_label.place(x=60,y=485)
   global current_value14
   return_value(current_value14)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value14.get())
      print(current_value14)
   gtsr_sb = Spinbox(from_=0, to=10, width=5,textvariable=current_value14)
   gtsr_sb.place(x=100, y=600)
   # Smoked Beef Mushroom and Cheese
   sbmac =ImageTk.PhotoImage(Image.open("smoked beef mushroom and cheese.png"))
   label17 = Label(orderframe,image=sbmac,bg="#DAA520")
   label17.image = sbmac
   label17.place(x=290, y=315)
   sbmac_label = Label(orderframe,text="Smoked Beef Mushroom\n And Cheese\n Rp.30.000",bg="#DAA520",font=("helvetica",17, "bold"))
   sbmac_label.place(x=260,y=485)
   global current_value15
   return_value(current_value15)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value15.get())
      print(current_value15)
   sbmac_sb = Spinbox(from_=0, to=10, width=5,textvariable=current_value15)
   sbmac_sb.place(x=380, y=600)
   # Spicy Roast Beef
   srr =ImageTk.PhotoImage(Image.open("spicy roast beef.png"))
   label18 = Label(orderframe,image=srr,bg="#DAA520")
   label18.image = srr
   label18.place(x=565, y=315)
   srr_label = Label(orderframe,text="Spicy Roast Beef\n Rp.35.000",bg="#DAA520",font=("helvetica",17, "bold"))
   srr_label.place(x=575,y=500)
   global current_value16
   return_value(current_value16)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value16.get())
      print(current_value16)
   srr_sb = Spinbox(from_=0, to=10, width=5,textvariable=current_value16)
   srr_sb.place(x=645, y=600)
   # Tuna Black Pepper Bread
   tbb =ImageTk.PhotoImage(Image.open("tuna black pepper bread.png"))
   label19 = Label(orderframe,image=tbb,bg="#DAA520")
   label19.image = tbb
   label19.place(x=865, y=315)
   tbb_label = Label(orderframe,text="Tuna Blackpepper Bread\n Rp.30.000",bg="#DAA520",font=("helvetica",17, "bold"))
   tbb_label.place(x=805,y=500)
   global current_value17
   return_value(current_value17)
   def value_changed():
      # global current_value
      # current_value = current_value.get()
      return_value(current_value17.get())
      print(current_value17)
   tbb_sb = Spinbox(from_=0, to=10, width=5,textvariable=current_value17)
   tbb_sb.place(x=900, y=600)
   
   #Tombol Next
   NEXT = Button(orderframe, width=10, pady=7, text="Pay", bg='#8B4513', fg='white',command=bayar).place(x=1150, y=600)
   back = Button(orderframe, width=10, pady=7, text="Back", bg='#8B4513', fg='white',command=order).place(x=1050, y=600)
   simpan = Button(orderframe, width=10, pady=7, text="Save", bg='#8B4513', fg='white',command=value_changed).place(x=950, y=600)

def bayar ():
   global current_value
   bayarframe = Frame(coffee_shop,width= 1280 , height=720,bg="#DAA520")
   bayarframe.place(x= 0, y=0)
   nama_head= Label(bayarframe,text="Menu Pembelian",fg= "black", bg="#DAA520", font=("helvetica",23,"bold"))
   nama_head.place (x=200,y=90)
   label1 = Label(bayarframe,text="PAYMENT",bg="#DAA520",font=("helvetica",30,"bold"))
   label1.place (x=500,y=40)
   ll2 =int(current_value.get())*15000
   if ll2 != 0:
      label2 = Label(bayarframe,text=f"latte = {current_value.get()} ( Rp{ll2} )",bg="#DAA520",font=8)
      label2.place(x= 200,y= 140)
   ll3 =int(current_value1.get())*20000
   if ll3 != 0:
      label3 = Label(bayarframe,text=f"Green Tea Latte = {current_value1.get()} ( Rp{ll3} )",bg="#DAA520",font=8)
      label3.place(x= 200,y=180)
   ll4 =int(current_value2.get())*20000
   if ll4 != 0:
      label4 = Label(bayarframe,text=f"Black Tea Latte = {current_value2.get()} ( Rp{ll4} )",bg="#DAA520",font=8)
      label4.place(x= 200,y=220)
   ll5=int(current_value3.get())*18000
   if ll5 != 0:
      label5 = Label(bayarframe,text=f"Espresso = {current_value3.get()} ( Rp{ll5} )",bg="#DAA520",font=8)
      label5.place(x= 200,y=260)
   ll6 =int(current_value4.get())*18000
   if ll6 != 0:
      label6 = Label(bayarframe,text=f"Americano = {current_value4.get()} ( Rp{ll6} )",bg="#DAA520",font=8)
      label6.place(x= 200,y=300)
   ll7 =int(current_value5.get())*23000
   if ll7 != 0:
      label7 = Label(bayarframe,text=f"Caramel Machiato = {current_value5.get()} ( Rp{ll7} )",bg="#DAA520",font=8)
      label7.place(x= 200,y=340)
   ll8 =int(current_value6.get())*15000
   if ll8 != 0:
      label8 = Label(bayarframe,text=f"Cappucino = {current_value6.get()} ( Rp{ll8} )",bg="#DAA520",font=8)
      label8.place(x= 200,y=380)
   ll9 =int(current_value7.get())*25000
   if ll9 != 0:
      label9 = Label(bayarframe,text=f"Caramel Cream Frappuchino = {current_value7.get()} ( Rp{ll9} )",bg="#DAA520",font=8)
      label9.place(x= 200,y=420)
   ll10=int(current_value8.get())*25000
   if ll10 != 0:
      label10 = Label(bayarframe,text=f"Green Tea Cream Frappuchino = {current_value8.get()} ( Rp{ll10} )",bg="#DAA520",font=8)
      label10.place(x= 200,y=460)
   ll11 =int(current_value9.get())*25000
   if ll11 != 0:
      label11 = Label(bayarframe,text=f"Vanilla Cream Frappuchino = {current_value9.get()} ( Rp{ll11} )",bg="#DAA520",font=8)
      label11.place(x= 200,y=500)
   

   #order2
   ll12 =int(current_value10.get())*24000
   if ll12 != 0:
      label12 = Label(bayarframe,text=f"Apple and Cinnamon Crumble = {current_value10.get()} ( Rp{ll12} )",bg="#DAA520",font=8)
      label12.place(x= 600,y=140)
   ll13=int(current_value11.get())*25000
   if ll13 != 0:
      label13 = Label(bayarframe,text=f"Chicken Sandwich = {current_value11.get()} ( Rp{ll13} )",bg="#DAA520",font=8)
      label13.place(x= 600,y=180)
   ll14=int(current_value12.get())*22000
   if ll14 != 0:
      label14 = Label(bayarframe,text=f"Choco Chips Pistachio Pocket = {current_value12.get()} ( Rp{ll14} )",bg="#DAA520",font=8)
      label14.place(x= 600,y=220)
   ll15=int(current_value13.get())*20000
   if ll15 != 0:
      label15 = Label(bayarframe,text=f"Chocolate Croissant  = {current_value13.get()} ( Rp{ll15} )",bg="#DAA520",font=8)
      label15.place(x= 600,y=260)
   ll16=int(current_value14.get())*20000
   if ll16 != 0:
      label16 = Label(bayarframe,text=f"Green Tea Roll = {current_value14.get()} ( Rp{ll16} )",bg="#DAA520",font=8)
      label16.place(x= 600,y=300)
   ll17=int(current_value15.get())*30000
   if ll17 != 0:
      label17 = Label(bayarframe,text=f"Smoked Beef Mushroom And Cheese= {current_value15.get()} ( Rp{ll17} )",bg="#DAA520",font=8)
      label17.place(x= 600,y=340)
   ll18=int(current_value16.get())*35000
   if ll18 != 0:
      label18 = Label(bayarframe,text=f"Spicy Roast Beef = {current_value16.get()} ( Rp{ll18} )",bg="#DAA520",font=8)
      label18.place(x= 600,y=380)
   ll19=int(current_value17.get())*30000
   if ll19 != 0:
      label19 = Label(bayarframe,text=f"Tuna Blackpepper Bread = {current_value17.get()} ( Rp{ll19} )",bg="#DAA520",font=8)
      label19.place(x= 600,y=420)
      

   global total_bills
   total_bills = ll2 + ll3 + ll4 + ll5 + ll6 + ll7 + ll8 + ll9 + ll10 + ll11 + ll12 + ll13 + ll14 + ll15 + ll16 + ll17 + ll18 + ll19
   bills = Label(text=f"Total Harga Rp.{total_bills}", font=("Helvetica", 30, "bold"), bg="#DAA520")
   bills.place(x=200, y=580)
   a = [ll2, ll3, ll4, ll5, ll6, ll7, ll8, ll9, ll10, ll11, ll12, ll13, ll14, ll15, ll16, ll17, ll18, ll19]
   b = [i for i, e in enumerate(a) if e != 0]
   print(b)

   namapelanggan=pelanggan_var.get()
   datetime_object = datetime.datetime.now()
   
   
   data = {
   'Nama': [namapelanggan],
   'Nomer Menu' : [b],
   'Total Harga':[total_bills],
   'Waktu Pembelian':[datetime_object]
   }

   df = pd.DataFrame(data)
   df.to_csv('Tagihan.csv', mode='a', index=False, header=False)
   
   back = Button(bayarframe, width=10, pady=7, text="Back", bg='#8B4513', fg='white',command=order2).place(x=1000, y=600)
   selesai =Button(bayarframe, width=10, pady=7, text="Finish", bg='#8B4513', fg='white',command=coffee_shop.destroy).place(x=1100, y=600)
   



coffee_shop.mainloop()


