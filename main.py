
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="library")
myc=mydb.cursor()
#+---------------------------------------------------------------------------------------------------------------------+
#                            FUNCTIONS                                                                                                                             |
#+---------------------------------------------------------------------------------------------------------------------+

#-----------------------------------------------------------------------------------------------------------------------
#Function1
#-----------------------------------------------------------------------------------------------------------------------
def addbook():
   print("---------------------------------------------------------------------------------------")
   bc=str(input("Enter the code of book : "))
   print("---------------------------------------------------------------------------------------")
   bn=str(input("Enter the name of the book : "))
   print("---------------------------------------------------------------------------------------")
   ba=str(input("Enter the author of the book : "))
   print("---------------------------------------------------------------------------------------")
   bp=str(input("Enter the publisher of the book : "))
   print("---------------------------------------------------------------------------------------")
   bq=str(input("Enter the QTY of the book : "))
    
   myc.execute("insert into Books values("+bc+",'"+bn+"','"+ba+"','"+bp+"',"+bq+")")
   mydb.commit()
   print("---------------------------------------------------------------------------------------")
   print("Data Entered succesfully ")
   print("---------------------------------------------------------------------------------------")
   a = str(input("want to continue enter 'yes' else press any key "))
   if a == "yes":
      addbook()
   else :
      main()

#----------------------------------------------------------------------------------------------------------------------
#Function 2
#----------------------------------------------------------------------------------------------------------------------           

def issue():
   name=str(input("Enter the name : "))
   print("---------------------------------------------------------------------------------------")
   reg=str(input("Enter the Reg no  : "))
   print("---------------------------------------------------------------------------------------")
   bc=str(input("Enter the Book code : "))
   print("---------------------------------------------------------------------------------------")
   date=str(input("Enter the date (yyyy-mm-dd) : "))
   print("---------------------------------------------------------------------------------------")
   myc.execute("insert into issue values("+reg+",'"+name+"',"+bc+",'"+date+"',NULL,NULL)")
   mydb.commit()
   myc.execute("select QTY from books where Book_code = "+ bc)
   a = myc.fetchall()
   x = a[0]
   b = int(x[0]) - 1
   z= str(b)
   if b >= 0:
      myc.execute("update books set QTY = "+z+ " where Book_code = " +bc)
      mydb.commit()
      print("---------------------------------------------------------------------------------------")
      print("Book is successfully issued")
      print("---------------------------------------------------------------------------------------")
   else :
      print("---------------------------------------------------------------------------------------")
      print("books not available ")
      print("---------------------------------------------------------------------------------------")
   def more_2():
      ad = input("Enter 'yes' to issue more 'no' for main menu : ")
      print("---------------------------------------------------------------------------------------")
      if ad == "yes":
         issue()
      elif ad == "no":
         main()
      else :
         print("wrong input")
         more_2()
   more_2()

#----------------------------------------------------------------------------------------------------------------------
#Function 3
#----------------------------------------------------------------------------------------------------------------------

def submition():
   r = str(input("Enter the reg no : "))
   d = str(input("Enter the date of submition (yyyy-mm-dd) : "))
   myc.execute("update issue set submit = 'submited' , submit_date = '"+d+"' where reg_no = " +r )
   mydb.commit()
   myc.execute("select * from issue where reg_no = "+r)
   a = myc.fetchall()
   for d in a:
      l,m,n,o,p,q = d
      ns = str(n)
      myc.execute("update books set QTY = QTY +1 where Book_code = "+ns)
      mydb.commit()
      print("---------------------------------------------------------------------------------------")
      print("Book is successfully submitted")
      print("reg no = ",l," B code = ",n," date of submition ",q)
      print("---------------------------------------------------------------------------------------")
      def more_3():
         b=str(input("Enter 'yes' for submit more 'no' for main menu : "))
         if b == "yes":
            submition()
         elif b == "no":
            main()
         else :
            more_3()
      more_3()

#----------------------------------------------------------------------------------------------------------------------            
#Function 4
#----------------------------------------------------------------------------------------------------------------------

def  edit():
   bc = str(input("Enter the book_code : "))
   print("---------------------------------------------------------------------------------------")
   print(" 1. modify Book name ")
   print(" 2. modify Author'name ")
   print(" 3. modify Publisher' name ")
   print(" 4. modify QTY")
   print(" 5  return to  main menu ")
   print("---------------------------------------------------------------------------------------")
   while True:
      a = str(input("Enter your choise : "))
      print("---------------------------------------------------------------------------------------")
      if a == "1":
         b =str(input("Enter the name : "))
         myc.execute("update books set book_name = '"+b+"' where book_code = "+bc)
         mydb.commit()
         print("---------------------------------------------------------------------------------------")
         print("Reocrd is succesfully edited")
         print("---------------------------------------------------------------------------------------")
         while True:
            c = str(input("Want to continue enter 'yes' else 'no' :"))
            if c == "yes":
               edit()
            elif c == "no":
               main()
            else :
               print("ERROR")
               continue

      elif a == "2":
         b =str(input("Enter the author's_name : "))
         myc.execute("update books set Author = '"+b+"' where book_code = "+bc)
         mydb.commit()
         print("---------------------------------------------------------------------------------------")
         print("Reocrd is succesfully edited")
         print("---------------------------------------------------------------------------------------")
         while True :
            c = str(input("Want to continue enter 'yes' else 'no' :"))
            if c == "yes":
               edit()
            elif c == "no":
               main()
            else :
               print("ERROR")
               continue
      elif a == "3":
         b =str(input("Enter the publisher'sname : "))
         myc.execute("update books set publisher = '"+b+"' where book_code = "+bc)
         mydb.commit()
         print("---------------------------------------------------------------------------------------")
         print("Reocrd is succesfully edited")
         print("---------------------------------------------------------------------------------------")
         while True :
            c = str(input("Want to continue enter 'yes' else 'no' :"))
            if c == "yes":
               edit()
            elif c == "no":
               main()
            else :
               print("ERROR")
               continue

      elif a == "4":
         b =str(input("Enter the QTY : "))
         myc.execute("update books set QTY = '"+b+"' where book_code = "+bc)
         mydb.commit()
         print("---------------------------------------------------------------------------------------")
         print("Reocrd is succesfully edited")
         print("---------------------------------------------------------------------------------------")
         while True :
            c = str(input("Want to continue enter 'yes' else 'no' :"))
            if c == "yes":
               edit()
            elif c == "no":
               main()
            else :
               print("ERROR")
               continue    
      elif a == "5":
         main()
      else :
         print("ERROR")
         continue
     
#----------------------------------------------------------------------------------------------------------------------            
#Function 5
#----------------------------------------------------------------------------------------------------------------------         

def display():
   print("---------------------------------------------------------------------------------------")
   print(" 1. display all record ")
   print(" 2. show as per ISBN no.  ")
   print(" x. main menu ")
   print("---------------------------------------------------------------------------------------")
   def again():
      a = str(input("Enter your choise : "))
      print("---------------------------------------------------------------------------------------")
      if a == "1":
         myc.execute("select * from books ")
         a = myc.fetchall()
         print("+-----------+---------------------+--------------------+--------------------+-----+")
         print("| Book code |      Book name      |       Author       |     Publisher      | Qty |")
         print("+-----------+---------------------+--------------------+--------------------+-----+")
         for i in a:
            print("|",i[0],end='')
            for j in range (len(str(i[0])),10):
               print(" ",end='')
            print("|",i[1],end='')
            for k in range (len(i[1]),20):
               print(" ",end='')
            print("|",i[2],end='')
            for l in range (len(i[2]),19):
               print(" ",end='')
            print("|",i[3],end='')
            for m in range (len(i[3]),19):
               print(" ",end='')
            print("|",i[4],end='')
            for n in range (len(str(i[4])),4):
               print(" ",end = '')
            print("|")
               
         print("+-----------+---------------------+--------------------+--------------------+-----+")   
         display()

      elif a == "2":
         b = str(input("Enter the ISBN No. : "))
         myc.execute("select * from books where Book_code = "+b)
         y = myc.fetchall()
         for w in y:
            print("---------------------------------------------------------------------------------------")
            print("Book name. : ", w[1])
            print("Book's Author : ",w[2])
            print("Book's Publisher : ",w[3])
            print("Book's Qty : ",w[4])
         print("---------------------------------------------------------------------------------------")
         def more_6():
            print("Enter 'y' for more or 'n' for display  ")
            b = str(input("Enter : "))
            if b == "y":
               again()
            elif b == "n":
               display()
            else :
               more_6()
         more_6()
      elif a == "x":
         main()
      else:
         again()
   again()
#----------------------------------------------------------------------------------------------------------------------            
#Function 6
#----------------------------------------------------------------------------------------------------------------------

def delete():
   while True:
      print("1. to delete a record ")
      print("2. to delete all records")
      print("x. to jump over main menu")
      d = str (input("Enter : "))
      if d == "1":
         print("---------------------------------------------------------------------------------------")
         a = str(input("Enter the book code to delete "))
         print("---------------------------------------------------------------------------------------")
         b = str(input("Are u sure (yes/no) : "))
         print("---------------------------------------------------------------------------------------")
         if b == "yes":
            myc.execute("delete from books where book_code ="+a)
            mydb.commit()
            print(" 'Record delete successfully '")
            print("---------------------------------------------------------------------------------------")
            def more_7():
               c = str(input("want to continue (yes/no)"))
               print("---------------------------------------------------------------------------------------")
               if c == "yes":
                  delete()
               elif c == "no":
                  main()
               else :
                  print("ERROR")
                  print("---------------------------------------------------------------------------------------")
                  more_7()

         elif b == "no":
            main()

         else :
            print("ERROR")
            print("---------------------------------------------------------------------------------------")
            continue
      elif d == "2":
         print("---------------------------------------------------------------------------------------")
         print("are u sure 'yes' to proceed 'no' to return over main menu ")
         while True:
            e = str(input("Enter : "))
            if e == "yes":
               myc.execute("delete from books")
               mydb.commit()
               print("---------------------------------------------------------------------------------------")
               print("All records are deleted succesfully")
               print("---------------------------------------------------------------------------------------")
               main()
            elif e == "no":
               main()
            else :
               print("ERROR")
               print("---------------------------------------------------------------------------------------")
               continue
      elif d == "x" :
         main()

      else:
         continue


#----------------------------------------------------------------------------------------------------------------------            
#                                       MAIN FUNCTION
#----------------------------------------------------------------------------------------------------------------------               

print("=========================================================")
print("             %WELCOME TO LIBRARY MANAGEMENT SYSTEM/                                  ")
print("=========================================================")
print("                               %USER INTERFACE/  ")
print("=========================================================")
def main():
   print("Enter 1. for Add a book ")
   print("Enter 2. for Issue book ")
   print("Enter 3. for Book submition ")
   print("Enter 4. for Edit the entry ")
   print("Enter 5. for Display the record ")
   print("Enter 6. for Deleting a record ")
   print("Enter Quit. to end ")
   print("----------------------------------------------------------------------------------------------")
    
    
   a = str(input("Enter your choise : "))
   if a == "1":
      addbook()
   elif a == "2":
      issue()
   elif a == "3":
      submition()
   elif a == "4":
      edit()
   elif a == "5":
      display()
   elif a == "6":
      delete()
   elif a == "Quit" or a == "quit" :
      quit()
   else :
      print("----------------------------------------------------------------------------------------------")
      print("ERROR")
      print("INCORRECT VALUE")
      print("----------------------------------------------------------------------------------------------")
      main()
       
           
#================================================================================================
def password():
   a = str(input("Enter the password (123) : "))
   print("----------------------------------------------------------------------------------------------")
   if a == "123":
      main()
   else :
       
      print("ERROR")
      print("try again ")
      print("----------------------------------------------------------------------------------------------")
      password()
                        
password()      

                        
#==========================================================================================================
                         
