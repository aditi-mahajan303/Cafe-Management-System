from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
from PIL import Image,ImageTk
import mysql.connector
import numpy as np
#main window
root = Tk()
root.geometry("1600x1600")
root.title('Cafe management system')
#root.configure(bg='cadet blue')

load=Image.open("food-lunch.jpg")
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)

#database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password123",
    database="hotel",
)
my_cursor = mydb.cursor()
#Create Database
#my_cursor.execute("CREATE DATABASE hotel")
#Check if database is created
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
 #   print(db)

#my_cursor.execute("CREATE TABLE customer (customer_id INT AUTO_INCREMENT PRIMARY KEY,cfirst_name VARCHAR(255),clast_name VARCHAR(255),c_gender VARCHAR(50),c_age VARCHAR(50),c_email VARCHAR(255),c_mobile_no VARCHAR(20),c_address VARCHAR(150))")
#my_cursor.execute("CREATE TABLE reciept(item_id INT AUTO_INCREMENT PRIMARY KEY,item VARCHAR(255),qty VARCHAR(50),rate VARCHAR(255))")
#my_cursor.execute("DROP TABLE reciept")
#show staff table
#my_cursor.execute("SELECT * FROM reciept")
#print(my_cursor.description)
#for thing in my_cursor.description:
    #print(thing)

# FRAME LOGIN
frame1 = Frame(root, height=250, width=250, highlightbackground='black', highlightthickness=3)
frame1.grid(row=0, column=0, padx=500, pady=200, ipadx=80, ipady=80)
# FRAME LABEL
large_font = ('Comic Sans MS', 30, 'bold')
Labelhead = Label(root, height=1, width=20, font=large_font, text="Cafe management system",
                  fg='black')
Labelhead.place(relx=0.33, rely=0.1)
global top

def newwindow():
    if usernamee.get() == "abc" and passworde.get() == "xyz":
        top = Toplevel()
        root.withdraw()

        large_font1 = ('Comic Sans MS', 20, 'bold')
        Labelhead1 = Label(top, height=1, width=90, font=large_font1,
                           text="Cafe management system", fg='black')
        Labelhead1.place(relx=0, rely=0)
        frame2 = Frame(top, height=570, width=900, highlightbackground='black', highlightthickness=1)
        frame2.grid(row=0, column=0, padx=250, pady=45, ipadx=80, ipady=80)
        large_font2 = ('Comic Sans MS', 15, 'bold')
        Labelhead2 = Label(frame2, height=1, width=88, font=large_font2,
                           text="MENU", fg='black')
        Labelhead2.place(relx=0, rely=0)
        large_font3 = ('Comic Sans MS', 13)
        large_font4 = ('Comic Sans MS', 11)
        l = Label(frame2, text="PIZZA", font=large_font3)
        l.place(relx=0, rely=0.05)
        #FOR CHECKBOX
        global var1
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = IntVar()
        var15 = IntVar()
        var16 = IntVar()
        var17 = IntVar()
        var18 = IntVar()
        var19 = IntVar()
        var20 = IntVar()
        var21 = IntVar()
        var22 = IntVar()
        var23 = IntVar()
        var24 = IntVar()
        var25 = IntVar()
        var26 = IntVar()
        var27 = IntVar()
        var28 = IntVar()
#FUNCTION TO CHECK IF ITEM IN MENU IS CHECKED
        def check1():
            if var1.get() == 1:
                e1.config(state='normal')
            elif var1.get() == 0:
                e1.config(state='disabled')
            if var1.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("1","Cheese Corn Pizza", "0", "250 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()
            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check2():
            if var2.get() == 1:
                e2.config(state='normal')
            elif var2.get() == 0:
                e2.config(state='disabled')

            if var2.get() == 1:
                sql_command2 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values2 = ("2","Country Side Pizza", "0", "260 Rs")
                my_cursor.execute(sql_command2, values2)
                # commit changes to database
                mydb.commit()
            my_cursor.execute("SELECT * FROM reciept")
            result2 = my_cursor.fetchall()
            for x in result2:
                print(x)
        def check3():
            if var3.get() == 1:
                e3.config(state='normal')
            elif var3.get() == 0:
                e3.config(state='disabled')
            if var3.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("3","Veg Supreme Pizza", "0", "260 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()
            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check4():
            if var4.get() == 1:
                e4.config(state='normal')
            elif var4.get() == 0:
                e4.config(state='disabled')
            if var4.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("4","Vegiteriana Pizza", "0", "250 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()
            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check5():
            if var5.get() == 1:
                e5.config(state='normal')
            elif var5.get() == 0:
                e5.config(state='disabled')

            if var5.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("5","Margherita Pizza", "0", "260 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check6():
            if var6.get() == 1:
                e6.config(state='normal')
            elif var6.get() == 0:
                e6.config(state='disabled')

            if var6.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("6","Al Arrabbiata Pasta", "0", "240 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)

        def check7():
            if var7.get() == 1:
                e7.config(state='normal')
            elif var7.get() == 0:
                e7.config(state='disabled')

            if var7.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("7","Makhani Pasta", "0", "230 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)

        def check8():
            if var8.get() == 1:
                e8.config(state='normal')
            elif var8.get() == 0:
                e8.config(state='disabled')

            if var8.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("8","Mexican Veggies Pasta", "0", "250 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)

        def check9():
            if var9.get() == 1:
                e9.config(state='normal')
            elif var9.get() == 0:
                e9.config(state='disabled')

            if var9.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("9","Veg Burger", "0", "180 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)

        def check10():
            if var10.get() == 1:
                e10.config(state='normal')
            elif var10.get() == 0:
                e10.config(state='disabled')

            if var10.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("10","Cottage Cheese Burger", "0", "180 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)

        def check11():
            if var11.get() == 1:
                e11.config(state='normal')
            elif var11.get() == 0:
                e11.config(state='disabled')

            if var11.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("11","Paneer Tikka Burger", "0", "150 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)

        def check12():
            if var12.get() == 1:
                e12.config(state='normal')
            elif var12.get() == 0:
                e12.config(state='disabled')

            if var12.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("12","Veg Cheese Grilled Sandwich", "0", "160 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)

        def check13():
            if var13.get() == 1:
                e13.config(state='normal')
            elif var13.get() == 0:
                e13.config(state='disabled')

            if var13.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("13","Veg Club Sandwich", "0", "140 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)

        def check14():
            if var14.get() == 1:
                e14.config(state='normal')
            elif var14.get() == 0:
                e14.config(state='disabled')

            if var14.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("14","Paneer Stuffed Sandwich", "0", "150 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check15():
            if var15.get() == 1:
                e15.config(state='normal')
            elif var15.get() == 0:
                e15.config(state='disabled')

            if var15.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("15","French Fries", "0", "120 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check16():
            if var16.get() == 1:
                e16.config(state='normal')
            elif var16.get() == 0:
                e16.config(state='disabled')

            if var16.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("16","Mexican Cheese Fries", "0", "140 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check17():
            if var17.get() == 1:
                e17.config(state='normal')
            elif var17.get() == 0:
                e17.config(state='disabled')

            if var17.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("17","Assorted Garlic Bread", "0", "160 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)

        def check18():
            if var18.get() == 1:
                e18.config(state='normal')
            elif var18.get() == 0:
                e18.config(state='disabled')

            if var18.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("18","Stuffed Garlic Bread", "0", "180 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check19():
            if var19.get() == 1:
                e19.config(state='normal')
            elif var19.get() == 0:
                e19.config(state='disabled')

            if var19.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("19","Chocolate Brownie", "0", "120 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check20():
            if var20.get() == 1:
                e20.config(state='normal')
            elif var20.get() == 0:
                e20.config(state='disabled')

            if var20.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("20","Donuts", "0", "100 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check21():
            if var21.get() == 1:
                e21.config(state='normal')
            elif var21.get() == 0:
                e21.config(state='disabled')

            if var21.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("21","Pastries", "0", "60 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check22():
            if var22.get() == 1:
                e22.config(state='normal')
            elif var22.get() == 0:
                e22.config(state='disabled')

            if var22.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("22","Icecream Scoops", "0", "60 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check23():
            if var23.get() == 1:
                e23.config(state='normal')
            elif var23.get() == 0:
                e23.config(state='disabled')

            if var23.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("23","Tea", "0", "40 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check24():
            if var24.get() == 1:
                e24.config(state='normal')
            elif var24.get() == 0:
                e24.config(state='disabled')

            if var24.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("24","Coffee", "0", "70 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check25():
            if var25.get() == 1:
                e25.config(state='normal')
            elif var25.get() == 0:
                e25.config(state='disabled')

            if var25.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("25","Cold Coffee", "0", "100 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check26():
            if var26.get() == 1:
                e26.config(state='normal')
            elif var26.get() == 0:
                e26.config(state='disabled')

            if var26.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("26","Chocolate Milkshake", "0", "120 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check27():
            if var27.get() == 1:
                e27.config(state='normal')
            elif var27.get() == 0:
                e27.config(state='disabled')

            if var27.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("27","Oreo Milkshake", "0", "140 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
        def check28():
            if var28.get() == 1:
                e28.config(state='normal')
            elif var28.get() == 0:
                e28.config(state='disabled')

            if var28.get() == 1:
                sql_command1 = "INSERT INTO reciept (item_id,item,qty,rate) VALUES (%s,%s,%s,%s)"
                values1 = ("28","Soft Drinks", "0", "30 Rs")
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()

            my_cursor.execute("SELECT * FROM reciept")
            result1 = my_cursor.fetchall()
            for x in result1:
                print(x)
#CHECKBUTTON AND SPINBOX IN MENU
        c1 = Checkbutton(frame2, text="Cheese Corn Pizza", variable=var1, font=large_font4, command=check1)
        c1.place(relx=0, rely=0.09)
        e1 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e1.place(relx=0.28, rely=0.095)

        c2 = Checkbutton(frame2, text="Country Side Pizza", variable=var2, font=large_font4, command=check2)
        c2.place(relx=0, rely=0.14)
        e2 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e2.place(relx=0.28, rely=0.145)

        c3 = Checkbutton(frame2, text="Veg Supreme Pizza", variable=var3, font=large_font4, command=check3)
        c3.place(relx=0, rely=0.19)
        e3 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e3.place(relx=0.28, rely=0.196)

        c4 = Checkbutton(frame2, text="Vegiteriana Pizza", variable=var4, font=large_font4, command=check4)
        c4.place(relx=0, rely=0.242)
        e4 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e4.place(relx=0.28, rely=0.25)

        c5 = Checkbutton(frame2, text="Margherita Pizza", variable=var5, font=large_font4, command=check5)
        c5.place(relx=0, rely=0.295)
        e5 = Spinbox(frame2, from_=0, to=10,width=10, state='disabled')
        e5.place(relx=0.28, rely=0.305)

        l1 = Label(frame2, text="PASTA", font=large_font3)
        l1.place(relx=0, rely=0.37)

        c6 = Checkbutton(frame2, text="Al Arrabbiata Pasta", variable=var6, font=large_font4, command=check6)
        c6.place(relx=0, rely=0.41)
        e6 = Spinbox(frame2,from_=0, to=10,width=10, state='disabled')
        e6.place(relx=0.28, rely=0.42)

        c7 = Checkbutton(frame2, text="Makhani Pasta", variable=var7, font=large_font4, command=check7)
        c7.place(relx=0, rely=0.46)
        e7 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e7.place(relx=0.28, rely=0.47)

        c8 = Checkbutton(frame2, text="Mexican Veggies Pasta", variable=var8, font=large_font4, command=check8)
        c8.place(relx=0, rely=0.51)
        e8 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e8.place(relx=0.28, rely=0.52)

        l2 = Label(frame2, text="BURGERS", font=large_font3)
        l2.place(relx=0, rely=0.58)

        c9 = Checkbutton(frame2, text="Veg Burger", variable=var9, font=large_font4, command=check9)
        c9.place(relx=0, rely=0.62)
        e9 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e9.place(relx=0.28, rely=0.63)

        c10 = Checkbutton(frame2, text="Cottage Cheese Burger", variable=var10, font=large_font4, command=check10)
        c10.place(relx=0, rely=0.67)
        e10 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e10.place(relx=0.28, rely=0.68)

        c11 = Checkbutton(frame2, text="Paneer Tikka Burger", variable=var11, font=large_font4, command=check11)
        c11.place(relx=0, rely=0.72)
        e11 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e11.place(relx=0.28, rely=0.73)

        l3 = Label(frame2, text="SANDWICHES", font=large_font3)
        l3.place(relx=0, rely=0.79)
        global e14
        c12 = Checkbutton(frame2, text="Veg Grilled Cheese Sandwich", variable=var12, font=large_font4, command=check12)
        c12.place(relx=0, rely=0.83)
        e12 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e12.place(relx=0.28, rely=0.84)

        c13 = Checkbutton(frame2, text="Veg Club Sandwich", variable=var13, font=large_font4, command=check13)
        c13.place(relx=0, rely=0.88)
        e13 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e13.place(relx=0.28, rely=0.89)

        c14 = Checkbutton(frame2, text="Paneer Stuffed Sandwich", variable=var14, font=large_font4, command=check14)
        c14.place(relx=0, rely=0.93)
        e14 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e14.place(relx=0.28, rely=0.94)

        l4 = Label(frame2, text="FRIES", font=large_font3)
        l4.place(relx=0.53, rely=0.05)
        global c15
        global e15

        c15 = Checkbutton(frame2, text="French Fries", variable=var15, font=large_font4, command=check15)
        c15.place(relx=0.53, rely=0.09)
        e15 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e15.place(relx=0.81, rely=0.095)

        c16 = Checkbutton(frame2, text="Mexican Cheese Fries", variable=var16, font=large_font4, command=check16)
        c16.place(relx=0.53, rely=0.14)
        e16 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e16.place(relx=0.81, rely=0.145)

        l5 = Label(frame2, text="GARLIC BREADS", font=large_font3)
        l5.place(relx=0.53, rely=0.21)
        global e17
        c17 = Checkbutton(frame2, text="Assorted Garlic Bread ", variable=var17, font=large_font4, command=check17)
        c17.place(relx=0.53, rely=0.25)
        e17 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e17.place(relx=0.81, rely=0.26)

        c18 = Checkbutton(frame2, text="Stuffed Garlic Bread", variable=var18, font=large_font4, command=check18)
        c18.place(relx=0.53, rely=0.30)
        global e18
        e18 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e18.place(relx=0.81, rely=0.31)

        l6 = Label(frame2, text="DESSERTS", font=large_font3)
        l6.place(relx=0.53, rely=0.37)
        global e24

        c19 = Checkbutton(frame2, text="Chocolate Brownie", variable=var19, font=large_font4, command=check19)
        c19.place(relx=0.53, rely=0.41)
        e19 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e19.place(relx=0.81, rely=0.42)

        c20 = Checkbutton(frame2, text="Donuts", variable=var20, font=large_font4, command=check20)
        c20.place(relx=0.53, rely=0.46)
        e20 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e20.place(relx=0.81, rely=0.47)

        c21 = Checkbutton(frame2, text="Pastries", variable=var21, font=large_font4, command=check21)
        c21.place(relx=0.53, rely=0.51)
        e21 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e21.place(relx=0.81, rely=0.52)

        c22 = Checkbutton(frame2, text="Icecream Scoops", variable=var22, font=large_font4, command=check22)
        c22.place(relx=0.53, rely=0.56)
        e22 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e22.place(relx=0.81, rely=0.57)

        l7 = Label(frame2, text="CAKES", font=large_font3)
        l7.place(relx=0.53, rely=0.63)

        c23 = Checkbutton(frame2, text="Black forest", variable=var23, font=large_font4, command=check23)
        c23.place(relx=0.53, rely=0.67)
        e23 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e23.place(relx=0.81, rely=0.68)

        c24 = Checkbutton(frame2, text="Black current", variable=var24, font=large_font4, command=check24)
        c24.place(relx=0.53, rely=0.72)
        e24 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e24.place(relx=0.81, rely=0.73)
        p1 = StringVar()
        c25 = Checkbutton(frame2, text="Buttersotch", variable=var25, font=large_font4, command=check25)
        c25.place(relx=0.53, rely=0.77)
        e25 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled',textvariable=p1)
        e25.place(relx=0.81, rely=0.78)

        c26 = Checkbutton(frame2, text="Chocolate ", variable=var26, font=large_font4, command=check26)
        c26.place(relx=0.53, rely=0.82)
        global e26
        e26 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e26.place(relx=0.81, rely=0.83)

        c27 = Checkbutton(frame2, text="Oreo Cake", variable=var27, font=large_font4, command=check27)
        c27.place(relx=0.53, rely=0.87)
        e27 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled')
        e27.place(relx=0.81, rely=0.88)

        c28 = Checkbutton(frame2, text="White forest", variable=var28, font=large_font4, command=check28)
        c28.place(relx=0.53, rely=0.92)
        global e28
        d1=StringVar()
        e28 = Spinbox(frame2, from_=0, to=10, width=10, state='disabled',textvariable=d1)
        e28.place(relx=0.81, rely=0.93)

        def a():
            if var1.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e1.get(),1))
                mydb.commit()

            if var2.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()
                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e2.get(),2))
                mydb.commit()

            if var3.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e3.get(),3))
                mydb.commit()

            if var4.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()

                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e4.get(),4))
                mydb.commit()

            if var5.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()

                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e5.get(),5))
                mydb.commit()

            if var6.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()

                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e6.get(),6))
                mydb.commit()

            if var7.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()

                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e7.get(),7))
                mydb.commit()

            if var8.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()

                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e8.get(),8))
                mydb.commit()

            if var9.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()

                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e9.get(),9))
                mydb.commit()

            if var10.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e10.get(),10))
                mydb.commit()

            if var11.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e11.get(),11))
                mydb.commit()

            if var12.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e12.get(),12))
                mydb.commit()

            if var13.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e13.get(),13))
                mydb.commit()

            if var14.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e14.get(),14))
                mydb.commit()

            if var15.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e15.get(),15))
                mydb.commit()

            if var16.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e16.get(),16))
                mydb.commit()

            if var17.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e17.get(),17))
                mydb.commit()

            if var18.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e18.get(),18))
                mydb.commit()

            if var19.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e19.get(),19))
                mydb.commit()

            if var20.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e20.get(),20))
                mydb.commit()

            if var21.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e21.get(),21))
                mydb.commit()

            if var22.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e22.get(),22))
                mydb.commit()

            if var23.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e23.get(),23))
                mydb.commit()

            if var24.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e24.get(),24))
                mydb.commit()

            if var25.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e25.get(),25))
                mydb.commit()

            if var26.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e26.get(),26))
                mydb.commit()

            if var27.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()


                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e27.get(),27))
                mydb.commit()

            if var28.get()==1:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()

                my_cursor.execute("""
                UPDATE reciept
                SET qty=%s
                WHERE item_id=%s
                """, (e28.get(),28))
                mydb.commit()

        def clear_previous():

         my_cursor.execute("DROP TABLE reciept")
         my_cursor.execute("CREATE TABLE reciept(item_id INT AUTO_INCREMENT PRIMARY KEY,item VARCHAR(255),qty VARCHAR(50),rate VARCHAR(255))")




        b=Button(top,text="Update",width=8, padx=4, pady=4,command=a,bg="LightYellow2",font=('Times', 15, 'bold'))
        b.place(relx=0.0,rely=0.3)
        backmain=Button(top,text="Back",width=8, padx=4, pady=4,font=('Times', 15, 'bold'))
        backmain.place(relx=0.0,rely=0.4)
        r = Button(top, text="X", width=8, padx=4, pady=4, command=clear_previous,
                   font=('Times', 15, 'bold'))
        r.place(relx=0.0, rely=0.5)

        def newwindow2():
            top2 = Toplevel()
            top.withdraw()
            top2.geometry("1600x1600")


            mainframe=Frame(top2,bd=10,width=1600,height=1600,relief=RIDGE)

            mainframe.place(relx=0.1,rely=0.03)

            titleframe = Frame(mainframe, bd=7, width=770, height=100, relief=RIDGE)
            titleframe.grid(row=0,column=0)
            topframe3 = Frame(mainframe, bd=5, width=770, height=500, relief=RIDGE)
            topframe3.grid(row=1,column=0)

            leftframe = Frame(topframe3, bd=5, width=770, height=400, padx=2,relief=RIDGE)
            leftframe.pack(side=LEFT)
            leftframe1 = Frame(leftframe, bd=5, width=600, height=180, padx=2,pady=4, relief=RIDGE)
            leftframe1.pack(side=TOP,padx=0,pady=0)

            rightframe1 = Frame(topframe3, bd=5, width=100, height=400, padx=2, relief=RIDGE)
            rightframe1.pack(side=RIGHT)
            rightframe1a = Frame(rightframe1, bd=5, width=90, height=300, padx=1,pady=1, relief=RIDGE)
            rightframe1a.pack(side=TOP)

            StaffId=StringVar()
            FirstName = StringVar()
            LastName = StringVar()
            Gender = StringVar()
            Age = StringVar()
            Post = StringVar()
            Salary = StringVar()
            Email = StringVar()
            MobileNo = StringVar()
            Address = StringVar()

            def iexit():
                iexit=messagebox.askyesno("Staff Database","Confirm if you want to exit")
                if iexit>0:
                    top2.destroy()
                    return

            def reset():
                efname.delete(0,END)
                elname.delete(0, END)
                Gender.set("")
                eage.delete(0, END)
                Post.set("")
                esalary.delete(0, END)
                eemail.delete(0, END)
                emobileno.delete(0, END)
                eaddress.delete(0, END)
                estaffid.delete(0, END)

            def adddata():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()
                sql_command = "INSERT INTO staff (staff_id,first_name,last_name,gender,age,post,salary,email,mobile_no,address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (
                estaffid.get(), efname.get(), elname.get(), egender.get(), eage.get(), epost.get(), esalary.get(), eemail.get(),emobileno.get(),eaddress.get())
                my_cursor.execute(sql_command, values)
                # commit changes to database
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Data Entry Form","Record Entered Successfully")

            def displaydata():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()
                my_cursor.execute("SELECT * FROM staff")
                result = my_cursor.fetchall()
                if len(result) !=0:
                    for row in result:
                        staff_record.insert('',END,values=row)
                    mydb.commit()


            def staffinfo(ev):
                viewinfo=staff_record.focus()
                staffdata=staff_record.item(viewinfo)
                row=staffdata['values']
                StaffId.set(row[0])
                FirstName.set(row[1])
                LastName.set(row[2])
                Gender.set(row[3])
                Age.set(row[4])
                Post.set(row[5])
                Salary.set(row[6])
                Email.set(row[7])
                MobileNo.set(row[8])
                Address.set(row[9])
            def updatedata():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()
                my_cursor.execute("""
                UPDATE staff 
                SET first_name=%s,last_name=%s,gender=%s,age=%s,post=%s,salary=%s,email=%s,mobile_no=%s,address=%s 
                WHERE staff_id=%s
                """,(FirstName.get(), LastName.get(), Gender.get(),Age.get(),Post.get(),Salary.get(),Email.get(),MobileNo.get(),Address.get(),StaffId.get()))
                mydb.commit()

                mydb.close()
                messagebox.showinfo("Data Entry Form", "Record Updated Successfully")

            def deletedata(staff_record):
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )


                my_cursor = mydb.cursor()
                selected_item=staff_record.selection()[0]
                #print(staff_record.item(selected_item)['values'])
                uid=staff_record.item(selected_item)['values'][0]
                del_query="DELETE FROM staff WHERE staff_id=%s"
                sel_data=(uid,)
                my_cursor.execute(del_query,sel_data)
                mydb.commit()
                mydb.close()
                staff_record.delete(selected_item)
                reset()
                messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")

            def search():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()

                try:
                    sql="SELECT * FROM staff where staff_id='%s'"%estaffid.get()
                    my_cursor.execute(sql)
                    result=my_cursor.fetchone()
                    FirstName.set(result[1])
                    LastName.set(result[2])
                    Gender.set(result[3])
                    Age.set(result[4])
                    Post.set(result[5])
                    Salary.set(result[6])
                    Email.set(result[7])
                    MobileNo.set(result[8])
                    Address.set(result[9])

                    mydb.commit()

                    mydb.close()

                except:
                    messagebox.showinfo("Data Entry Form", "No Such Record Found")
                    reset()




            def sback():
                top2.withdraw()
                newwindow()

            lbtitle=Label(titleframe,font=('arial',40,'bold'),text="Staff Database ",bd=7)
            lbtitle.grid(row=0,column=0,padx=132)

            lbstaffid = Label(leftframe1, font=('arial', 12, 'bold'), text="Staff Id", bd=7)
            lbstaffid.grid(row=1, column=0, sticky=W, padx=5)
            estaffid = Entry(leftframe1, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',textvariable=StaffId)
            estaffid.grid(row=1, column=1, sticky=W, padx=5)

            lbfname = Label(leftframe1, font=('arial', 12, 'bold'), text="First Name", bd=7)
            lbfname.grid(row=2, column=0, sticky=W,padx=5)
            efname = Entry(leftframe1, font=('arial', 12, 'bold'), bd=7,width=44,justify='left',textvariable=FirstName)
            efname.grid(row=2, column=1, sticky=W, padx=5)

            lblname = Label(leftframe1, font=('arial', 12, 'bold'), text="Last Name", bd=7)
            lblname.grid(row=3, column=0, sticky=W, padx=5)
            elname = Entry(leftframe1, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',textvariable=LastName)
            elname.grid(row=3, column=1, sticky=W, padx=5)

            lbgender = Label(leftframe1, font=('arial', 12, 'bold'), text="Gender", bd=7)
            lbgender.grid(row=4, column=0, sticky=W, padx=5)
            egender =Combobox(leftframe1, font=('arial', 12, 'bold'), width=43, state='readonly',textvariable=Gender)
            egender['values']=('','Female','Male')
            egender.current(0)
            egender.grid(row=4, column=1)

            lbage = Label(leftframe1, font=('arial', 12, 'bold'), text="Age", bd=7)
            lbage.grid(row=5, column=0, sticky=W, padx=5)
            eage = Entry(leftframe1, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',textvariable=Age)
            eage.grid(row=5, column=1, sticky=W, padx=5)

            lbpost = Label(leftframe1, font=('arial', 12, 'bold'), text="Post", bd=7)
            lbpost.grid(row=6, column=0, sticky=W, padx=5)
            epost = Combobox(leftframe1, font=('arial', 12, 'bold'), width=43, state='readonly',textvariable=Post)
            epost['values'] = ('', 'Manager', 'Receptionist','Chef','Helping Staff')
            epost.current(0)
            epost.grid(row=6, column=1)

            lbsalary = Label(leftframe1, font=('arial', 12, 'bold'), text="Salary", bd=7)
            lbsalary.grid(row=7, column=0, sticky=W, padx=5)
            esalary = Entry(leftframe1, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',textvariable=Salary)
            esalary.grid(row=7, column=1, sticky=W, padx=5)

            lbemail = Label(leftframe1, font=('arial', 12, 'bold'), text="Email", bd=7)
            lbemail.grid(row=8, column=0, sticky=W, padx=5)
            eemail = Entry(leftframe1, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',textvariable=Email)
            eemail.grid(row=8, column=1, sticky=W, padx=5)

            lbmobileno = Label(leftframe1, font=('arial', 12, 'bold'), text="Mobile No", bd=7)
            lbmobileno.grid(row=9, column=0, sticky=W, padx=5)
            emobileno = Entry(leftframe1, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',textvariable=MobileNo)
            emobileno.grid(row=9, column=1, sticky=W, padx=5)

            lbaddress = Label(leftframe1, font=('arial', 12, 'bold'), text="Address", bd=7)
            lbaddress.grid(row=10, column=0, sticky=W, padx=5)
            eaddress = Entry(leftframe1, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',textvariable=Address)
            eaddress.grid(row=10, column=1, sticky=W, padx=5)

            scroll_y=Scrollbar(leftframe,orient=VERTICAL)
            staff_record=Treeview(leftframe,height=12,columns=("staff_id","firstname","lastname","gender","age","post","salary","email","mobile_no","address"),yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT,fill=Y)

            staff_record.heading("staff_id", text="Staff ID")
            staff_record.heading("firstname", text="First Name")
            staff_record.heading("lastname", text="Last Name")
            staff_record.heading("gender", text="Gender")
            staff_record.heading("age", text="Age")
            staff_record.heading("post", text="Post")
            staff_record.heading("salary", text="Salary")
            staff_record.heading("email", text="Email")
            staff_record.heading("mobile_no", text="Mobile No")
            staff_record.heading("address", text="Address")

            staff_record['show']='headings'

            staff_record.column("staff_id", width=60)
            staff_record.column("firstname", width=100)
            staff_record.column("lastname", width=100)
            staff_record.column("gender", width=70)
            staff_record.column("age", width=40)
            staff_record.column("post", width=100)
            staff_record.column("salary", width=70)
            staff_record.column("email", width=150)
            staff_record.column("mobile_no", width=90)
            staff_record.column("address", width=150)


            staff_record.pack(fill = BOTH,expand=1)
            staff_record.bind("<ButtonRelease-1>",staffinfo)
            #displaydata()

            btnaddnew=Button(rightframe1a,font=('arial',16,'bold'),text="Add New",bd=4,pady=1,padx=24,width=8,height=2,command=adddata)
            btnaddnew.grid(row=0,column=0,padx=1)
            btndisplay = Button(rightframe1a, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24, width=8,height=2,command=displaydata)
            btndisplay.grid(row=1, column=0, padx=1)
            btnupdate = Button(rightframe1a, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24, width=8, height=2,command=updatedata)
            btnupdate.grid(row=2, column=0, padx=1)
            btndelete = Button(rightframe1a, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24, width=8,height=2,command=lambda:deletedata(staff_record))
            btndelete.grid(row=3, column=0, padx=1)
            btnsearch = Button(rightframe1a, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24, width=8,height=2,command=search)
            btnsearch.grid(row=4, column=0, padx=1)
            btnreset = Button(rightframe1a, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24, width=8,height=2,command=reset)
            btnreset.grid(row=5, column=0, padx=1)
            btnexit = Button(rightframe1a, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24, width=8,height=2,command=iexit)
            btnexit.grid(row=6, column=0, padx=1)
            btnback = Button(rightframe1a, font=('arial', 16, 'bold'), text="Back", bd=4, pady=1, padx=24, width=8,
                             height=2, command=sback)
            btnback.grid(row=7, column=0, padx=1)


        staffb=Button(top,text="Staff",width=8, padx=4, pady=4, command=newwindow2, font=("Times", 15, 'bold'),bg="LightYellow2")
        staffb.place(relx=0.0,rely=0.1)
        def sback2():
            newwindow()
        def newwindow1():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="password123",
                database="hotel",
            )
            my_cursor = mydb.cursor()

            top1 = Toplevel()
            top.withdraw()

            top1.config(bg='NavajoWhite3')
            top1.title("Customer details")
            top1.geometry('1600x1600')

            bbutton=Button(top1,width=8,text="BACK", font=("Times", 15, 'bold'),command=sback2)
            bbutton.place(relx=0.0,rely=0.8)

            large_font6 = ('Comic Sans MS', 10, 'bold')
            framerecipt = Frame(top1, height=600, width=609)
            framerecipt.place(relx=0.3, rely=0.15)
            labeltitle = Label(top1, height=2, width=30, text="Cafe management", font=large_font6)
            labeltitle.place(relx=0.42, rely=0.2)
            labeltitle1 = Label(top1, height=1, width=65, text=" 5 \38,Old Mahabalipuram Road,"
                                                               "Oggiyampet Chennai ", font=large_font6)
            labeltitle1.place(relx=0.32, rely=0.24)
            labeltitle2 = Label(top1, height=1, width=30, text="Mobile:9884131916",
                                font=large_font6)
            labeltitle2.place(relx=0.4, rely=0.28)
            my_canvas = Canvas(top1, width=450, height=450, bg="white")
            my_canvas.place(relx=0.35, rely=0.32)
            my_canvas.create_line(0, 50, 450, 50, fill="black")
            labelitem = Label(my_canvas, text="ITEM", bg="white")
            labelitem.place(relx=0.1, rely=0.05)
            labelprice1 = Label(my_canvas, height=1, width=5, bg="white")
            labelprice1.place(relx=0.08, rely=0.12)
            labelprice2 = Label(my_canvas, height=1, width=5, bg="white")
            labelprice2.place(relx=0.08, rely=0.12)
            labelitem = Label(my_canvas, text="QTY", bg="white")
            labelitem.place(relx=0.5, rely=0.05)
            myframe = Frame(my_canvas, height=250, width=30, bg="yellow")
            myframe.place(relx=0.5, rely=0.12)
            labelprice = Label(my_canvas, text="RATE", bg="white")
            labelprice.place(relx=0.8, rely=0.05)
            myframe1 = Frame(my_canvas, height=250, width=50, bg="white")
            myframe1.place(relx=0.8, rely=0.12)

            labeldash = Label(my_canvas,
                              text="----------------------------------------------------------------------------------------------",
                              bg="white")
            labeldash.place(relx=0.00, rely=0.9)

            my_cursor.execute("SELECT SUM(rate) FROM reciept")
            result = my_cursor.fetchall()

            labelsubtotal = Label(my_canvas, text="TOTAL", bg="white")
            labelsubtotal.place(relx=0.05, rely=0.7)
            labelsubtotalV = Label(my_canvas, text=result, bg="light grey", width='7')
            labelsubtotalV.place(relx=0.8, rely=0.7)



#calculation of receipt
            result1=np.asarray(result)*0.18

            labeltotal = Label(my_canvas, text="TAX", bg="white")
            labeltotal.place(relx=0.055, rely=0.75)
            labeltotalV = Label(my_canvas, text=result1, bg="light grey", width='7')
            labeltotalV.place(relx=0.8, rely=0.76)
            my_canvas.create_line(0, 310, 450, 310, fill="black")

            result2=result1+result

            labelpaid = Label(my_canvas, text="SUBTOTAL", bg="white")
            labelpaid.place(relx=0.05, rely=0.8)
            labelpaidV = Label(my_canvas, text=result2, bg="light grey", width='7')
            labelpaidV.place(relx=0.8, rely=0.82)

            labelthank = Label(my_canvas, height="1", width="20", text="THANK YOU !VISIT AGAIN",
                               bg="light grey")
            labelthank.place(relx=0.38, rely=0.95)



            my_cursor.execute("SELECT item FROM reciept")
            result = my_cursor.fetchall()
            for index,x in enumerate(result):
                num=0
                for y in x:
                    lookup_label=Label(labelprice2,text=y)
                    lookup_label.grid(row=index,column=num)
                    num+=1

            my_cursor.execute("SELECT qty FROM reciept")
            result = my_cursor.fetchall()
            for index, x in enumerate(result):
                num = 0
                for y in x:
                    lookup_label = Label(myframe, text=y)
                    lookup_label.grid(row=index, column=num)
                    num += 1

            my_cursor.execute("SELECT rate FROM reciept")
            result = my_cursor.fetchall()
            for index, x in enumerate(result):
                num = 0
                for y in x:
                    lookup_label = Label(myframe1, text=y)
                    lookup_label.grid(row=index, column=num)
                    num += 1

            mydb.commit()
        def newwindow4():
            top4 = Toplevel()
            top.withdraw()
            top4.geometry("1600x1600")
            mainframe1 = Frame(top4, bd=10, width=770, height=700, relief=RIDGE)
            mainframe1.place(relx=0.17,rely=0.05)
            titleframe1 = Frame(mainframe1, bd=7, width=770, height=100, relief=RIDGE)
            titleframe1.grid(row=0, column=0)
            topframe3a = Frame(mainframe1, bd=5, width=770, height=500, relief=RIDGE)
            topframe3a.grid(row=1, column=0)
            leftframea = Frame(topframe3a, bd=5, width=770, height=400, padx=2, relief=RIDGE)
            leftframea.pack(side=LEFT)
            leftframe1a = Frame(leftframea, bd=5, width=600, height=180, padx=2, pady=4, relief=RIDGE)
            leftframe1a.pack(side=TOP, padx=0, pady=0)

            rightframe1a = Frame(topframe3a, bd=5, width=100, height=400, padx=2, relief=RIDGE)
            rightframe1a.pack(side=RIGHT)
            rightframe1aa = Frame(rightframe1a, bd=5, width=90, height=300, padx=1, pady=1, relief=RIDGE)
            rightframe1aa.pack(side=TOP)
            CustomerId = StringVar()
            cFirstName = StringVar()
            cLastName = StringVar()
            cGender = StringVar()
            cAge = StringVar()
            cEmail = StringVar()
            cMobileNo = StringVar()
            cAddress = StringVar()

            def cexit():
                cexit = messagebox.askyesno("Customer Database", "Confirm if you want to exit")
                if cexit > 0:
                    top4.destroy()
                    return

            def Reset():
                Ecustomerid.delete(0, END)
                Efname.delete(0, END)
                Elname.delete(0, END)
                cGender.set("")
                Eage.delete(0, END)
                Eemail.delete(0, END)
                Emobileno.delete(0, END)
                Eaddress.delete(0, END)

            def cadddata():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()
                sql_command1 = "INSERT INTO customer (customer_id,cfirst_name,clast_name,c_gender,c_age,c_email,c_mobile_no,c_address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                values1 = (
                    Ecustomerid.get(), Efname.get(), Elname.get(), Egender.get(), Eage.get(), Eemail.get(),
                    Emobileno.get(), Eaddress.get())
                my_cursor.execute(sql_command1, values1)
                # commit changes to database
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Data Entry Form", "Record Entered Successfully")

            def displaycustomerdata():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()
                my_cursor.execute("SELECT * FROM customer")
                result1 = my_cursor.fetchall()
                if len(result1) != 0:
                    for row in result1:
                        customer_record.insert('', END, values=row)
                    mydb.commit()

            def customerinfo(ev):
                viewcinfo = customer_record.focus()
                customerdata = customer_record.item(viewcinfo)
                row = customerdata['values']
                CustomerId.set(row[0])
                cFirstName.set(row[1])
                cLastName.set(row[2])
                cGender.set(row[3])
                cAge.set(row[4])
                cEmail.set(row[5])
                cMobileNo.set(row[6])
                cAddress.set(row[7])

            def updatecustomerdata():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()

                my_cursor.execute("""
                            UPDATE customer 
                            SET cfirst_name=%s,clast_name=%s,c_gender=%s,c_age=%s,c_email=%s,c_mobile_no=%s,c_address=%s 
                            WHERE customer_id=%s
                            """, (
                    cFirstName.get(), cLastName.get(), cGender.get(), cAge.get(), cEmail.get(),
                    cMobileNo.get(), cAddress.get(), CustomerId.get()))
                mydb.commit()

                mydb.close()
                messagebox.showinfo("Data Entry Form", "Record Updated Successfully")

            def deletecustomerdata(customer_record):

                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()
                selected_item1 = customer_record.selection()[0]
                print(customer_record.item(selected_item1)['values'])
                uid = customer_record.item(selected_item1)['values'][0]
                del_query1 = "DELETE FROM customer WHERE customer_id=%s"
                sel_data1 = (uid,)
                my_cursor.execute(del_query1, sel_data1)

                mydb.commit()

                mydb.close()
                customer_record.delete(selected_item1)
                Reset()
                messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")

            def csearch():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password123",
                    database="hotel",
                )
                my_cursor = mydb.cursor()

                try:


                    sql1 = "SELECT * FROM customer where customer_id='%s'"%Ecustomerid.get()
                    my_cursor.execute(sql1)
                    result1= my_cursor.fetchone()
                    cFirstName.set(result1[1])
                    cLastName.set(result1[2])
                    cGender.set(result1[3])
                    cAge.set(result1[4])
                    cEmail.set(result1[5])
                    cMobileNo.set(result1[6])
                    cAddress.set(result1[7])

                    mydb.commit()

                    mydb.close()

                except:
                    messagebox.showinfo("Data Entry Form", "No Such Record Found")
                    Reset()


            lbtitle1 = Label(titleframe1, font=('arial', 40, 'bold'), text="Customer Database ", bd=7)
            lbtitle1.grid(row=0, column=0, padx=132)

            lbcustomerid = Label(leftframe1a, font=('arial', 12, 'bold'), text="Customer Id", bd=7)
            lbcustomerid.grid(row=1, column=0, sticky=W, padx=5)
            Ecustomerid = Entry(leftframe1a, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',
                             textvariable=CustomerId)
            Ecustomerid.grid(row=1, column=1, sticky=W, padx=5)

            lbcfname = Label(leftframe1a, font=('arial', 12, 'bold'), text="First Name", bd=7)
            lbcfname.grid(row=2, column=0, sticky=W, padx=5)
            Efname = Entry(leftframe1a, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',
                           textvariable=cFirstName)
            Efname.grid(row=2, column=1, sticky=W, padx=5)

            lblcname = Label(leftframe1a, font=('arial', 12, 'bold'), text="Last Name", bd=7)
            lblcname.grid(row=3, column=0, sticky=W, padx=5)
            Elname = Entry(leftframe1a, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',
                           textvariable=cLastName)
            Elname.grid(row=3, column=1, sticky=W, padx=5)

            lbcgender = Label(leftframe1a, font=('arial', 12, 'bold'), text="Gender", bd=7)
            lbcgender.grid(row=4, column=0, sticky=W, padx=5)
            Egender = Combobox(leftframe1a, font=('arial', 12, 'bold'), width=43, state='readonly', textvariable=cGender)
            Egender['values'] = ('', 'Female', 'Male')
            Egender.current(0)
            Egender.grid(row=4, column=1)

            lbcage = Label(leftframe1a, font=('arial', 12, 'bold'), text="Age", bd=7)
            lbcage.grid(row=5, column=0, sticky=W, padx=5)
            Eage = Entry(leftframe1a, font=('arial', 12, 'bold'), bd=7, width=44, justify='left', textvariable=cAge)
            Eage.grid(row=5, column=1, sticky=W, padx=5)

            lbcemail = Label(leftframe1a, font=('arial', 12, 'bold'), text="Email", bd=7)
            lbcemail.grid(row=6, column=0, sticky=W, padx=5)
            Eemail = Entry(leftframe1a, font=('arial', 12, 'bold'), bd=7, width=44, justify='left', textvariable=cEmail)
            Eemail.grid(row=6, column=1, sticky=W, padx=5)

            lbcmobileno = Label(leftframe1a, font=('arial', 12, 'bold'), text="Mobile No", bd=7)
            lbcmobileno.grid(row=7, column=0, sticky=W, padx=5)
            Emobileno = Entry(leftframe1a, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',
                              textvariable=cMobileNo)
            Emobileno.grid(row=7, column=1, sticky=W, padx=5)

            lbcaddress = Label(leftframe1a, font=('arial', 12, 'bold'), text="Address", bd=7)
            lbcaddress.grid(row=8, column=0, sticky=W, padx=5)
            Eaddress = Entry(leftframe1a, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',
                             textvariable=cAddress)
            Eaddress.grid(row=8, column=1, sticky=W, padx=5)

            scroll_y = Scrollbar(leftframea, orient=VERTICAL)
            customer_record = Treeview(leftframea, height=12, columns=(
                "customer_id", "firstname", "lastname", "gender", "age", "email", "mobile_no", "address"),
                                       yscrollcommand=scroll_y.set)

            scroll_y.pack(side=RIGHT, fill=Y)

            customer_record.heading("customer_id", text="Customer ID")
            customer_record.heading("firstname", text="First Name")
            customer_record.heading("lastname", text="Last Name")
            customer_record.heading("gender", text="Gender")
            customer_record.heading("age", text="Age")
            customer_record.heading("email", text="Email")
            customer_record.heading("mobile_no", text="Mobile No")
            customer_record.heading("address", text="Address")

            customer_record['show'] = 'headings'

            customer_record.column("customer_id", width=60)
            customer_record.column("firstname", width=100)
            customer_record.column("lastname", width=100)
            customer_record.column("gender", width=70)
            customer_record.column("age", width=40)
            customer_record.column("email", width=150)
            customer_record.column("mobile_no", width=90)
            customer_record.column("address", width=150)

            customer_record.pack(fill=BOTH, expand=1)
            customer_record.bind("<ButtonRelease-1>",customerinfo)
            # displaydata()

            btnaddnew1 = Button(rightframe1aa, font=('arial', 16, 'bold'), text="Add New", bd=4, pady=1, padx=24, width=8,
                               height=2,command=cadddata)
            btnaddnew1.grid(row=0, column=0, padx=1)
            btndisplay1 = Button(rightframe1aa, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                width=8, height=2,command=displaycustomerdata)
            btndisplay1.grid(row=1, column=0, padx=1)
            btnupdate1 = Button(rightframe1aa, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24, width=8,
                               height=2,command=updatecustomerdata)
            btnupdate1.grid(row=2, column=0, padx=1)
            btndelete1 = Button(rightframe1aa, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24, width=8,
                               height=2,command=lambda:deletecustomerdata(customer_record))
            btndelete1.grid(row=3, column=0, padx=1)
            btnsearch1 = Button(rightframe1aa, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24, width=8,
                               height=2,command=csearch)
            btnsearch1.grid(row=4, column=0, padx=1)
            btnreset1 = Button(rightframe1aa, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24, width=8,
                              height=2,command=Reset)
            btnreset1.grid(row=5, column=0, padx=1)
            btnexit1 = Button(rightframe1aa, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24, width=8,
                             height=2,command=cexit)
            btnexit1.grid(row=6, column=0, padx=1)
            def sback1():
                top4.withdraw()
                newwindow()

            btn1back = Button(rightframe1aa, font=('arial', 16, 'bold'), text="Back", bd=4, pady=1, padx=24, width=8,
                             height=2, command=sback1)
            btn1back.grid(row=7, column=0, padx=1)

        nextb = Button(top, text="Customers", width=8, padx=4, pady=4, command=newwindow4, font=('Times', 15, 'bold'))
        nextb.place(relx=0.0, rely=0.2)
        BUTTONPRINT = Button(top, text="PRINT RECIEPT", width=15, padx=4, pady=4, font=('Times', 12, 'bold'), relief=RAISED,
                             command=newwindow1)
        BUTTONPRINT.place(relx=0.9, rely=0.85)


    else:
        labe = Label(frame1, text="Incorrect Username or Password")
        labe.place(relx=0.3, rely=0.8)

# LABELS
large_font = ('Verdana', 20)
large_font1 = ('Verdana', 15)
# label username
usernamel = Label(frame1, text="Username", padx=5, pady=5, font=large_font1)
usernamel.place(relx=0.1, rely=0.21)

# label entry for username
usernamee = Entry(frame1, width=10, font=large_font)
usernamee.place(relx=0.42, rely=0.23)
# label password
passwordl = Label(frame1, text="Password", padx=15, pady=15, font=large_font1)
passwordl.place(relx=0.11, rely=0.42)
# label entry for password
passworde = Entry(frame1, width=10, show="*", font=large_font)
passworde.place(relx=0.42, rely=0.45)
# button submit
submitb = Button(frame1, text="Submit", width=10, padx=5, pady=5, command=newwindow, font=large_font1)
submitb.place(relx=0.35, rely=0.65)

root.mainloop()
