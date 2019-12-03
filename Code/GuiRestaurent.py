from tkinter import*
import random
import time;
import datetime
from tkinter import Tk, StringVar, ttk, messagebox

class Restaurant:
    def __init__(self, root):
        self.root = root
        #master.title("A simple GUI")
        root.title("Restaurant Management")
        root.configure(background="Blue")

#----------------------Frame 1--------------------------------------------------
        Tops= Frame (root,width=1350,height=100, bd=10,relief="raise",bg="Blue")
        Tops.pack(side=TOP)

        #Tops.config(BaBackground="white")
        lblTitle=Label(Tops, font=('arial', 25,'bold'), text="\t\t\t  KHANA KHAJANA \t\t\t",foreground="Blue")
        lblTitle.grid(row=0,column=0)

        BottomMainFrame= Frame (root, width=1350, height=1550, bd=12,relief="raise",bg="Blue")
        BottomMainFrame.pack(side=BOTTOM)

        f1= Frame (BottomMainFrame, width=450, height=650, bd=12,relief="raise")
        f1.pack(side=LEFT)

        f2=Frame (BottomMainFrame, width=450, height=650, bd=12,relief="raise")
        f2.pack(side=LEFT)

        f2TOP= Frame (f2, width=450, height=350, bd=4,relief="raise")
        f2TOP.pack(side=TOP)

        f2BOTTOM= Frame (f2, width=450, height=300, bd=4,relief="raise")
        f2BOTTOM.pack(side=BOTTOM)


        f3= Frame (BottomMainFrame, width=450, height=650, bd=12,relief="raise")
        f3.pack(side=RIGHT)

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        var10=IntVar()
        var11=IntVar()
        var12=IntVar()
        var13=IntVar()
        var14=IntVar()
        var15=IntVar()
        var16=IntVar()
        var17=IntVar()
        var18=IntVar()
        var19=IntVar()
        var20=IntVar()
        var21=IntVar()
        var22=IntVar()
        var23=IntVar()
        var24=IntVar()
        var25=IntVar()
        var26=IntVar()
        var27=IntVar()
        var28=IntVar()
        var29=IntVar()
        var30=IntVar()
        var31=IntVar()
        var32=IntVar()
        var33=IntVar()
        var34=StringVar()
        varChange=StringVar()
        varSubTotal=StringVar()
        varTotal=StringVar()
        varVat=StringVar()
        varPayment=IntVar()


        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var18.set(0)
        var19.set(0)
        var20.set(0)
        var21.set(0)
        var22.set(0)
        var23.set(0)
        var24.set(0)
        var25.set(0)
        var26.set(0)
        var27.set(0)
        var28.set(0)
        var29.set(0)
        var30.set(0)
        var31.set(0)
        var32.set(0)
        var33.set(0)
        var34.set(0)
        varChange.set('0')
        varSubTotal.set('0')
        varTotal.set('0')
        varVat.set('0')
        varPayment.set(" ")


        #Variables for Light Meals
        varFries=StringVar()
        varMomo=StringVar()
        varWings=StringVar()
        varNachos=StringVar()
        varOrings=StringVar()


        #Variables for Heavy Meals
        varSubSandwich=StringVar()
        varBBurger=StringVar()
        varCBurger=StringVar()
        varFriedrice=StringVar()
        varBBQChicken=StringVar()

        #Variables value for Light Meals


        varFries.set('0')
        varMomo.set('0')
        varWings.set('0')
        varNachos.set('0')
        varOrings.set('0')

        #Variables value for Heavy Meal

        varSubSandwich.set('0')
        varBBurger.set('0')
        varCBurger.set('0')
        varFriedrice.set('0')
        varBBQChicken.set('0')



        lblMeal=Label(f1, font=('arial', 18,'bold'), text="         Crispy Crunch ")
        lblMeal.grid(row=0,column=0)
        def chkFries():
            if (var1.get()==1):
                txtFries.configure(state=NORMAL)
                varFries.set("")
            elif(var1.get()==0):
                txtFries.configure(state=DISABLED)
                varFries.set("0")


        def chkMomo():
            if (var2.get()==1):
                txtMomo.configure(state=NORMAL)
                varMomo.set("")
            elif(var2.get()==0):
                txtMomo.configure(state=DISABLED)
                varMomo.set("0")
        def chkWings():
            if (var3.get()==1):
                txtWings.configure(state=NORMAL)
                varWings.set("")
            elif(var3.get()==0):
                txtWings.configure(state=DISABLED)
                varWings.set("0")
        def chkNachos():
            if (var4.get()==1):
                txtNachos.configure(state=NORMAL)
                varNachos.set("")
            elif(var4.get()==0):
                txtNachos.configure(state=DISABLED)
                varNachos.set("0")

        def chkOrings():
            if (var5.get()==1):
                txtORings.configure(state=NORMAL)
                varOrings.set("")
            elif(var5.get()==0):
                txtORings.configure(state=DISABLED)
                varOrings.set("0")
        def chkSubdSanwich():
            if (var7.get()==1):
                txtSubdSanwich.configure(state=NORMAL)
                varSubSandwich.set("")
            elif(var7.get()==0):
                txtSubdSanwich.configure(state=DISABLED)
                varSubSandwich.set("0")
        def chkBBurger():
            if (var8.get()==1):
                txtBBurger.configure(state=NORMAL)
                varBBurger.set("")
            elif(var8.get()==0):
                txtBBurger.configure(state=DISABLED)
                varBBurger.set("0")

        def chkCBurger():
            if (var9.get()==1):
                txtCBurger.configure(state=NORMAL)
                varCBurger.set("")
            elif(var9.get()==0):
                txtCBurger.configure(state=DISABLED)
                varCBurger.set("0")

        def chkFriedRice():
            if (var10.get()==1):
                txtFriedRice.configure(state=NORMAL)
                varFriedrice.set("")
            elif(var10.get()==0):
                txtFriedRice.configure(state=DISABLED)
                varFriedrice.set("0")

        def chkCBBQChicken():
            if (var11.get()==1):
                txtCBBQChicken.configure(state=NORMAL)
                varBBQChicken.set("")
            elif(var11.get()==0):
                txtCBBQChicken.configure(state=DISABLED)
                varBBQChicken.set("0")

        def chkLemonade():
            if (var21.get()==1):
                txtLemonade.configure(state=NORMAL)
                varLemonade.set("")
            elif(var21.get()==0):
                txtLemonade.configure(state=DISABLED)
                varLemonade.set("0")
        def chkBlueMint():
            if (var22.get()==1):
                txtBlueMint.configure(state=NORMAL)
                varBlueMint.set("")
            elif(var22.get()==0):
                txtBlueMint.configure(state=DISABLED)
                varBlueMint.set("0")

        def chkColdCoffee():
            if (var23.get()==1):
                txtColdCoffee.configure(state=NORMAL)
                varColdCoffee.set("")
            elif(var23.get()==0):
                txtColdCoffee.configure(state=DISABLED)
                varColdCoffee.set("0")

        def chkMilkshake():
            if (var24.get()==1):
                txtMilkshake.configure(state=NORMAL)
                varMilkshake.set("")
            elif(var24.get()==0):
                txtMilkshake.configure(state=DISABLED)
                varMilkshake.set("0")

        def chkBrowni():
            if (var25.get()==1):
                txtBrowni.configure(state=NORMAL)
                varBrowni.set("")
            elif(var25.get()==0):
                txtBrowni.configure(state=DISABLED)
                varBrowni.set("0")

        def chkCupcake():
            if (var26.get()==1):
                txtCupcake.configure(state=NORMAL)
                varCupcake.set("")
            elif(var26.get()==0):
                txtCupcake.configure(state=DISABLED)
                varCupcake.set("0")

        def chkVanillaPastry():
            if (var27.get()==1):
                txtVanillaPastry.configure(state=NORMAL)
                varVannilaPastry.set("")
            elif(var27.get()==0):
                txtVanillaPastry.configure(state=DISABLED)
                varVannilaPastry.set("0")
        def chkBlackforestPastry():
            if (var28.get()==1):
                txtBlackforestPastry.configure(state=NORMAL)
                varBlackForestPastry.set("")
            elif(var28.get()==0):
                txtBlackforestPastry.configure(state=DISABLED)
                varBlackForestPastry.set("0")
        def chkIcecreamV():
            if (var30.get()==1):
                txtIcecreamV.configure(state=NORMAL)
                varIcecreamV.set("")
            elif(var30.get()==0):
                txtIcecreamV.configure(state=DISABLED)
                varIcecreamV.set("0")

        def chkIcecreamC():
            if (var31.get()==1):
                txtIcecreamC.configure(state=NORMAL)
                varIcecreamC.set("")
            elif(var31.get()==0):
                txtIcecreamC.configure(state=DISABLED)
                varIcecreamC.set("0")
        def chkIcecreamM():
            if (var32.get()==1):
                txtIcecreamM.configure(state=NORMAL)
                varIcecreamM.set("")
            elif(var32.get()==0):
                txtIcecreamM.configure(state=DISABLED)
                varIcecreamM.set("0")
        def chkIcecreamS():
            if (var33.get()==1):
                txtIcecreamS.configure(state=NORMAL)
                varIcecreamS.set("")
            elif(var33.get()==0):
                txtIcecreamS.configure(state=DISABLED)
                varIcecreamS.set("0")
        def chkVarpayment():
            if (var31.get()==1):
                txtIcecreamC.configure(state=NORMAL)
                varIcecreamC.set("")
            elif(var31.get()==0):
                txtIcecreamC.configure(state=DISABLED)
                varIcecreamC.set("0")
        def costofmeal():
                meal1=float(varFries.get())
                meal2=float(varMomo.get())
                meal3=float(varWings.get())
                meal4=float(varNachos.get())
                meal5=float(varOrings.get())
                meal6=float(varSubSandwich.get())
                meal7=float(varBBurger.get())
                meal8=float(varCBurger.get())
                meal9=float(varFriedrice.get())
                meal10=float(varBBQChicken.get())
                meal11=float(varLemonade.get())
                meal12=float(varBlueMint.get())
                meal13=float(varColdCoffee.get())
                meal14=float(varMilkshake.get())
                meal15=float(varBrowni.get())
                meal16=float(varCupcake.get())
                meal17=float(varVannilaPastry.get())
                meal18=float(varBlackForestPastry.get())
                meal19=float(varIcecreamV.get())
                meal20=float(varIcecreamC.get())
                meal21=float(varIcecreamM.get())
                meal22=float(varIcecreamS.get())

                iTotal1=((meal1 * 120 )+ (meal2 * 150)+ (meal3 * 220) + (meal4 * 130) + (meal5 * 180) )
                iTotal2=((meal6 * 145) + (meal7 * 140) + (meal8 * 150) + (meal9 * 230) + (meal10 * 220))
                iTotal3=((meal11 * 100) + (meal12 * 110) + (meal13 * 100) + (meal14 * 100))
                iTotal4=((meal15 * 80) + (meal16* 60) + (meal17 * 50 )+ (meal18*60))
                iTotal5=((meal19*100) + (meal20*100) + (meal21*100 )+ (meal22*100))


                if (var34.get()=="Cash"):
                   # ichange=float(varPayment.get())
                    icost=(iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
                    iVat=(icost * 15)/100
                    #cChange=(ichange-(icost+iVat))
                    varChange.set(cChange)
                elif(var34.get()=="Master Card" or "Visa Card" or "bKash"):
                    varPayment.set(" ")
                    icost=(iTotal1+iTotal2+iTotal3+iTotal4+iTotal5)
                    iVat=(icost * 15)/100
                    varVat.set(iVat)
                    varSubTotal.set(icost)
                    varTotal.set(icost+iVat)

        Fries= Checkbutton (f1, text="Fries  \t\t 120 BDT",variable=var1,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkFries).grid(row=1,column=0,sticky='w')
        txtFries=Entry(f1,font=('arial',13,'bold'), textvariable=varFries ,width=6,justify='right',state=DISABLED)
        txtFries.grid(row=1,column =1)

        Momo= Checkbutton (f1, text="Chicken Momo\t 150 BDT",variable=var2,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkMomo).grid(row=2,column=0,sticky='w')
        txtMomo= Entry(f1,font=('arial',13,'bold'), textvariable=varMomo ,width=6,justify='right',state=DISABLED)
        txtMomo.grid(row=2,column =1)

        Wings= Checkbutton (f1, text="Chicken Wings\t 220 BDT",variable=var3,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkWings).grid(row=3,column=0,sticky='w')
        txtWings= Entry(f1,font=('arial',13,'bold'), textvariable=varWings,width=6,justify='right',state=DISABLED)
        txtWings.grid(row=3,column =1)




        #----------------------Main Meals---------------
        lblMeal=Label(f1, font=('arial', 18,'bold'), text="    Chicken, Roti & Rice")
        lblMeal.grid(row=6,column=0)

        SubSandwich= Checkbutton (f1, text="SubSandwich\t 145 BDT",variable=var7,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkSubdSanwich).grid(row=7,column=0,sticky='w')
        txtSubdSanwich= Entry(f1,font=('arial',13,'bold'), textvariable=varSubSandwich ,width=6,justify='right',state=DISABLED)
        txtSubdSanwich.grid(row=7,column =1)

        BBurger= Checkbutton (f1, text="Beef Burger\t 140 BDT",variable=var8,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkBBurger).grid(row=8,column=0,sticky='w')
        txtBBurger= Entry(f1,font=('arial',13,'bold'), textvariable=varBBurger ,width=6,justify='right',state=DISABLED)
        txtBBurger.grid(row=8,column =1)

        #CBurger= Checkbutton (f1, text="Chicken Burger\t 150 BDT",variable=var9,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkCBurger).grid(row=9,column=0,sticky='w')
        #txtCBurger= Entry(f1,font=('arial',13,'bold'), textvariable=varCBurger,width=6,justify='right',state=DISABLED)
        #txtCBurger.grid(row=9,column =1)


        FriedRice= Checkbutton (f1, text="Fried Rice Set Menu 230 BDT",variable=var10,onvalue=1, offvalue=0,font=('arial',13,'bold')).grid(row=10,column=0,sticky='w')
        txtFriedRice= Entry(f1,font=('arial',13,'bold'), textvariable=varFriedrice ,width=6,justify='right',state=DISABLED)
        txtFriedRice.grid(row=10,column =1)

        BBQChicken= Checkbutton (f1, text="BBQ Chicken\t 220 BDT ",variable=var11,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkFriedRice()).grid(row=11,column=0,sticky='w')
        txtCBBQChicken= Entry(f1,font=('arial',13,'bold'), textvariable=varBBQChicken ,width=6,justify='right',state=DISABLED)
        txtCBBQChicken.grid(row=11,column =1)

        #----------------------Frame 2-------------------------------------------------


        #Variables for Starter
        varLemonade=StringVar()
        varBlueMint=StringVar()
        varColdCoffee=StringVar()
        varMilkshake=StringVar()


        #Variables value for Drinks
        varLemonade.set('0')
        varBlueMint.set('0')
        varColdCoffee.set('0')
        varMilkshake.set('0')


        lblMeal=Label(f2TOP, font=('arial', 18,'bold'), text="   Beverages   ")
        lblMeal.grid(row=0,column=0)

        Lemonade= Checkbutton (f2TOP, text="Lemonade\t 100 BDT",variable=var21,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkLemonade).grid(row=1,column=0,sticky='w')
        txtLemonade= Entry(f2TOP,font=('arial',13,'bold'), textvariable=varLemonade ,width=6,justify='right',state=DISABLED)
        txtLemonade.grid(row=1,column =1)

        BlueMint= Checkbutton (f2TOP, text="BlueMint\t\t 110 BDT",variable=var22,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkBlueMint).grid(row=2,column=0,sticky='w')
        txtBlueMint= Entry(f2TOP,font=('arial',13,'bold'), textvariable=varBlueMint ,width=6,justify='right',state=DISABLED)
        txtBlueMint.grid(row=2,column =1)

        ColdCoffee= Checkbutton (f2TOP, text="ColdCoffee\t 100 BDT",variable=var23,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkColdCoffee).grid(row=3,column=0,sticky='w')
        txtColdCoffee= Entry(f2TOP,font=('arial',13,'bold'), textvariable=varColdCoffee,width=6,justify='right',state=DISABLED)
        txtColdCoffee.grid(row=3,column =1)

        Milkshake= Checkbutton (f2TOP, text="MilkShake\t 100 BDT",variable=var24,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkMilkshake).grid(row=4,column=0,sticky='w')
        txtMilkshake= Entry(f2TOP,font=('arial',13,'bold'), textvariable=varMilkshake ,width=6,justify='right',state=DISABLED)
        txtMilkshake.grid(row=4,column =1)
        #--------------------
        def iExit():
            qExit=messagebox.askyesno("Quit System","Do you want yo quit?")
            if qExit > 0:
                root.destroy()
                return


        def Reset():
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)
            var16.set(0)
            var17.set(0)
            var18.set(0)
            var19.set(0)
            var20.set(0)
            var21.set(0)
            var22.set(0)
            var23.set(0)
            var24.set(0)
            var25.set(0)
            var26.set(0)
            var27.set(0)
            var28.set(0)
            var29.set(0)
            var30.set(0)
            var31.set(0)
            var32.set(0)
            var33.set(0)
            var34.set("")
            varFries.set('0')
            varMomo.set('0')
            varWings.set('0')
            varNachos.set('0')
            varOrings.set('0')
            varSubSandwich.set('0')
            varBBurger.set('0')
            varCBurger.set('0')
            varFriedrice.set('0')
            varBBQChicken.set('0')
            varLemonade.set('0')
            varBlueMint.set('0')
            varColdCoffee.set('0')
            varMilkshake.set('0')
            varChange.set('0')
            varVat.set('0')
            varSubTotal.set('0')
            varTotal.set('0')
            varBrowni.set('0')
            varCupcake.set('0')
            varVannilaPastry.set('0')
            varBlackForestPastry.set('0')
            varIcecreamV.set('0')
            varIcecreamC.set('0')
            varIcecreamM.set('0')
            varIcecreamS.set('0')
            txtFries.configure(state=DISABLED)
            txtMomo.configure(state=DISABLED)
            txtWings.configure(state=DISABLED)
            txtNachos.configure(state=DISABLED)
            txtORings.configure(state=DISABLED)
            txtSubdSanwich.configure(state=DISABLED)
            txtBBurger.configure(state=DISABLED)
            txtCBurger.configure(state=DISABLED)
            txtFriedRice.configure(state=DISABLED)
            txtCBBQChicken.configure(state=DISABLED)
            txtLemonade.configure(state=DISABLED)
            txtBlueMint.configure(state=DISABLED)
            txtColdCoffee.configure(state=DISABLED)
            txtMilkshake.configure(state=DISABLED)
            txtBrowni.configure(state=DISABLED)
            txtCupcake.configure(state=DISABLED)
            txtVanillaPastry.configure(state=DISABLED)
            txtBlackforestPastry.configure(state=DISABLED)
            txtIcecreamV.configure(state=DISABLED)
            txtIcecreamC.configure(state=DISABLED)
            txtIcecreamM.configure(state=DISABLED)
            txtIcecreamS.configure(state=DISABLED)

        #-------------------------Frame2 Bottom---------------------
        varChange=StringVar()
        varSubTotal=StringVar()
        varTotal=StringVar()
        varVat=StringVar()
        varPayment=IntVar()

        varChange.set('0')
        varSubTotal.set('0')
        varTotal.set('0')
        varVat.set('0')
        #varPayment.set('0')



        lblPaymentMethod=Label(f2BOTTOM, font=('arial', 14,'bold'), text="   Payment Method   ",bd=4,width=16, justify='right',anchor='w')
        lblPaymentMethod.grid(row=0,column=0)

        '''lblChange=Label(f2BOTTOM, font=('arial', 12,'bold'), text="   Change   ",bd=4, anchor='w')
        lblChange.grid(row=0,column=1)
        txtChange=Entry(f2BOTTOM, font=('arial', 18,'bold'), textvariable=varChange,width=6, justify='right',state=DISABLED)
        txtChange.grid(row=0,column=2)'''

        cmbPaymentMethod=ttk.Combobox(f2BOTTOM,textvariable=var34 ,state='readonly',font=('arial', 10,'bold'), width=20)
        cmbPaymentMethod['value']=('Cash','Master Card','Visa Card','bkash')
        cmbPaymentMethod.current(0)
        cmbPaymentMethod.grid(row=1,column=0)


        lblVAT=Label(f2BOTTOM, font=('arial', 12,'bold'), text="   VAT   ",bd=10, anchor='w')
        lblVAT.grid(row=1,column=1)
        txtVAT=Entry(f2BOTTOM,font=('arial',18,'bold'),textvariable=varVat,width=6,justify='right',state=DISABLED)
        txtVAT.grid(row = 1,column= 2)


        '''txtPayment=Entry(f2BOTTOM, font=('arial', 12,'bold'), textvariable=varPayment,width=6,justify='right',state=DISABLED)
        txtPayment.grid(row=2,column=0)'''

        lblSubtotal=Label(f2BOTTOM,font=('arial',12,'bold'),text='Sub Total',bd=10,width=8,anchor='w')
        lblSubtotal.grid(row=2,column=1)
        txtSubtotal=Entry(f2BOTTOM,font=('arial',18,'bold'),textvariable=varSubTotal,width=6,justify='right',state=DISABLED)
        txtSubtotal.grid(row=2,column=2)

        lblTotal=Label(f2BOTTOM,font=('arial',12,'bold'),text='Total',bd=10,width=8,anchor='w')
        lblTotal.grid(row=3,column=1)
        txtTotal=Entry(f2BOTTOM,font=('arial',18,'bold'),textvariable=varTotal,width=6,justify='right',state=DISABLED)
        txtTotal.grid(row=3,column=2)

        ButtonTotal=Button(f2BOTTOM,padx=16,pady=2,bd=10,fg='blue',font=('arial',12,'bold'),width=3,text='Total',command=costofmeal).grid(row=8,column=0)
        ButtonReset=Button(f2BOTTOM,padx=16,pady=2,bd=10,fg='blue',font=('arial',12,'bold'),width=3,text='Reset',command=Reset).grid(row=8,column=1)
        ButtonExit=Button(f2BOTTOM,padx=6,pady=2,bd=10,fg='blue',font=('arial',12,'bold'),width=3,text='Exit',command=lambda:iExit()).grid(row=8,column=2)
        lblspace=Label(f2BOTTOM,text='\n\n\n\n\n\n\n')
        lblspace.grid(row=8,column=4)


        #-----------------------Frame3------------------------------

        #Variables for Desserts

        varBrowni=StringVar()
        varCupcake=StringVar()
        varVannilaPastry=StringVar()
        varBlackForestPastry=StringVar()
        #------------
        varIcecreamV=StringVar()
        varIcecreamC=StringVar()
        varIcecreamM=StringVar()
        varIcecreamS=StringVar()




        varBrowni.set('0')
        varCupcake.set('0')
        varVannilaPastry.set('0')
        varBlackForestPastry.set('0')

        #-----------

        varIcecreamV.set('0')
        varIcecreamC.set('0')
        varIcecreamM.set('0')
        varIcecreamS.set('0')



        lblMeal=Label(f3, font=('arial', 18,'bold'), text="         Desserts ")
        lblMeal.grid(row=0,column=0)

        Browni= Checkbutton (f3, text="Chocolate Browni\t\t80 BDT ",variable=var25,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkBrowni).grid(row=1,column=0,sticky='w')
        txtBrowni= Entry(f3,font=('arial',13,'bold'), textvariable=varBrowni ,width=6,justify='right',state=DISABLED)
        txtBrowni.grid(row=1,column =1)


        Cupcake= Checkbutton (f3, text="Chocolate Cupcake\t 60 BDT",variable=var26,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkCupcake).grid(row=2,column=0,sticky='w')
        txtCupcake= Entry(f3,font=('arial',13,'bold'), textvariable=varCupcake ,width=6,justify='right',state=DISABLED)
        txtCupcake.grid(row=2,column =1)

        VannilaPastry= Checkbutton (f3, text="Vannila Pastry\t\t 50 BDT",variable=var27,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkVanillaPastry).grid(row=3,column=0,sticky='w')
        txtVanillaPastry= Entry(f3,font=('arial',13,'bold'), textvariable=varVannilaPastry ,width=6,justify='right',state=DISABLED)
        txtVanillaPastry.grid(row=3,column =1)

        #BlackForestPastry= Checkbutton (f3, text="Black Forest Pastry\t 60 BDT",variable=var28,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkBlackforestPastry).grid(row=4,column=0,sticky='w')
        #txtBlackforestPastry= Entry(f3,font=('arial',13,'bold'), textvariable=varBlackForestPastry ,width=6,justify='right',state=DISABLED)
        #txtBlackforestPastry.grid(row=4,column =1)

        #----------------------Ice Cream---------------
        lblMeal=Label(f3, font=('arial', 18,'bold'), text="  Cold Ice Cream " )
        lblMeal.grid(row=5,column=0)

        IcecreamV= Checkbutton (f3, text="Vanila IceCream\t\t 100 BDT",variable=var30,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkIcecreamV).grid(row=6,column=0,sticky='w')
        txtIcecreamV= Entry(f3,font=('arial',13,'bold'), textvariable=varIcecreamV ,width=6,justify='right',state=DISABLED)
        txtIcecreamV.grid(row=6,column =1)

        IcecreamC= Checkbutton (f3, text="Chocolate IceCream\t 100 BDT",variable=var31,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkIcecreamC).grid(row=7,column=0,sticky='w')
        txtIcecreamC= Entry(f3,font=('arial',13,'bold'), textvariable=varIcecreamC ,width=6,justify='right',state=DISABLED)
        txtIcecreamC.grid(row=7,column =1)

        #IcecreamM= Checkbutton (f3, text="Mango IceCream\t\t 100 BDT",variable=var32,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkIcecreamM).grid(row=8,column=0,sticky='w')
        #txtIcecreamM= Entry(f3,font=('arial',13,'bold'), textvariable=varIcecreamM ,width=6,justify='right',state=DISABLED)
        #txtIcecreamM.grid(row=8,column =1)

        #IcecreamS= Checkbutton (f3, text="Strawberry IceCream\t 100 BDT",variable=var33,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkIcecreamS).grid(row=9,column=0,sticky='w')
        #txtIcecreamS= Entry(f3,font=('arial',13,'bold'), textvariable=varIcecreamS ,width=6,justify='right',state=DISABLED)
        #txtIcecreamS.grid(row=9,column =1)


root = Tk()
root.geometry("1350x750+0+0")
Order = Restaurant(root)

root.mainloop()
