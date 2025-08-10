import tkinter as tk


#  POP UP WINDOW
def Top_func(message):
	
	top_Var = tk.Tk()
	top_Var.geometry("500x40")
	top_Var.title(message)
	top_Var.resizable(False,False)
	LoginState = tk.Label(top_Var,text=message)
	LoginState.pack()
	close_button = tk.Button(top_Var,text= "Close",bg= "Red", command=top_Var.destroy)
	close_button.pack()
	
	
#  LOGIN ID Function check
def entry():
	global account_number
	account_number = accountEntry.get()

	if account_number in locked_accounts :
		Top_func("Account is locked please go to the branch")
	elif account_number not in data_dic :
		Top_func("Wrong account number")
	else :
		pass_check()	

#  LOGIN Password Function check	
def pass_check():
	global password
	password = passwordEntry.get() 
	
	if(password == data_dic[account_number][1] and data_dic[account_number][1] !=3):
		main_menu()
	else:
		data_dic[account_number][3] += 1
		if(data_dic[account_number][3] == 3):
			Top_func("you entered you password 3 times wrong Account is locked please go to the branch")
			locked_accounts.append(account_number)
			return 0
		Top_func("Wrong Password You have "+str(3-(data_dic[account_number][3]))+" Trials Left")

#Main menu Function
def main_menu():
	main_window.destroy()
	global main_menu
	main_menu = tk.Tk()
	main_menu.title("ATM Machine")
	main_menu.geometry("1000x500")
	main_menu.resizable(False,False)
	
	#Weclome message
	LoginState = tk.Label(main_menu,text="LOGIN SUCCSESSFULY \n Welcome "+str(data_dic[account_number][0])+ "\n \n \n How can we help you ? ")
	LoginState.pack()
	
	global  selected
	selected = tk.IntVar()
	#Radio Button for options
	Rad_Btn1 = tk.Radiobutton(main_menu,text= "Cash Withdraw",variable= selected ,value=1)
	Rad_Btn1.pack()

	Rad_Btn2 = tk.Radiobutton(main_menu,text= "Balance Inquiry",variable= selected, value=2)
	Rad_Btn2.pack()
	
	Rad_Btn3 = tk.Radiobutton(main_menu,text= "Password Change",variable= selected, value=3)
	Rad_Btn3.pack()
	
	Rad_Btn4 = tk.Radiobutton(main_menu,text= "Fawry Services",variable= selected, value=4)
	Rad_Btn4.pack()
	
	#Choosing Buttons 
	choose_button = tk.Button(main_menu,text= "Choose",bg= "springgreen", command=choose)
	choose_button.pack()
	
	close_button = tk.Button(main_menu,text= "Close",bg= "Red", command=main_menu.destroy)
	close_button.pack()
	
	

#BALANCE INQUIRT FUNCTION
def balance_inquiry():
	global main_menu
	main_menu.destroy()
	Top_func("Your Balance is : "+str(data_dic[account_number][2]) )
#Password window function
def password_change():
	global main_menu
	main_menu.destroy()
	global New_window
	New_window = tk.Tk()
	New_window.title("Password Change")
	New_window.geometry("500x100")
	New_window.resizable(False,False)
	global pwcheck1
	global pwcheck2	
	pwcheck1 = tk.StringVar() 
	pwcheck2 = tk.StringVar()
	
	PasswordNum2 = tk.Label(New_window,text="Please Enter your New Password ")
	PasswordNum2.place(x=0 , y=0)
	
	PasswordEntry2 = tk.Entry(New_window,show="*",textvariable=pwcheck1)
	PasswordEntry2.place(x=200,y=0)

	#label/entery for account Password
	PasswordNum3 = tk.Label(New_window,text="Re-enter new Password  ")
	PasswordNum3.place(x=0 , y=30)
	
	passwordEntry3 = tk.Entry(New_window,show="*",textvariable=pwcheck2)
	passwordEntry3.place(x=200,y=30)
	
	accountBtn = tk.Button(New_window,text="Change Password",command=check_pw_change)
	accountBtn.place(x=230,y=50)

	
#password Change Function
def check_pw_change():
	global pwcheck1 
	global pwcheck2
	if(pwcheck2.get()==pwcheck1.get() and 999<int(pwcheck1.get()) and 10000>int(pwcheck1.get()) ) :
		Top_func("Password Change Succesfully :) <3 ")
		data_dic[account_number][1] = pwcheck2.get()
		New_window.destroy()
		main_menu()
	else : 
		Top_func("Password Not matched or You didnt enter 4 digits")
#Cash withdraw Window
def cash_withdraw():
	global main_menu
	main_menu.destroy()
	global New_window
	New_window = tk.Tk() 
	New_window.title("Cash Withdraw")
	New_window.geometry("500x100")
	New_window.resizable(False,False)
	
	lb1 = tk.Label(New_window , text = "Please Enter the desired amount to withdraw") 
	lb1.place(x=100,y=10)
	
	global withdraw_amount
	withdraw_amount = tk.StringVar()
	entry = tk.Entry(New_window , textvariable =withdraw_amount)
	entry.place(x=170,y=30)
	
	btn =tk.Button(New_window,text = "Withdraw" , command = withdraw) 
	btn.place(x=200,y=50)
	
#cash withdraw function
def withdraw():
	global withdraw_amount
	global New_window
	global main_menu
	amount = int(withdraw_amount.get())
	
	if(amount>5000):
		Top_func("Max Amount To Withdraw is 5000 LE ya fa2er ")
	elif(amount%100):
		Top_func("The allowed values are multiple of 100 L.E")
	elif(amount>int(data_dic[account_number][2])):
		Top_func("YOUUU DOOOOONTT HAVEEEE MONEEEEEEEEY")
	else :
		Top_func("Thank You ")
		data_dic[account_number][2] = int(data_dic[account_number][2]) - amount 
		New_window.destroy()	
		main_menu()
#choosing function
def fawry_service():
	global main_menu
	main_menu.destroy()
	global New_window
	New_window = tk.Tk() 
	New_window.title("Fawry Service")
	New_window.geometry("500x300")
	New_window.resizable(False,False)
	
	#Weclome message
	LoginState = tk.Label(New_window,text="Welcome to Fawry services \n \n \n \n Plesae enter your Phone Number  ")
	LoginState.pack()
	PhoneNum = tk.Entry(New_window)
	PhoneNum.pack()
	
	
	global  selected
	selected = tk.IntVar()
	#Radio Button for options
	Rad_Btn1 = tk.Radiobutton(New_window,text= "Orange Recharge" ,value=1)
	Rad_Btn1.pack()

	Rad_Btn2 = tk.Radiobutton(New_window,text= "Etisalat Recharge", value=2)
	Rad_Btn2.pack()
	
	Rad_Btn3 = tk.Radiobutton(New_window,text= "Vodafone Recharge", value=3)
	Rad_Btn3.pack()
	
	Rad_Btn4 = tk.Radiobutton(New_window,text= "We Recharge", value=4)
	Rad_Btn4.pack()
	
	lb1 = tk.Label(New_window,text="Enter the recharge amount")
	lb1.pack()
	PhoneNum = tk.Entry(New_window,textvariable=selected)
	PhoneNum.pack()
	#Choosing Buttons 
	choose_button = tk.Button(New_window,text= "Recharge",bg= "springgreen", command=recharge)
	choose_button.pack()
	
def recharge():
	global selected
	global New_window
	
	if(int(selected.get())>int(data_dic[account_number][2])):
		Top_func("you dont have enough balance for recharge")
		New_window.destroy()
		main_menu()
	else:
		data_dic[account_number][2] = int(data_dic[account_number][2]) - selected.get()
		Top_func("Recharge Done")
		New_window.destroy()
		main_menu()
		
	
def choose():
	global selected
	if(selected.get() == 1) :
		cash_withdraw()
		
	elif(selected.get() == 2) :
		balance_inquiry()
		
	elif(selected.get() == 3) :
		password_change()
		
	elif(selected.get() == 4) :
		fawry_service()



# Users Data (name , Password , Balance , trials) # willing to change it to Excel reading in future upgrading
data1=["Ahmed Abdelrazek Mohamed" , "1783" , "3500166",0]
data2=["Salma Mohamed Fouad" , "1390" , "520001",0]
data3=["Adel Khaled Abdelrhamna" , "1214" , "111000",0]
data4=["Saeed ameen el sawy" , "2001" , "1200",0]
data5=["Amira Salama el gendy" , "8935" , "178933",0]
data6=["Wael mohamed Khairy" , "3420" , "55000",0]
data7=["Mina Sameh Bishoy" , "1179" , "18000",0]
data8=["Omneya Ahmed Awad" , "1430" , "180350",0]
data9=["aam" ,"1" ,"1212",0]
data_dic = {"215321701332":data1 ,"203659302214":data2 , "126355700193":data3, "201455998011":data4,"201122369851":data5,"201356788002":data6,"203366789564":data7 , "201236787812":data8 , "1":data9 }

#arry for locked accounts
locked_accounts =[]

#main window

main_window = tk.Tk() 
main_window.title("ATM Machine")
main_window.geometry("400x100")
main_window.resizable(False,False)



#label/entery for account ID
accountNum = tk.Label(main_window,text="Please Enter your Account Number: ")
accountNum.place(x=0 , y=0)
entryname_var = tk.StringVar()
accountEntry = tk.Entry(main_window,textvariable=entryname_var)
accountEntry.place(x=200,y=0)

#label/entery for account Password
PasswordNum = tk.Label(main_window,text="Please Enter Password: ")
PasswordNum.place(x=0 , y=30)
pw = tk.StringVar()
passwordEntry = tk.Entry(main_window,show="*",textvariable=pw)
passwordEntry.place(x=200,y=30)

#Button For login
accountBtn = tk.Button(text="LOGIN",command=entry)
accountBtn.place(x=230,y=50)


main_window.mainloop()

