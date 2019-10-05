from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import pymysql
import mysql.connector
import re
import getpass


root1=Tk()
root1.title("Student Management System")
root1.geometry("400x400+200+200")

StaffLogin=Toplevel(root1)
StaffLogin.title("Staff Login")
StaffLogin.geometry('300x300+200+200')
StaffLogin.withdraw()

Register=Toplevel(root1)
Register.title("Register")
Register.geometry('300x600+200+200')
Register.withdraw()


StuLogin=Toplevel(root1)
StuLogin.title("Student Login")
StuLogin.geometry('300x400+200+200')
StuLogin.withdraw()

ChangePass=Toplevel(StuLogin)
ChangePass.title("Change Password")
ChangePass.geometry('300x400+200+200')
ChangePass.withdraw()

StaffReg=Toplevel(root1)
StaffReg.title("Staff Register")
StaffReg.geometry('300x400+200+200')
StaffReg.withdraw()


lblCname=Label(ChangePass,text="Enter Username")
entCname=Entry(ChangePass,bd=5)
lblCPassword=Label(ChangePass,text="Enter New password")
entCPassword=Entry(ChangePass,bd=7)

lblCname.pack(pady=10)
entCname.pack(pady=10)
lblCPassword.pack(pady=10)
entCPassword.pack(pady=10)

lblUname=Label(StaffLogin,text="Enter Username")
entUname=Entry(StaffLogin,bd=5)
lblPassword=Label(StaffLogin,text="Enter password")
entPassword=Entry(StaffLogin,bd=7)

lblUname.pack(pady=10)
entUname.pack(pady=10)
lblPassword.pack(pady=10)
entPassword.pack(pady=10)

lblSname=Label(StaffReg,text="Enter Username")
entSname=Entry(StaffReg,bd=5)
lblSPassword=Label(StaffReg,text="Enter password")
entSPassword=Entry(StaffReg,bd=7)
lblSubject=Label(StaffReg,text="Enter Subject")
entSubject=Entry(StaffReg,bd=5)

entPassword.config(show="*")

lblSname.pack(pady=10)
entSname.pack(pady=10)
lblSPassword.pack(pady=10)
entSPassword.pack(pady=10)
lblSubject.pack(pady=10)
entSubject.pack(pady=10)

def f20():
        StaffLogin.deiconify()
        root1.withdraw()
        

def f21():
        Register.deiconify()
        root1.withdraw()

def f22():
        StuLogin.deiconify()
        root1.withdraw()

        

def f16():
        StaffLogin.deiconify()
        root1.withdraw()
        Uname=entUname.get()
        Passname=entPassword.get()
        db=pymysql.connect('localhost','root','abc123','student')
        query=db.cursor()
        if(query.execute("select * from staff where staffid=%s and password=SHA(%s)",(str(Uname),Passname))):
                root=Toplevel(StaffLogin)
                root.title("Student Management")
                root.geometry("400x400+200+200")
                marks=Toplevel(root)
                marks.title("Enter marks")
                marks.geometry('300x300+200+200')
                vist=Toplevel(root)
                vist.title("View Student")
                vist.geometry("400x400+200+200")
                vist.withdraw()
                stViewData=scrolledtext.ScrolledText(vist,width=30,height=10)

                def f25():
                        marks.deiconify()
                        root.withdraw()

                btnMarks=Button(root,text="Enter Marks",width=10,command=f25)
                
                def f30():
                        root1.deiconify()
                        root.withdraw()
                        entUname.delete(0,'end')
                        entPassword.delete(0,'end')
                btnRootBack=Button(root,text="back",command=f30)
               
                
                lblRno3=Label(marks,text="enter rno")
                entRno3=Entry(marks,bd=5)
                lblmarks1=Label(marks,text="enter marks")
                entMarks1=Entry(marks,bd=7)

                lblRno3.pack(pady=10)
                entRno3.pack(pady=10)
                lblmarks1.pack(pady=10)
                entMarks1.pack(pady=10)
                def f26():
                        try:
                                db=pymysql.connect('localhost','root','abc123','student')
                                cursor=db.cursor()
                                rno3=int(entRno3.get())
                                if rno3<0:
                                        messagebox.showinfo("","Enter Positive Number")
                                        entRno3.delete(0,'end')
                                else:
                                        marks1=int(entMarks1.get())
                                        sql="insert into studentmarks values('%d','%d')"
                                        args=(rno3,marks1)
                                        cursor.execute(sql % args)
                                        db.commit()
                                        #for result in cursor.stored_results():
                                                #print result.fetchall()
                                        print(cursor.rowcount,"records inserted")
                                        messagebox.showinfo("sucess",str(cursor.rowcount) +" record inserted" )
                                        entRno3.delete(0,'end')
                                        entMarks1.delete(0,'end')
                                        entRno3.focus()
                        except ValueError:
                                        db.rollback()
                                        messagebox.showerror("Issue","Only Integers allowed")   
                                        entRno3.delete(0,'end')
                                        entRno3.focus()
                        except:
                                       messagebox.showerror("Error","Marks not in range")
                        finally:
                                        if cursor is not None:
                                                cursor.close()


                btnEnter=Button(marks,text="Enter",width=10,command=f26)
                btnEnter.pack(pady=20)
                def f35():
                        root.deiconify()
                        marks.withdraw()

                btnMarksBack=Button(marks,text="Back",width=10,command=f35)

               
        

                
                
                def f4():
                        root.deiconify()
                        vist.withdraw()
                        stViewData.delete('1.0',END)
                btnViewBack=Button(vist,text="back",command=f4)
                stViewData.pack()
                btnViewBack.pack()

                def f3():
                        vist.deiconify()
                        root.withdraw()
                        db=pymysql.connect('localhost','root','abc123','student')
                        cursor=db.cursor()
                        stViewData.configure(state='normal')
                        stViewData.delete('1.0',END)
                        response='select * from student1'
                        try:
                                cursor.execute(response)
                                results=cursor.fetchall()
                                info=''
                                for row in results:
                                        info=info+"rno= " +str(row[0])+" name= "+row[1]+"\n"
                                        print(info)
                        except:
                                print("Error")
                        finally:
                                if cursor is not None:
                                        cursor.close()                
                        
                        stViewData.insert(INSERT,info)
                        stViewData.configure(state='disabled')
                btnView=Button(root,text="View",width=10,command=f3)



                adst=Toplevel(root)
                adst.title("add student")
                adst.geometry('300x300+200+200')
                adst.withdraw()

                lblRno1=Label(adst,text="enter rno")
                entRno1=Entry(adst,bd=5)
                lblName1=Label(adst,text="enter name")
                entName1=Entry(adst,bd=7)

                def f5():
                        try:
                                db=pymysql.connect('localhost','root','abc123','student')
                                cursor=db.cursor()
                                rno1=int(entRno1.get())
                                if rno1<0:
                                        messagebox.showinfo("","Enter Positive Number")
                                        entRno1.delete(0,'end')
                                else:
                                        name1=entName1.get()
                                        if(not name1.isalpha()):
                                                messagebox.showinfo("","Enter proper name")
                                                entName1.delete(0,'end')
                                                entName1.focus()
                                        else:
                                                sql="insert into student1 values('%d','%s')"
                                                args=(rno1,name1)
                                                cursor.execute(sql % args)
                                                db.commit()
                                                print(cursor.rowcount,"records inserted")
                                                messagebox.showinfo("sucess",str(cursor.rowcount) +" record inserted" )
                                                entRno1.delete(0,'end')
                                                entName1.delete(0,'end')
                                                entRno1.focus()
                        except NameError:
                                print('Enter proper name')
                                db.rollback()
                                entName1.delete(0,'end')
                                entRno1.focus() 
                        except ValueError:
                                db.rollback()
                                messagebox.showerror("Issue","Only Integers allowed")   
                                entRno1.delete(0,'end')
                                entRno1.focus()
                        except:
                               messagebox.showerror("Error","Duplicates not allowed") 
                        finally:
                                if cursor is not None:
                                        cursor.close()
                                
                btnAddsave=Button(adst,text="save",command=f5)
                def f2():
                        root.deiconify()
                        adst.withdraw()
                        entRno1.delete(0,'end')
                        entName1.delete(0,'end')
                btnAddback=Button(adst,text="Back",command=f2)

                lblRno1.pack(pady=10)
                entRno1.pack(pady=10)
                lblName1.pack(pady=10)
                entName1.pack(pady=10)
                btnAddsave.pack(pady=10)
                btnAddback.pack(pady=10)

                def f1():
                        adst.deiconify()
                        root.withdraw()
                        entRno1.focus()
                btnAdd=Button(root,text="Add",width=10,command=f1)

                btnAdd.pack(pady=20)
                btnView.pack(pady=20)

                upst=Toplevel(root)
                upst.title("Update student")
                upst.geometry('300x300+200+200')
                upst.withdraw()

                lblRno=Label(upst,text="enter rno")
                entRno=Entry(upst,bd=5)
                lblName=Label(upst,text="enter name")
                entName=Entry(upst,bd=7)



                def f7():
                        con=None
                        cursor=None
                        try:
                                db=pymysql.connect('localhost','root','abc123','student')
                                cursor=db.cursor()
                                rno=int(entRno.get())
                                name=entName.get()
                                if(not name.isalpha()):
                                        messagebox.showinfo("Issue","Enter proper name")
                                        entName.delete(0,'end')
                                        entName.focus()
                                else:
                                        sql="update student1 set name='%s' where rno='%d'"
                                        args=(name,rno)
                                        cursor.execute(sql % args)
                                        db.commit()
                                        print(cursor.rowcount," records updated")
                                        messagebox.showinfo("success",str(cursor.rowcount) +" record updated" )
                                        entRno.delete(0,'end')
                                        entName.delete(0,'end')
                                        entRno.focus()
                        except NameError:
                                db.rollback()
                                entName.delete(0,'end')
                                print('Enter proper name')
                                entName.focus()
                        except ValueError:
                                db.rollback()
                                messagebox.showerror("Issue","Integers Only")
                                entRno.delete(0,'end')
                                entRno.focus()
                        finally:
                                if cursor is not None:
                                        cursor.close()
                                
                btnUpdatesave=Button(upst,text="Update",command=f7)
                def f8():
                        root.deiconify()
                        upst.withdraw()
                        entRno.delete(0,'end')
                        entName.delete(0,'end')
                btnUpdateback=Button(upst,text="Back",command=f8)

                lblRno.pack(pady=10)
                entRno.pack(pady=10)
                lblName.pack(pady=10)
                entName.pack(pady=10)
                btnUpdatesave.pack(pady=10)
                btnUpdateback.pack(pady=10)

                def f9():
                        upst.deiconify()
                        root.withdraw()
                        entRno.focus()
                btnUpdate=Button(root,text="Update",width=10,command=f9)
                btnUpdate.pack(pady=20)


                dest=Toplevel(root)
                dest.title("Update student")
                dest.geometry('300x300+200+200')
                dest.withdraw()

                lblRno2=Label(dest,text="enter rno")
                entRno2=Entry(dest,bd=5)



                def f10():
                        con=None
                        cursor=None
                        try:
                                db=pymysql.connect('localhost','root','abc123','student')
                                cursor=db.cursor()                                
                                cursor=db.cursor()
                                rno=int(entRno2.get())
                                sql="delete from student1 where rno='%d'"
                                args=(rno)
                                cursor.execute(sql % args)
                                db.commit()
                                print(cursor.rowcount," record deleted")
                                messagebox.showinfo("success",str(cursor.rowcount) +" record deleted" )
                                entRno2.delete(0,'end')
                                entRno2.focus()
                        except ValueError:
                                db.rollback()
                                messagebox.showerror("Issue","Integers only")
                                entRno2.delete(0,'end')
                                entRno2.focus()
                        finally:
                                if cursor is not None:
                                        cursor.close()

                                        
                btnDeletesave=Button(dest,text="Delete",command=f10)
                def f11():
                        root.deiconify()
                        dest.withdraw()
                        entRno2.delete(0,'end')
                btnDeleteback=Button(dest,text="Back",command=f11)

                lblRno2.pack(pady=10)
                entRno2.pack(pady=10)
                btnDeletesave.pack(pady=10)
                btnDeleteback.pack(pady=10)

                                

                def f12():
                        dest.deiconify()
                        root.withdraw()
                        entRno2.focus()
                btnDelete=Button(root,text="Delete",width=10,command=f12)
                btnDelete.pack(pady=20)
                btnMarksBack.pack(pady=10)
                btnMarks.pack(pady=20)
                btnRootBack.pack(pady=10)
                root.deiconify()
                StaffLogin.withdraw()
                print("Login")
        else:
                messagebox.showerror("Issue","Invalid Details")
                print("Invalid Details")
                entUname.delete(0,'end')
                entPassword.delete(0,'end')


entSPassword.config(show="*")
def f54():
        db=pymysql.connect('localhost','root','abc123','student')
        cursor=db.cursor()
        Sname=entSname.get()
        SPassword=entSPassword.get()
        Subject=entSubject.get()
        try:          
                sql="insert into staff values('%s',SHA('%s'),'%s')"
                args=(Sname,SPassword,Subject)
                if(Sname=="" or SPassword=="" or Subject==""):
                         #Register.deiconify()
                         messagebox.showerror("failure"," Invalid Details" )
                elif(not((len(SPassword)>5) and re.search("[a-z]", SPassword) and re.search("[A-Z]", SPassword) and re.search("[0-9]", SPassword)and re.search("[_@$]", SPassword))):
                      messagebox.showinfo("Issue","Length should be more than 5 One Uppercase,One LowerCase,One Digit,One Special Character ")  
                else: 
                        cursor.execute(sql % args)
                        print(cursor.rowcount,"records inserted")
                        messagebox.showinfo("sucess",str(cursor.rowcount) +" record inserted" )
                        db.commit()
                        entSname.delete(0,'end')
                        entSPassword.delete(0,'end')
                        entSubject.delete(0,'end')
        except:
                messagebox.showerror("failure","Username already exist" )
                

def f55():
        StaffReg.deiconify()
        root1.withdraw()               
                        
btnStaffRegister=Button(root1,text="Staff Register",width=10,command=f55)
btnStaffRegister.pack(pady=10)

btnStaffRegis=Button(StaffReg,text="Register",width=10,command=f54)
btnStaffRegis.pack(pady=10)

def f56():
        root1.deiconify()
        StaffReg.withdraw()
        entSname.delete(0,'end')
        entSPassword.delete(0,'end')
        entSubject.delete(0,'end')
        #stViewData.delete('1.0',END)
btnStaffRBack=Button(StaffReg,text="back",command=f56)

btnStaffRBack.pack(pady=10)        

btnStLogin=Button(StaffLogin,text="Login",width=10,command=f16)
btnStLogin.pack(pady=10)

lblUname1=Label(Register,text="Enter Username")
entUname1=Entry(Register,bd=5)
lblPassword1=Label(Register,text="Enter password")
entPassword1=Entry(Register,bd=7)
lblBranch=Label(Register,text="Enter Branch")
entBranch=Entry(Register,bd=7)
lblSex=Label(Register,text="Enter Sex")
entSex=Entry(Register,bd=7)

lblUname1.pack(pady=10)
entUname1.pack(pady=10)
lblPassword1.pack(pady=10)
entPassword1.pack(pady=10)
lblBranch.pack(pady=10)
entBranch.pack(pady=10)
lblSex.pack(pady=10)
entSex.pack(pady=10)
entPassword1.config(show="*")

def f17():
        db=pymysql.connect('localhost','root','abc123','student')
        cursor=db.cursor()
        Uname=entUname1.get()
        Password=entPassword1.get()
        Branch=entBranch.get()
        Sex=entSex.get()
        try:          
                sql="insert into register values('%s',SHA('%s'),'%s','%s')"
                args=(Uname,Password,Branch,Sex)
                if(Uname=="" or Password=="" or Branch=="" or Sex==""):
                         Register.deiconify()
                         messagebox.showerror("failure"," Invalid Details" )
                elif(not (Branch.isalpha() and Sex.isalpha())):
                        messagebox.showinfo("Issue","Enter proper Branch and Sex")
                        entBranch.delete(0,'end')
                        entSex.delete(0,'end')
                        entBranch.focus()
                elif(not((len(Password)>5) and re.search("[a-z]", Password) and re.search("[A-Z]", Password) and re.search("[0-9]", Password)and re.search("[_@$]", Password))):
                      messagebox.showinfo("Issue","Length should be more than 5 One Uppercase,One LowerCase,One Digit,One Special Character ")  
                else: 
                        cursor.execute(sql % args)
                        print(cursor.rowcount,"records inserted")
                        messagebox.showinfo("sucess",str(cursor.rowcount) +" record inserted" )
                        db.commit()
        except:
                messagebox.showerror("failure","Username already exist" )
                
               


btnRegister1=Button(Register,text="Register",width=10,command=f17)
btnRegister1.pack(pady=10)

lblUname2=Label(StuLogin,text="Enter Username")
entUname2=Entry(StuLogin,bd=5)
lblPassword2=Label(StuLogin,text="Enter password")
entPassword2=Entry(StuLogin,bd=7)
def f50():
        ChangePass.deiconify()
        StuLogin.withdraw()

btnChangePassword=Button(StuLogin,text="Forgot Password",width=15,command=f50)



lblUname2.pack(pady=10)
entUname2.pack(pady=10)
lblPassword2.pack(pady=10)
entPassword2.pack(pady=10)
entCPassword.config(show="*")
entPassword2.config(show="*")
def f52():
        con=None
        cursor=None
        try:
                db=pymysql.connect('localhost','root','abc123','student')
                cursor=db.cursor()
                entCname1=entCname.get()
                entCPassword1=entCPassword.get()
                if(entCname1=="" or entCPassword1==""):
                        #ChangePass.deiconify()
                        messagebox.showerror("Issue","Invalid Details")
                        print("Invalid Details")
                else:
                        sql="update register set password=SHA('%s') where uname='%s'"
                        args=(entCPassword1,entCname1)
                        cursor.execute(sql % args)
                        db.commit()
                        print(cursor.rowcount," records updated")
                        messagebox.showinfo("success",str(cursor.rowcount) +" record updated" )
                        entCname.delete(0,'end')
                        entCPassword.delete(0,'end')
                        entCname.focus()
        except NameError:
                db.rollback()
                entCname.delete(0,'end')
                print('Enter proper name')
                entCname.focus()

btnCPass=Button(ChangePass,text="Change Password",width=15,command=f52)
btnCPass.pack(pady=10)



def f18():
        StuLogin.withdraw()
        db=pymysql.connect('localhost','root','abc123','student')
        query=db.cursor()
        Uname2=entUname2.get()
        Passname2=entPassword2.get()
        if(Uname2=="" or Passname2==""):
                StuLogin.deiconify()
                messagebox.showerror("Issue","Invalid Details")
                print("Invalid Details")
        else:
                if(query.execute("select * from register where uname=%s and password=SHA(%s)",(Uname2,Passname2))):
                        print("Login");
                        root2=Toplevel(StuLogin)
                        root2.title("Student Login")
                        root2.geometry("400x400+200+200")
                        lblViewMarks=Label(root2,text="Enter Rno")
                        entViewMarks=Entry(root2,bd=5)
                        lblViewMarks.pack(pady=10)
                        entViewMarks.pack(pady=10)
                        def f31():
                                StuLogin.deiconify()
                                root2.withdraw()
                                entUname2.delete(0,'end')
                                entPassword2.delete(0,'end')
                        btnRoot2Back=Button(root2,text="back",command=f31)
                        
                        def f26():
                                db=pymysql.connect('localhost','root','abc123','student')
                                cursor=db.cursor()
                                try:
                                        rno4=int(entViewMarks.get())
                                        if(cursor.execute("select marks from studentmarks where rno=%s",(str(rno4)))):
                                                results=cursor.fetchone()
                                                for row in results:
                                                        #messagebox.showinfo("Marks ",row )
                                                        print(row)
                                                        mySQL_conn = mysql.connector.connect(host='localhost',
                                                        database='student',
                                                        user='root',
                                                        password='abc123')
                                                        cur = mySQL_conn.cursor()
                                                        d=cur.callproc('p4',[rno4,0])
                                                        c="Roll no: "+ str(d[0]) +" Marks: "+ str(row) +" Grade: "+ str(d[1])
                                                        messagebox.showinfo("results",c)


                                except:
                                        messagebox.showinfo("","Enter Positive Number")
                        btnView=Button(root2,text="View Marks",width=10,command=f26)
                        btnView.pack(pady=10)
                        btnRoot2Back.pack(pady=10)

                else:
                        StuLogin.deiconify()
                        messagebox.showerror("Issue","Invalid Details")
                        print("Invalid Details")
                        entUname2.delete(0,'end')
                        entPassword2.delete(0,'end')
                
btnStuMainLogin=Button(StuLogin,text="Login",width=10,command=f18)
btnStuMainLogin.pack(pady=10)
btnChangePassword.pack(pady=10)




btnStaffLogin=Button(root1,text="Staff Login",width=10,command=f20)
btnRegister=Button(root1,text="Register",width=10,command=f21)
btnStuLogin=Button(root1,text="Student Login",width=10,command=f22)
btnStaffLogin.pack(pady=10)
btnRegister.pack(pady=10)
btnStuLogin.pack(pady=10)


def f51():
        StuLogin.deiconify()
        ChangePass.withdraw()
        #stViewData.delete('1.0',END)
        entCname.delete(0,'end')
        entCPassword.delete(0,'end')
btnChangePassBack=Button(ChangePass,text="back",command=f51)

def f13():
        root1.deiconify()
        StaffLogin.withdraw()
        #stViewData.delete('1.0',END)
        entUname.delete(0,'end')
        entPassword.delete(0,'end')
btnStaffLoginBack=Button(StaffLogin,text="back",command=f13)

def f14():
        root1.deiconify()
        Register.withdraw()
        entBranch.delete(0,'end')
        entSex.delete(0,'end')
        entUname1.delete(0,'end')
        entPassword1.delete(0,'end')
        #stViewData.delete('1.0',END)
btnRegisterBack=Button(Register,text="back",command=f14)

def f15():
        root1.deiconify()
        StuLogin.withdraw()
        entUname2.delete(0,'end')
        entPassword2.delete(0,'end')
        #stViewData.delete('1.0',END)
btnStuLoginBack=Button(StuLogin,text="back",command=f15)

btnStaffLoginBack.pack(pady=10)
btnRegisterBack.pack(pady=10)
btnStuLoginBack.pack(pady=10)
btnChangePassBack.pack(pady=10)


'''
def f32():
        StaffLogin.deiconify()
        root1.withdraw()
'''


#btnStuLoginBack=Button(StuLogin,text="back",command=f32)


#btnStaffLoginBack.pack(pady=10)
root1.mainloop()










