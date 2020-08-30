from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time;

class Customer:

     def __init__(self,roo):
         self.root = root
         self.root.title("Customer Billing system")
         self.root.geometry("1450x750+0+0")
         self.root.config(background="powder blue")
         

         ABC =Frame(self.root, bg="powder blue", bd=70, relief=RIDGE)
         ABC.grid()
         ABC1 =Frame(ABC, bd=30, width=2050, height=540, padx=20, relief=RIDGE,bg="powder blue")
         ABC1.grid(row=0, column=0 ,columnspan=4, sticky=W)
         ABC2 =Frame(ABC, bd=30, width=2050, height=488, padx=20, relief=RIDGE,bg="cadet blue")
         ABC2.grid(row=1, column=0, sticky=W)
         ABC3 =Frame(ABC, bd=14, width=2050, height=488, padx=20, relief=RIDGE,bg="powder blue")
         ABC3.grid(row=1, column=1, sticky=W)
         ABC4 =Frame(ABC, bd=14, width=2050, height=488, padx=20, relief=RIDGE,bg="cadet blue")
         ABC4.grid(row=1, column=2, sticky=W)
         ABC5 =Frame(ABC4, bd=14, width=370, height=340, padx=20, relief=RIDGE,bg="powder blue")
         ABC5.grid(row=0, column=0, sticky=W)
         ABC6 =Frame(ABC4, bd=14, width=370, height=150, padx=20, relief=RIDGE,bg="cadet blue")
         ABC6.grid(row=1, column=0 ,columnspan=4, sticky=W)

         Datel =StringVar() 
         Timel = StringVar()
         Datel.set(time.strftime("%d/%m/%y"))
         Timel.set(time.strftime("%H:%M:%S"))
         #============================================================================================================================
         
         CustomerRef=StringVar()
         Name=StringVar()
         Mobile=StringVar()
         Gender=StringVar()
         Email=StringVar()
         Address=StringVar()
         PinCode=StringVar()
         Nationality=StringVar()
         Noofpeoples=StringVar()
         SubTotal=StringVar()
         PaidTax=StringVar()
         TotalCost=StringVar()

         CustomerRef.set(random.randint(19800, 9875648))

         var1=IntVar()
         var2=IntVar()
         var3=IntVar()
         var4=IntVar()
         var5=IntVar()
         var6=IntVar()
         var7=IntVar()
         var8=IntVar()
         var9=IntVar()
     
          
         Tea=StringVar()
         Coffee=StringVar()
         Icecream=StringVar()
         Choclateshake=StringVar()
         Oreoshake=StringVar()
         Bananashake=StringVar()
         Coldcoffee=StringVar()
         Icetea=StringVar()
         SubTotal=StringVar()
         PaidTax=StringVar()
         TotalCost=StringVar()


         var1.set("0")
         var2.set("0")
         var3.set("0")
         var4.set("0")
         var5.set("0")
         var6.set("0")
         var7.set("0")
         var8.set("0")               



         
         self.lblTitle=Label(ABC1, textvariable=Datel,font=('Arial',30,'bold'),pady=9,
                               bd=5,bg='cadet blue', fg="Cornsilk").grid(row=0,column=0)
                   
         self.lb1Title=Label(ABC1, text="\tCustomer Billing system\t\t",font=('Arial',30,'bold'),pady=9,
                     bd=5,bg='cadet blue', fg="Cornsilk", justify= CENTER).grid(row=0,column=1)
                   
         self.lb1Title=Label(ABC1, textvariable=Timel,font=('Arial',30,'bold'),pady=9,
                     bd=5,bg='cadet blue', fg="Cornsilk").grid(row=0,column=2)
         #=============================================EXIT=========================================================================================
         def iExit():
              iExit = tkinter.messagebox.askyesno("Customer Billing system","Confirm if you want to exit")
              if iExit > 0:
                   root.destroy()
                   return
          #==========================================================================================================================================

         def Reset():
              self.txtReceipt.delete("1.0",END)
              Tea.set("0")
              Coffee.set("0")
              Icecream.set("0")
              Choclateshake.set("0")
              Oreoshake.set("0")
              Bananashake.set("0")
              Coldcoffee.set("0")
              Icetea.set("0")
              TotalCost.set("0")
              SubTotal.set("0")
              PaidTax.set("0")

              var1.set(0)
              var2.set(0)
              var3.set(0)
              var4.set(0)
              var5.set(0)
              var6.set(0)
              var7.set(0)
              var8.set(0)

              

              CustomerRef.set("")
              Name.set("")
              Mobile.set("")
              Gender.set("")
              Email.set("")
              Address.set("")
              Pincode.set("")
              Nataniolity.set("")
              Noofpeoples.set("")
              TotalCost.set("")
              SubTotal.set("")
              PaidTax.set("")
              
         #=====================================================================================================================================

         def Save():
             outwb = openpyl.Workbook()
             ws = outwb.active
             ws.append([Item1, Item2, Item3, Item4, Item5, Item6, Item7, Item8])
             outwb.save('result.XlSX')
             outwb.close()


          #=============================================================================================================================================
         def chkTea():
              if (var1.get() == 1):
                  self.txtTea.configure(state= NORMAL)
                  self.txtTea.delete(0,END)
                  self.txtTea.focus()
                  Tea.set("")
              elif var1.get()== 0:
                  self.txtTea.configure(state= DISABLED)



         def chkCoffee():
              if (var2.get() == 1):
                   self.txtCoffee.configure(state= NORMAL)
                   self.txtCoffee.delete(0,END)
                   self.txtCoffee.focus()
                   Coffee.set("")
              elif var2.get()== 0:
                   self.txtCoffee.configure(state= DISABLED)
                   Coffee.set("0")
                   
             
         def chkIcecream():
              if (var3.get() == 1):
                   self.txtIcecream.configure(state= NORMAL)
                   self.txtIcecream.delete(0,END)
                   self.txtIcecream.focus()
                   Icecream.set("")
              elif var3.get()== 0:
                   self.txtIcecream.configure(state= DISABLED)
                   Icecream.set("0")



         def chkChoclateshake():
              if (var4.get() == 1):
                   self.txtChoclateshake.configure(state= NORMAL)
                   self.txtChoclateshake.delete(0,END)
                   self.txtChoclateshake.focus()
                   Choclateshake.set("")
              elif var4.get()== 0:
                   self.txtChoclateshake.configure(state= DISABLED)
                   Choclateshake.set("0")




         def chkOreoshake():
              if (var5.get() == 1):
                   self.txtOreoshake.configure(state= NORMAL)
                   self.txtOreoshake.delete(0,END)
                   self.txtOreoshake.focus()
                   Oreoshake.set("")
              elif var5.get()== 0:
                   self.txtOreoshake.configure(state= DISABLED)
                   Oreoshake.set("0")




         def chkBananashake():
              if (var6.get() == 1):
                   self.txtBananashake.configure(state= NORMAL)
                   self.txtBananashake.delete(0,END)
                   self.txtBananashake.focus()
                   Bananashake.set("")
              elif var6.get()== 0:
                   self.txtBananashake.configure(state= DISABLED)
                   Bananashake.set("0")




         def chkColdcoffee():
              if (var7.get() == 1):
                   self.txtColdcoffee.configure(state= NORMAL)
                   self.txtColdcoffee.delete(0,END)
                   self.txtColdcoffee.focus()
                   Coldcoffee.set("")
              elif var7.get()== 0:
                   self.txtColdcoffee.configure(state= DISABLED)
                   Coldcoffee.set("0")


         def chkIcetea():
              if (var8.get() == 1):
                   self.txtIcetea.configure(state= NORMAL)
                   self.txtIcetea.delete(0,END)
                   self.txtIcetea.focus()
                   Icetea.set("")
              elif var8.get()== 0:
                   self.txtIcetea.configure(state= DISABLED)
                   Icetea.set("0")
          #=====================================================================================================================================
                   
                        
         def costOfItem():
             CustomerRef.set(random.randint(19800, 9875648))
             Item1=float(Tea.get())
             Item2=float(Coffee.get())
             Item3=float(Icecream.get())
             Item4=float(Choclateshake.get())
             Item5=float(Oreoshake.get())
             Item6=float(Bananashake.get())
             Item7=float(Coldcoffee.get())
             Item8=float(Icetea.get())


             costOfItem = (Item1 * 10) + (Item2 * 20)\
                          + (Item3 * 30) + (Item4 * 40) + (Item5 * 50) + (Item6 * 60) + (Item7* 70) + (Item8* 80)
             SubTotalofITEMS = "Rs.", str('%.2f'% costOfItem)
          
             SubTotal.set(SubTotalofITEMS)
             Tax="Rs.", str('%.2f'% ((costOfItem) * 0.18))
             PaidTax.set(Tax)
             TTax = ((costOfItem) * 0.18)

             TCost = "Rs.", str('%.2f'% (costOfItem + TTax))
             TotalCost.set(TCost)


             

             self.txtReceipt.insert(END,'Customer Ref:\t\t\t\t'+CustomerRef.get()+"\n")
             self.txtReceipt.insert(END,'\t\t\t\t\t\t\t\t\t\t\t'+"\n")
             self.txtReceipt.insert(END,'ITEMS\t\t\t\t\t'+"Qantity \n")
             self.txtReceipt.insert(END,'\nTea: \t\t\t\t\t' + str(Tea.get())+"\n")
             self.txtReceipt.insert(END,'Coffee: \t\t\t\t\t'+ str(Coffee.get())+"\n")
             self.txtReceipt.insert(END,'Icecream: \t\t\t\t\t'+ str(Icecream.get())+"\n")
             self.txtReceipt.insert(END,'Choclateshake: \t\t\t\t\t'+ str(Choclateshake.get())+"\n")
             self.txtReceipt.insert(END,'Oreoshake: \t\t\t\t\t'+ str(Oreoshake.get())+"\n")
             self.txtReceipt.insert(END,'Bananashake: \t\t\t\t\t'+ str(Bananashake.get())+"\n")
             self.txtReceipt.insert(END,'Coldcoffee: \t\t\t\t\t'+ str(Coldcoffee.get())+"\n")
             self.txtReceipt.insert(END,'Icetea: \t\t\t\t\t'+ str(Icetea.get())+"\n")
            
            

             self.txtReceipt.insert(END, '\nTax:\t\t\t' + PaidTax.get()+"\n")
             self.txtReceipt.insert(END, '\n SubTotal:\t\t\t' + str(SubTotal.get())+"\n")
             self.txtReceipt.insert(END, '\nTotalCost:\t\t\t' + str(TotalCost.get()))
             
             
          
                        

 
          #=============================================RECIPT COLOUR=====================================================================================
         self.txtReceipt = Text(ABC5, height =19, width =43, bd=10 ,font=('arial',9,'bold'))
         self.txtReceipt .grid(row=0,column=0)
          
         
         #=====================================================================================================================================
        
         
         self.lblcus_Ref=Label(ABC2, font=('arial',23,'bold'),text="Customer Ref:",padx=7,pady=5,fg="cornsilk",
                               bg="cadet blue",)
         self.lblcus_Ref.grid (row=0,column=0, sticky =W)
         self.txtcus_Ref =Entry(ABC2, font=('arial',12,'bold'),textvariable=CustomerRef,width =15)
         self.txtcus_Ref.grid(row=0, column=1, pady=1, padx=20)
         

         self.lblName =Label(ABC2, font=('arial',19,'bold'),text="Name:",padx=5,pady=5,fg="cornsilk",
                             bg="cadet blue",)
         self.lblName.grid (row=1,column=0, sticky =W)
         self.txtName=Entry(ABC2, font=('arial',12,'bold'),textvariable=Name, width =15)
         self.txtName.grid(row=1, column=1,pady=15, padx=20)


         self.lblMobile =Label(ABC2, font=('arial',19,'bold'),text="Mobile:",padx=5,pady=5,fg="cornsilk",
                                  bg="cadet blue",)
         self.lblMobile.grid (row=2,column=0, sticky =W)
         self.txtMobile =Entry(ABC2, font=('arial',12,'bold'),textvariable=Mobile, width =15)
         self.txtMobile.grid(row=2, column=1, pady=15, padx=20)


         
         self.lblGender =Label(ABC2, font=('arial',19,'bold'),text="Gender:",padx=5,pady=5,fg="cornsilk",
                               bg="cadet blue",)
         self.lblGender.grid (row=3,column=0, sticky =W)
         self.txtGender=Entry(ABC2, font=('arial',12,'bold'),textvariable =Gender, width =15)
         self.txtGender.grid(row=3,column=1,pady=15, padx=20)

         self.lblEmail =Label(ABC2, font=('arial',19,'bold'),text="Email:",padx=5,pady=5,fg="cornsilk",
                              bg="cadet blue",)
         self.lblEmail.grid (row=4,column=0, sticky =W)
         self.txtEmail=Entry(ABC2, font=('arial',12,'bold'),textvariable =Email, width =15)
         self.txtEmail.grid(row=4,column=1,pady=15, padx=20)
         

         self.lblAddress =Label(ABC2, font=('arial',19,'bold'),text="Address:",padx=5,pady=5,fg="cornsilk",
                                bg="cadet blue",)
         self.lblAddress.grid (row=5,column=0, sticky =W)
         self.txtAddress=Entry(ABC2, font=('arial',12,'bold'),textvariable =Address, width =15)
         self.txtAddress.grid(row=5,column=1,pady=15, padx=20)


         self.lblPinCode =Label(ABC2, font=('arial',19,'bold'),text="PinCode:",padx=5,pady=5,fg="cornsilk",
                              bg="cadet blue",)
         self.lblPinCode.grid (row=6,column=0, sticky =W)
         self.txtPinCode=Entry(ABC2, font=('arial',12,'bold'),textvariable =PinCode, width =15)
         self.txtPinCode.grid(row=6,column=1,pady=15, padx=20)
         
         self.lblNationality =Label(ABC2, font=('arial',19,'bold'),text="Nationality:",padx=5,pady=5,fg="cornsilk",
                          bg="cadet blue",)
         self.lblNationality.grid (row=7,column=0, sticky =W)
         self.txtNationality=Entry(ABC2, font=('arial',12,'bold'),textvariable =Nationality, width =15)
         self.txtNationality.grid(row=7,column=1,pady=15, padx=20)

         self.lblNoofpeoples =Label(ABC2, font=('arial',19,'bold'),text="No of peoples:",padx=5,pady=5,fg="cornsilk",
                                  bg="cadet blue",)
         self.lblNoofpeoples.grid (row=8,column=0, sticky =W)
         self.txtNoofpeoples =Entry(ABC2, font=('arial',12,'bold'),textvariable=Noofpeoples, width =15)
         self.txtNoofpeoples.grid(row=8, column=1, pady=15, padx=20)



         
          #================================================================================================================================     

        
                    
         #=====================================================================================================================================
         
         self.lbl= Checkbutton(ABC3, text="Tea ", variable=var1, onvalue = 1, offvalue = 0,
                         font=('arial',15,'bold'),bg="powder blue",command=chkTea).grid (row=1, sticky=W)
         self.txtTea = Entry(ABC3, font=('arial',12,'bold'),textvariable=Tea, bd=6,
                              width=9, justify='left',state= DISABLED)
         self.txtTea.grid(row=1,column=2)
                        
          
         self.Coffee = Checkbutton(ABC3, text="Coffee ", variable=var2, onvalue = 1, offvalue = 0,
                         font=('arial',15,'bold'),bg="powder blue",command=chkCoffee).grid (row=2, sticky=W)
         self.txtCoffee = Entry(ABC3, font=('arial',12,'bold'),textvariable=Coffee, bd=6,
                              width=9, justify='left',state= DISABLED)
         self.txtCoffee.grid(row=2,column=2)
         

         
         self.Icecream = Checkbutton(ABC3, text="Ice Cream ", variable=var3, onvalue = 1, offvalue = 0,
                         font=('arial',15,'bold'),bg="powder blue",command=chkIcecream).grid (row=3, sticky=W)
         self.txtIcecream = Entry(ABC3, font=('arial',12,'bold'),textvariable=Icecream, bd=6,
                              width=9, justify='left',state= DISABLED)
         self.txtIcecream.grid(row=3,column=2)
         
          
         self.Choclateshake = Checkbutton(ABC3, text="Choclate shake ", variable=var4, onvalue = 1, offvalue = 0,
                         font=('arial',15,'bold'),bg="powder blue",command=chkChoclateshake).grid (row=4, sticky=W)
         self.txtChoclateshake = Entry(ABC3, font=('arial',12,'bold'),textvariable=Choclateshake, bd=6,
                              width=9, justify='left',state= DISABLED)
         self.txtChoclateshake.grid(row=4,column=2)


          
         self.Oreoshake = Checkbutton(ABC3, text="Oreo shake ", variable=var5, onvalue = 1, offvalue = 0,
                         font=('arial',15,'bold'),bg="powder blue",command=chkOreoshake).grid (row=5, sticky=W)
         self.txtOreoshake = Entry(ABC3, font=('arial',12,'bold'),textvariable=Oreoshake, bd=6,
                              width=9, justify='left',state= DISABLED)
         self.txtOreoshake.grid(row=5,column=2)
         
          
         self.Bananashake = Checkbutton(ABC3, text="Banana shake ", variable=var6, onvalue = 1, offvalue = 0,
                         font=('arial',15,'bold'),bg="powder blue",command=chkBananashake).grid (row=6, sticky=W)
         self.txtBananashake = Entry(ABC3, font=('arial',12,'bold'),textvariable=Bananashake, bd=6,
                              width=9, justify='left',state= DISABLED)
         self.txtBananashake.grid(row=6,column=2)
         
          
         self.Coldcoffee = Checkbutton(ABC3, text="Cold coffee ", variable=var7, onvalue = 1, offvalue = 0,
                         font=('arial',15,'bold'),bg="powder blue",command=chkColdcoffee).grid (row=7, sticky=W)
         self.txtColdcoffee = Entry(ABC3, font=('arial',12,'bold'),textvariable=Coldcoffee, bd=6,
                              width=9, justify='left',state= DISABLED)
         self.txtColdcoffee.grid(row=7,column=2)
         


         self.Icetea = Checkbutton(ABC3, text="Ice Tea ", variable=var8, onvalue = 1, offvalue = 0,
                         font=('arial',15,'bold'),bg="powder blue",command=chkIcetea).grid (row=8, sticky=W)
         self.txtIcetea = Entry(ABC3, font=('arial',12,'bold'),textvariable=Icetea, bd=6,
                              width=9, justify='left',state= DISABLED)
         self.txtIcetea.grid(row=8,column=2)


#===============================================heading tax and total sum=====================================================================================
         self.lblspace=Label(ABC3, text="Tax and Total sum",font=('arial',19,'bold') ,pady=1, bd=4,bg="cadet Blue",
                             fg="cornsilk",width=20, justify=CENTER).grid(row=9,column=0, columnspan=4)


         
         #==========================================================================================================================================================

         self.lblPaidTax = Label(ABC3,font=('arial',12,'bold'),text="Paid Tax:", bd=4,bg="powder blue",fg="black",)
         self.lblPaidTax.grid (row=10,column=0, sticky =W,)
         self.txtPaidTax= Entry(ABC3, font=('arial',10,'bold'),textvariable =PaidTax, bd=4, bg="white",
                                width =10, justify=LEFT)
         self.txtPaidTax.grid(row=10,column=2,pady=12, padx=20)


         self.lblSubTotal = Label(ABC3,font=('arial',12,'bold'),text="Sub Total:", bd=4,bg="powder blue",fg="black",)
         self.lblSubTotal.grid (row=11,column=0, sticky =W)
         self.txtSubTotal= Entry(ABC3, font=('arial',10,'bold'),textvariable =SubTotal,bd=4, bg="white",
                                 width =10, justify=LEFT)
         self.txtSubTotal.grid(row=11,column=2,pady=12, padx=20)
         
         self.lblTotalCost =Label(ABC3,font=('arial',12,'bold'),text="Total Cost:", bd=4,bg="powder blue",fg="black",)
         self.lblTotalCost.grid (row=12,column=0, sticky =W)
         self.txtTotalCost=Entry(ABC3, font=('arial',10,'bold'),textvariable =TotalCost, bd=4, bg="white",
                                 width =10)
         self.txtTotalCost.grid(row=12,column=2,pady=12, padx=20)


         #============================================Buttons========================================================================================
         self.btnTotal = Button(ABC6, padx=13, pady=5,bd=3,fg="black",font=('arial',14,'bold'), width =3, height=2,
                                bg="powder blue", text="Total",command=costOfItem).grid(row=0,column=1)
         
         self.btnReset = Button(ABC6, padx=13, pady=5,bd=3,fg="black",font=('arial',14,'bold'), width =3, height=2,
                                bg="powder blue", text="Reset",command=Reset).grid(row=0,column=2)
         
         self.btnExit = Button(ABC6, padx=13, pady=5,bd=3,fg="black",font=('arial',14,'bold'), width =3, height=2,
                                bg="powder blue", text="Exit",command=iExit).grid(row=0,column=3)
         
         self.btnSave = Button(ABC6, padx=13, pady=5,bd=3,fg="black",font=('arial',14,'bold'), width =3, height=2,
                                bg="powder blue", text="Save",command=Save).grid(row=0,column=4)

         self.btnPrint = Button(ABC6, padx=13, pady=5,bd=3,fg="black",font=('arial',14,'bold'), width =3, height=2,
                                bg="powder blue", text="Print",).grid(row=0,column=5)


         
         #===================================================================================================================================

         

     

if __name__=='__main__':
     root = Tk()
     application = Customer(root)
     root.mainloop()
