import sys 
import mysql.connector 
mycon=mysql.connector.connect(host='localhost',user='root',passwd='parvathy') 
mycur=mycon.cursor() 
def User_details(): 
 print("\nPLEASE ENTER THE DETAILS\n") 
 mysql="insert into Scholar_Details(name,age,gender,nationality,address,ph.no)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
 admno=int(input("\nENTER THE ADMISIION  NUMBER TO REGISTER FOR EXAMINATION :  "))
 name=input("\nNAME : ") 
 age=int(input("\nAGE: ")) 
 gender=input("\n Male/Female/Others") 
 nationality=input("\nNationality ") 
 address=input("\nENTER THE CURRENT  ADDRESS : ")
 ph.no=int(input("\nEnter your mobile no.: "))
  
 values=(name,age,gender,nationality,address,ph.no) 
 mycur.execute(mysql,values) 
 try: 
  mycon.commit( )
  print(name,"ADDED SUCCESFULLY!!") 
 except: 
  print("UNABLE TO INSERT VALUES ") 


main() 