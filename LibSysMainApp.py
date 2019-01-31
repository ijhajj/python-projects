"""
Module to Enter the Inventory Details
Tab Name: Add Inventory
Details: Name of the Book
         Author of the Book
         Year of print
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import LibSysBackEnd
from datetime import date
from datetime import timedelta



window=Tk()

window.title(" Book Library")
window.geometry("500x545+30+30")

nb = ttk.Notebook(window)

#********************************************
# EDIT FUNCTIONS
#********************************************
def addBookEdits():
	editInd=''
	if ((title_text.get() == "" )or (author_text.get()=="")or (year_text.get()=="")):
		messagebox.showinfo("Edit Failure", "Please ensure Book Title/Author Name/Year details are populated")
		editInd='N'
		return editInd

	if ((year_text.get().isdigit()) == False):
		messagebox.showinfo("Edit Failure", "Please enter valid Year details")
		editInd = 'N'
	return editInd

def addMemberEdits():
	editInd=''
	if ((first_name.get())==""or (last_name.get())=="" or (address_text.get())=="" or (mobile_number.get())==""):
		messagebox.showinfo("Edit Failure", "Please ensure Member Name/Address/Mobile Number details are populated")
		editInd='N'
		return editInd

	if ((mobile_number.get().isdigit()) == False):
		messagebox.showinfo("Edit Failure", "Please enter valid Mobile Number details")
		editInd = 'N'
	return editInd

def issueReturnEdits(book_Name,member_Name,radioButtonSelection):
	editInd = ''
	if book_Name == '':
		messagebox.showinfo("Edit Failure", "Please Select a Book")
		editInd = 'N'
	if radioButtonSelection==1:
		if member_Name=='':
			messagebox.showinfo("Edit Failure", "Please Select a Member")
			editInd = 'N'
	return editInd


#********************************************
# DATABASE FUNCTIONS
#********************************************

def addBookCommand():
	editInd=addBookEdits()
	if editInd != 'N':
		LibSysBackEnd.addBook(title_text.get(),author_text.get(),year_text.get())
		messagebox.showinfo("Confirmation", "Book has been successfully ADDED")
		ea1.delete(0,END)
		ea2.delete(0,END)
		ea3.delete(0, END)


def addMemCommand():
	editInd=addMemberEdits()
	if editInd != 'N':
		LibSysBackEnd.addMember(first_name.get(),last_name.get(),address_text.get(),mobile_number.get())
		messagebox.showinfo("Confirmation", "Member has been successfully ADDED")
		ea4.delete(0, END)
		ea5.delete(0, END)
		ea6.delete(0, END)
		ea7.delete(0, END)

def searchBookCommand():
	listb1.delete(0,END)
	if (book_author_name.get()==''):
		for row in LibSysBackEnd.searchAllBooks():
			listb1.insert(END, row)
	else:
		for row in LibSysBackEnd.searchBook(book_author_name.get()):
			listb1.insert(END,row)

def searchMemberCommand():
	listb2.delete(0, END)
	if(member_first_last_name.get()==''):
		for row in LibSysBackEnd.searchAllMembers():
			listb2.insert(END, row)
	else:
		for row in LibSysBackEnd.searchMember(member_first_last_name.get()):
			listb2.insert(END, row)

def refreshMainTab(event):
	cntBooks_ref=LibSysBackEnd.totalBooks()
	ltb1_value['text']=cntBooks_ref

	cntMembers_ref = LibSysBackEnd.totalMembers()
	ltb2_value['text']=cntMembers_ref

	cntIssuedBooks_ref = LibSysBackEnd.totalIssuedBooks()
	ltb3_value['text'] = cntIssuedBooks_ref

	cntOverdueBooks_ref = LibSysBackEnd.totalOverdueBooks(todays_dt)
	ltb4_value['text'] = cntOverdueBooks_ref

#********************************************
# MAIN SCREEN
#********************************************
TabMain=ttk.Frame(nb)
nb.grid(row=1,column=0)
nb.add(TabMain,text="Welcome")

lfx=LabelFrame(TabMain,text="Welcome",padx=40,pady=40)
lfx.grid(padx=(20,10),pady=(20,10),row=20,column=0)

ltb1=Label(lfx,text="Shreya's Library ",width=25, font=("bold",16),fg="darkblue")
ltb1.grid(row=0,column=0)


lfw=LabelFrame(TabMain,text="Summary",padx=40,pady=40)
lfw.grid(padx=(20,10),pady=(20,10),row=40,column=0)

ltb1=Label(lfw,text="Total Books :  ",width=25,anchor="w")
ltb1.grid(row=0,column=0)

cntBooks=LibSysBackEnd.totalBooks()
ltb1_value=Label(lfw,text=cntBooks,width=5)
ltb1_value.grid(row=0,column=1)

ltb2=Label(lfw,text="Total Members : ",width=25,anchor="w")
ltb2.grid(row=1,column=0)

cntMembers=LibSysBackEnd.totalMembers()
ltb2_value=Label(lfw,text=cntMembers,width=5)
ltb2_value.grid(row=1,column=1)

ltb3=Label(lfw,text="Total Issued Books : ",width=25,anchor="w")
ltb3.grid(row=2,column=0)

cntIssuedBooks=LibSysBackEnd.totalIssuedBooks()
ltb3_value=Label(lfw,text=cntIssuedBooks,width=5)
ltb3_value.grid(row=2,column=1)

ltb4=Label(lfw,text="Total Overdue Books : ",width=25,anchor="w")
ltb4.grid(row=3,column=0)

todays_dt=date.today()
cntOverdueBooks=LibSysBackEnd.totalOverdueBooks(todays_dt)
ltb4_value=Label(lfw,text=cntOverdueBooks,width=5)
ltb4_value.grid(row=3,column=1	)

nb.bind('<<NotebookTabChanged>>',refreshMainTab)

#********************************************
# GLOBAL VARIABLES
#********************************************
title_text=StringVar()
author_text=StringVar()
year_text=StringVar()
first_name = StringVar()
last_name = StringVar()
address_text = StringVar()
mobile_number=StringVar()

book_tuple=()
member_tuple=()
mem_tuple=()


#********************************************
# TAB NAME : ADD BOOK/MEMBER
#********************************************
Tab1=ttk.Frame(nb)
nb.grid(row=1,column=0,columnspan=500,rowspan=499,sticky="NESW")
nb.add(Tab1,text="Add")

lf1=LabelFrame(Tab1,text="NEW Book",padx=10,pady=40)
lf1.grid(padx=(20,10),pady=(20,10),row=0,column=0)

la1=Label(lf1,text="Title  ",width=15)
la1.grid(row=0,column=0)

ea1 = Entry(lf1,textvariable=title_text,width=30)
ea1.grid(row=0,column=1)

la2=Label(lf1,text="Author ",width=15)
la2.grid(row=1,column=0)

ea2 = Entry(lf1,textvariable=author_text,width=30)
ea2.grid(row=1,column=1)

la3=Label(lf1,text="Year ",width=15)
la3.grid(row=2,column=0)

ea3 = Entry(lf1,textvariable=year_text,width=30)
ea3.grid(row=2,column=1)


b1=Button(lf1,text="Submit",command=addBookCommand)
b1.grid(row=3,column=1)

lf2=LabelFrame(Tab1,text="NEW Member",padx=30,pady=40)
lf2.grid(padx=(20,10),pady=(20,10),row=10,column=0)

la4=Label(lf2,text="First Name   ")
la4.grid(row=0,column=0)


ea4=Entry(lf2,textvariable=first_name,width=30)
ea4.grid(row=0,column=1)

la5=Label(lf2,text="Last Name   ")
la5.grid(row=1,column=0)


ea5=Entry(lf2,textvariable=last_name,width=30)
ea5.grid(row=1,column=1)

la6=Label(lf2,text="Address   ")
la6.grid(row=2,column=0)


ea6=Entry(lf2,textvariable=address_text,width=30)
ea6.grid(row=2,column=1)

la7=Label(lf2,text="Mobile No.")
la7.grid(row=3,column=0)


ea7=Entry(lf2,textvariable=mobile_number,width=30)
ea7.grid(row=3,column=1)

b1=Button(lf2,text="Submit",command=addMemCommand)
b1.grid(row=4,column=1)






#********************************************
# TAB NAME : SEARCH/EDIT BOOK
#********************************************
Tab2=ttk.Frame(nb)
nb.grid(row=1,column=0,columnspan=400,rowspan=399,sticky="NESW")
nb.add(Tab2,text="Search/Edit")

lm6=Label(Tab2,text="SEARCH Criteria :     ",fg="darkblue",font=("Helvetica"))
lm6.grid(row=0,column=0)

lbbook=Label(Tab2,text="BOOK ",fg="darkblue",font=("Helvetica"))
lbbook.grid(row=1,column=0)

lb1=Label(Tab2,text="Book/Author Name",width=15)
lb1.grid(row=2,column=0)

book_author_name=StringVar()
eb1=Entry(Tab2,textvariable=book_author_name,width=30)
eb1.grid(row=2,column=1)


bb1=Button(Tab2,text="Search",command=searchBookCommand)
bb1.grid(row=3,column=1)

#create the scroll bar for the list box
sb1=Scrollbar(Tab2,orient=VERTICAL)
sb1.grid(row=5,column=30,sticky="NS")
sbHoriz1=Scrollbar(Tab2,orient=HORIZONTAL)
sbHoriz1.grid(row=15,column=1,sticky="EW")

#create a list box
listb1=Listbox(Tab2,height=5,width=30,yscrollcommand=sb1.set,xscrollcommand=sbHoriz1.set)
listb1.grid(row=5,column=1)

sb1.configure(command=listb1.yview)
sbHoriz1.configure(command=listb1.xview)


def selectedBook_Edit(event):
	if len(listb1.curselection()) == 0:
		pass
	else:
		index = listb1.curselection()[0]
		selected_Book = listb1.get(index)
		book_tuple = selected_Book
		editPopUp(book_tuple)


listb1.bind('<<ListboxSelect>>', selectedBook_Edit)

def editPopUp(book_tuple):
	editPU1 = Toplevel()
	editPU1.minsize(width=400,height=100)
	editPU1.maxsize(width=400,height=100)

	book_id=book_tuple[0]
	issued_status=book_tuple[4]

	lbv1=Label(editPU1,text="Title",width=10)
	lbv1.grid(row=0,column=0)


	title_edit=StringVar(value=book_tuple[1])
	ebv1 = Entry(editPU1,textvariable=title_edit,width=30)
	ebv1.grid(row=0,column=1,columnspan=3)


	lbv2=Label(editPU1,text="Author",width=10)
	lbv2.grid(row=1,column=0)

	author_edit=StringVar(value=book_tuple[2])
	ebv2 = Entry(editPU1,textvariable=author_edit,width=30)
	ebv2.grid(row=1,column=1,columnspan=3)


	lbv3=Label(editPU1,text="Year",width=10)
	lbv3.grid(row=2,column=0)

	year_edit=StringVar(value=book_tuple[3])
	ebv3 = Entry(editPU1,textvariable=year_edit,width=30)
	ebv3.grid(row=2,column=1,columnspan=3)

	def changeBookEdits():
		editInd = ''
		if ((title_edit.get() == "") or (author_edit.get() == "") or (year_edit.get() == "")):
			messagebox.showinfo("Edit Failure", "Please ensure Book Title/Author Name/Year details are populated")
			editInd = 'N'
			return editInd

		if ((year_edit.get().isdigit()) == False):
			messagebox.showinfo("Edit Failure", "Please enter valid Year details")
			editInd = 'N'
		return editInd

	def saveChngSuccess():
		editInd = changeBookEdits()
		if (editInd == 'N'):
			editPU1.destroy()
			return
		if (issued_status == 'Y'):
			messagebox.showinfo("Edit Failure", "Book is in issued status. CANNOT be updated")
		else:
			LibSysBackEnd.updateBook(title_edit.get(),author_edit.get(),year_edit.get(),book_id)
			messagebox.showinfo("Confirmation","Book has been successfully UPDATED")
			listb1.delete(0, END)
		editPU1.destroy()


	bbv1=Button(editPU1,text="Update",command=saveChngSuccess)
	bbv1.grid(row=3,column=1)


	def delBookSuccess():
		if(issued_status=='Y'):
			messagebox.showinfo("Edit Failure", "Book is in issued status. CANNOT be deleted")
		else:
			LibSysBackEnd.deleteBook(book_id)
			messagebox.showinfo("Confirmation","Book has been successfully DELETED")
			listb1.delete(0, END)
		editPU1.destroy()


	bbv2=Button(editPU1,text="Delete ",command=delBookSuccess)
	bbv2.grid(row=3,column=2)


	editPU1.focus_force()

def clearlistb1():
	listb1.delete(0, END)

bbclear1=Button(Tab2,text="Clear",command=clearlistb1)
bbclear1.grid(row=24,column=1)

#------------------------------------------------
# SEARCH/EDIT : MEMBER DETAILS
#------------------------------------------------

lbmember=Label(Tab2,text="MEMBER ",fg="darkblue",font=("Helvetica"))
lbmember.grid(row=25,column=0)

lb2=Label(Tab2,text="First/Last Name",width=15)
lb2.grid(row=31,column=0)

member_first_last_name=StringVar()
eb2=Entry(Tab2,textvariable=member_first_last_name,width=30)
eb2.grid(row=31,column=1)


bb2=Button(Tab2,text="Search",command=searchMemberCommand)
bb2.grid(row=32,column=1)

#create the scroll bar for the list box
sb2=Scrollbar(Tab2,orient=VERTICAL)
sb2.grid(row=33,column=30,sticky="NS")
sbHoriz2=Scrollbar(Tab2,orient=HORIZONTAL)
sbHoriz2.grid(row=43,column=1,sticky="EW")

#create a list box
listb2=Listbox(Tab2,height=5,width=30,yscrollcommand=sb2.set,xscrollcommand=sbHoriz2.set)
listb2.grid(row=33,column=1)

sb2.configure(command=listb2.yview)
sbHoriz2.configure(command=listb2.xview)

def selectedMember_Edit(event):
	if len(listb2.curselection()) == 0:
		pass
	else:
		index = listb2.curselection()[0]
		selected_Mem = listb2.get(index)
		mem_tuple = selected_Mem
		editPopUpMem(mem_tuple)


listb2.bind('<<ListboxSelect>>', selectedMember_Edit)

def editPopUpMem(mem_tuple):
	editPUMem = Toplevel()
	editPUMem.minsize(width=400,height=120)
	editPUMem.maxsize(width=400,height=120)

	client_id=mem_tuple[0]

	lbmv1=Label(editPUMem,text="First Name",width=15)
	lbmv1.grid(row=0,column=0)


	first_name_edit=StringVar(value=mem_tuple[1])
	ebmv1 = Entry(editPUMem,textvariable=first_name_edit,width=30)
	ebmv1.grid(row=0,column=1,columnspan=3)


	lbmv2=Label(editPUMem,text="Last Name",width=15)
	lbmv2.grid(row=1,column=0)

	last_name_edit=StringVar(value=mem_tuple[2])
	ebmv2 = Entry(editPUMem,textvariable=last_name_edit,width=30)
	ebmv2.grid(row=1,column=1,columnspan=3)


	lbmv3=Label(editPUMem,text="Address",width=15)
	lbmv3.grid(row=2,column=0)

	address_edit=StringVar(value=mem_tuple[3])
	ebmv3 = Entry(editPUMem,textvariable=address_edit,width=30)
	ebmv3.grid(row=2,column=1,columnspan=3)

	lbmv4 = Label(editPUMem, text="Mobile Number", width=15)
	lbmv4.grid(row=3, column=0)

	mob_number_edit = StringVar(value=mem_tuple[4])
	ebmv4 = Entry(editPUMem, textvariable=mob_number_edit, width=30)
	ebmv4.grid(row=3, column=1, columnspan=3)


	def changeMemberEdits():
		editInd = ''
		if ((first_name_edit.get()) == "" or (last_name_edit.get()) == "" or (address_edit.get()) == "" or (
		mob_number_edit.get()) == ""):
			messagebox.showinfo("Edit Failure", "Please ensure Member Name/Address/Mobile Number details are populated")
			editInd = 'N'
			return editInd

		if ((mob_number_edit.get().isdigit()) == False):
			messagebox.showinfo("Edit Failure", "Please enter valid Mobile Number details")
			editInd = 'N'
		return editInd

	def saveChngSuccess():
		editInd=changeMemberEdits()
		if editInd != 'N':
			LibSysBackEnd.updateMember(first_name_edit.get(),last_name_edit.get(),address_edit.get(),mob_number_edit.get(),client_id)
			messagebox.showinfo("Confirmation","Client has been successfully UPDATED")
			listb2.delete(0, END)
		editPUMem.destroy()


	bbv1=Button(editPUMem,text="Update",command=saveChngSuccess)
	bbv1.grid(row=4,column=1)


	def deleteMemberEdits():
		editInd = ''
		rows=LibSysBackEnd.chkIssuedBookOnClient(client_id)
		if not rows:
			pass
		else:
			messagebox.showinfo("Edit Failure", "Book(s) issued to Client, CANNOT be deleted")
			editInd='N'
		return editInd

	def delMemSuccess():
		editInd=deleteMemberEdits()
		if(editInd!='N'):
			LibSysBackEnd.deleteMember(client_id)
			messagebox.showinfo("Confirmation","Client has been successfully DELETED")
			listb2.delete(0, END)
		editPUMem.destroy()


	bbv2=Button(editPUMem,text="Delete ",command=delMemSuccess)
	bbv2.grid(row=4,column=2)

def clearlistb2():
	listb2.delete(0, END)

bbclear2=Button(Tab2,text="Clear",command=clearlistb2)
bbclear2.grid(row=44,column=1)

#********************************************
# TAB NAME : ISSUE/RETURN BOOK
#********************************************
Tab3 = ttk.Frame(nb)
nb.grid(row=1,column=0,columnspan=400,rowspan=399,sticky="NESW")
nb.add(Tab3,text="Issue/Return")

#-------------------------------------
# SEARCH BOOK CODE
#-------------------------------------
lcf1=LabelFrame(Tab3,text="SEARCH Book :",padx=30,pady=20)
lcf1.grid(padx=(20,10),pady=(20,10),row=0,column=0)

lc2=Label(lcf1,text="Book/Author Name",width=15)
lc2.grid(row=0,column=0)

iss_book_author_name=StringVar()
ec2=Entry(lcf1,textvariable=iss_book_author_name,width=30)
ec2.grid(row=0,column=1,columnspan=2)


def editBookSearchPopUp():

	def selectBook(event):
		if len(listc1.curselection())==0:
			pass
		else:
			index = listc1.curselection()[0]
			selected_Book = listc1.get(index)
			book_tuple = selected_Book
			lc11a_bookName['text']=book_tuple[1]
			lc11b_bookID['text']=book_tuple[0]

	editPU2 = Toplevel()
	editPU2.minsize(width=400,height=110)
	editPU2.maxsize(width=400,height=110)

	#create a list box
	listc1=Listbox(editPU2,height=5,width=47)
	listc1.grid(row=0,column=1,rowspan=10,columnspan=15)

	#create the scroll bar for the list box
	sc1=Scrollbar(editPU2,orient=VERTICAL)
	sc1.grid(row=0,column=30,sticky="NS")

	listc1.configure(yscrollcommand=sc1.set)
	sc1.configure(command=listc1.yview)

	listc1.delete(0, END)
	if (iss_book_author_name.get()==''):
		for row in LibSysBackEnd.searchAllBooks():
			listc1.insert(END, row)
	else:
		for row in LibSysBackEnd.searchBook(str(iss_book_author_name.get())):
			listc1.insert(END, row)

	listc1.bind('<<ListboxSelect>>', selectBook)

	def CloseBookPopUp():
		editPU2.destroy()

	bcv1=Button(editPU2,text="Close",command=CloseBookPopUp)
	bcv1.grid(row=11,column=8)

bc1=Button(lcf1,text="Search",command=editBookSearchPopUp)
bc1.grid(row=3,column=1)

lc11=Label(lcf1,text="BOOK   ",fg="darkblue",font=("Helvetica"))
lc11.grid(row=4,column=0)

lc11a_bookName=Label(lcf1,text="",font=5)
lc11a_bookName.grid(row=4,column=1)

#This is a hidden Label to store interim data
lc11b_bookID=Label(lcf1,text="",state=DISABLED,disabledforeground=lcf1.cget('bg'))
lc11b_bookID.grid(row=5,column=1)

#-------------------------------------
# SEARCH MEMBER CODE
#-------------------------------------

lcf2=LabelFrame(Tab3,text="SEARCH Member :",padx=30,pady=20)
lcf2.grid(padx=(20,10),pady=(20,10),row=15,column=0)

lc7=Label(lcf2,text="First/Last Name/Mob No")
lc7.grid(row=0,column=0)

first_last_name_mobile = StringVar()
ec7=Entry(lcf2,textvariable=first_last_name_mobile,width=30)
ec7.grid(row=0,column=1,columnspan=2)


def editMemberSearchPopUp():
	def selectMember(event):
		if len(listc2.curselection())==0:
			pass
		else:
			index = listc2.curselection()[0]
			selected_Member = listc2.get(index)
			member_tuple=selected_Member
			lc12a['text']=member_tuple[1:3]
			lc12b_clientID['text']=member_tuple[0]


	editPU3 = Toplevel()
	editPU3.minsize(width=400,height=110)
	editPU3.maxsize(width=400,height=110)

	#create a list box
	listc2=Listbox(editPU3,height=5,width=47)
	listc2.grid(row=0,column=1,rowspan=10,columnspan=15)

	#create the scroll bar for the list box
	sc2=Scrollbar(editPU3,orient=VERTICAL)
	sc2.grid(row=0,column=30,sticky="NS")

	listc2.configure(yscrollcommand=sc2.set)
	sc2.configure(command=listc2.yview)

	listc2.delete(0, END)
	if (first_last_name_mobile.get() == ''):
		for row in LibSysBackEnd.searchAllMembers():
			listc2.insert(END, row)
	else:
		for row in LibSysBackEnd.searchMember(first_last_name_mobile.get()):
			listc2.insert(END, row)

	listc2.bind('<<ListboxSelect>>', selectMember)

	def CloseMemberPopUp():
		editPU3.destroy()

	bcv2=Button(editPU3,text="Close",command=CloseMemberPopUp)
	bcv2.grid(row=11,column=8)

bc1=Button(lcf2,text="Search",command=editMemberSearchPopUp)
bc1.grid(row=3,column=1)

lc12=Label(lcf2,text="MEMBER   ",fg="darkblue",font=("Helvetica"))
lc12.grid(row=4,column=0)

lc12a=Label(lcf2,text="",font=5)
lc12a.grid(row=4,column=1)

lc12b_clientID=Label(lcf2,text="",state=DISABLED,disabledforeground=lcf1.cget('bg'))
lc12b_clientID.grid(row=5,column=1)
#-------------------------------------
# ISSUE/RETURN CODE
#-------------------------------------
lcf3=LabelFrame(Tab3,text="ISSUE/RETURN :",padx=30,pady=20)
lcf3.grid(padx=(20,10),pady=(20,10),row=19,column=0)

lc10=Label(lcf3,text="Date of Return")
lc10.grid(row=0,column=0)

today=date.today()
default_issue_dt=today+ timedelta(days=14)

issued_till_dt=StringVar(value=default_issue_dt)
ec10=Entry(lcf3,textvariable=issued_till_dt,width=30)
ec10.grid(row=0,column=1,columnspan=2)

radioSelect=IntVar()
r1=Radiobutton(lcf3,text="Issue",variable=radioSelect,value=1)
r1.grid(row=1,column=0)

r2=Radiobutton(lcf3,text="Return",variable=radioSelect,value=2)
r2.grid(row=1,column=1)

def Issue_Return_Book():
	if(radioSelect.get()==0):
		messagebox.showinfo("Edit Failure", "Please select either Issue or Return Radio Button")
		return
	book_Name = lc11a_bookName['text']
	member_Name = lc12a['text']
	radioButtonSelection=radioSelect.get()
	editInd = issueReturnEdits(book_Name,member_Name,radioButtonSelection)
	if editInd=='N':
		return
	selectedBookId = lc11b_bookID['text']
	selectedClientId = lc12b_clientID['text']
	row = LibSysBackEnd.chkIssuedStatusBook(selectedBookId)
	if radioSelect.get()== 1:
		if (row[0]=='Y'):
			messagebox.showinfo("Edit Failure", "Book is already in ISSUED status")
		else:
			LibSysBackEnd.issueBook(selectedBookId, today, issued_till_dt.get(),selectedClientId)
			messagebox.showinfo("Confirmation","Book is Issued SUCCESSFULLY")
			lc11a_bookName['text']=''
			lc11b_bookID['text']=''
			lc12a['text'] = ''
			ec2.delete(0,END)
			ec7.delete(0,END)
	else:
		if(row[0]=='N'):
			messagebox.showinfo("Edit Failure", "Book is NOT in ISSUED status")
		else:
			LibSysBackEnd.returnBook(selectedBookId)
			messagebox.showinfo("Confirmation", "Book is Returned SUCCESSFULLY")
			lc11a_bookName['text'] = ''
			lc11b_bookID['text'] = ''
			lc12a['text']=''
			ec2.delete(0, END)
			ec7.delete(0, END)




bc2=Button(lcf3,text=" Submit  ",command=Issue_Return_Book)
bc2.grid(row=2,column=1)


#********************************************
# TAB NAME : NOTIFICATIONS
#********************************************
Tab4 = ttk.Frame(nb)
nb.grid(row=1,column=0,columnspan=400,rowspan=399,sticky="NESW")
nb.add(Tab4,text="Notifications")

#create a list box
ld1 = Label(Tab4,text="OVERDUE Books :   ",fg="darkblue",font=("Helvetica"))
ld1.grid(row=0,column=0)

listd1=Listbox(Tab4,height=5,width=30)
listd1.grid(row=1,column=1)

#create the scroll bar for the list box
sd1=Scrollbar(Tab4)
sd1.grid(row=1,column=30)

listd1.configure(yscrollcommand=sd1.set)
sd1.configure(command=listd1.yview)

def overdueBookDetails(event):
	if len(listd1.curselection()) == 0:
		pass
	else:
		ed1.delete(0,END)
		ed2.delete(0, END)
		ed3.delete(0, END)
		ed10.delete(0,END)
		ed4.delete(0, END)
		ed5.delete(0, END)
		ed6.delete(0, END)
		ed7.delete(0, END)
		index = listd1.curselection()[0]
		selected_Book = listd1.get(index)
		book_tuple = selected_Book
		ed1.insert(END,book_tuple[1])
		ed2.insert(END,book_tuple[2])
		ed3.insert(END,book_tuple[3])
		ed10.insert(END,book_tuple[6])
		client_tuple=LibSysBackEnd.fetchMembershipDetails(book_tuple[7])
		ed4.insert(END,client_tuple[1])
		ed5.insert(END,client_tuple[2])
		ed6.insert(END, client_tuple[3])
		ed7.insert(END, client_tuple[4])

current_dt=date.today()
listd1.delete(0, END)
for row in LibSysBackEnd.chkOverdueBooks(current_dt):
	listd1.insert(END, row)

listd1.bind('<<ListboxSelect>>', overdueBookDetails)

#Book Details
lm3=Label(Tab4,text="BOOK Details :       ",fg="darkblue",font=("Helvetica"))
lm3.grid(row=13,column=0)

ld1=Label(Tab4,text="Title  ",width=15)
ld1.grid(row=15,column=0)

title_value=StringVar()
ed1 = Entry(Tab4,textvariable=title_value,width=30)
ed1.grid(row=15,column=1)

ld2=Label(Tab4,text="Author ",width=15)
ld2.grid(row=16,column=0)

author_value=StringVar()
ed2 = Entry(Tab4,textvariable=author_value,width=30)
ed2.grid(row=16,column=1)

ld3=Label(Tab4,text="Year ",width=15)
ld3.grid(row=17,column=0)

year_value=StringVar()
ed3 = Entry(Tab4,textvariable=year_value,width=30)
ed3.grid(row=17,column=1)
#BookLayout(Tab4,15)

lspace3=Label(Tab4,text="")
lspace3.grid(row=18,column=0)
#Member Details
lm4=Label(Tab4,text="MEMBER Details :   ",fg="darkblue",font=("Helvetica"))
lm4.grid(row=19,column=0)

ld4=Label(Tab4,text="First Name   ")
ld4.grid(row=20,column=0)

first_value=StringVar()
ed4=Entry(Tab4,textvariable=first_value,width=30)
ed4.grid(row=20,column=1)

ld5=Label(Tab4,text="Last Name   ")
ld5.grid(row=21,column=0)

last_value=StringVar()
ed5=Entry(Tab4,textvariable=last_value,width=30)
ed5.grid(row=21,column=1)

ld6=Label(Tab4,text="Address   ")
ld6.grid(row=22,column=0)

address_value=StringVar()
ed6=Entry(Tab4,textvariable=address_value,width=30)
ed6.grid(row=22,column=1)

ld7=Label(Tab4,text="Mobile No.")
ld7.grid(row=23,column=0)

mobile_value=StringVar()
ed7=Entry(Tab4,textvariable=mobile_value,width=30)
ed7.grid(row=23,column=1)

lspace4=Label(Tab4,text="")
lspace4.grid(row=24,column=0)

#Issue Details
lm5=Label(Tab4,text="DUE Details :       ",fg="darkblue",font=("Helvetica"))
lm5.grid(row=25,column=0)

ld10=Label(Tab4,text="RETURN Date ")
ld10.grid(row=26,column=0)

return_date=StringVar()
ed10=Entry(Tab4,textvariable=return_date,width=30)
ed10.grid(row=26,column=1)

window.mainloop()