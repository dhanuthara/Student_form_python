#student Registration form
import tkinter as tk

window=tk.Tk()
window.title("Student Register form")
window.geometry("450x450")


def submitvalue():
    print(entry1.get())
    print(entry2.get())
    print(entry3.get())
    print(entry4.get())
    print(entry5.get())
    print(entry6.get())
    
    #file store
    #file=open("py_1.txt","x")
    file=open("py_1.txt","a")
    file.write("\n")
    file.write("Fname:")
    file.write(str(entry1.get()))
    file.write("\n")
    file.write("Lname:")
    file.write(str(entry2.get()))
    file.write("\n")
    file.write("Email:")
    file.write(str(entry3.get()))
    file.write("\n")
    file.write("PhoneNo:")
    file.write(str(entry4.get()))
    file.write("\n")
    file.write("standared:")
    file.write(str(entry5.get()))
    file.write("\n")
    file.write("Address:")
    file.write(str(entry6.get()))
    file.write("\n")
    file.write("________________________________________________")
    file.close()

#first name
label1=tk.Label(window,text="First Name:")
label1.grid(row=1,column=1,padx=10,pady=20)
entry1=tk.Entry(window,text="")
entry1.grid(row=1,column=2)


#last name
label2=tk.Label(window,text="Last Name:")
label2.grid(row=2,column=1,padx=10,pady=20)
entry2=tk.Entry(window,text="")
entry2.grid(row=2,column=2)

#email
label3=tk.Label(window,text="Email:")
label3.grid(row=3,column=1,padx=10,pady=20)
entry3=tk.Entry(window,text="")
entry3.grid(row=3,column=2)

#Phonenumber
label4=tk.Label(window,text="Phone Number:")
label4.grid(row=4,column=1,padx=10,pady=20)
entry4=tk.Entry(window,text="")
entry4.grid(row=4,column=2)

#Standerdname
label5=tk.Label(window,text="Standared:")
label5.grid(row=5,column=1,padx=10,pady=20)
entry5=tk.Entry(window,text="")
entry5.grid(row=5,column=2)

#Address
label6=tk.Label(window,text="Address:")
label6.grid(row=6,column=1,padx=10,pady=20)
entry6=tk.Entry(window,text="")
entry6.grid(row=6,column=2)

button1=tk.Button(window,text="Submit",command=submitvalue)
button1.grid(row=7,column=2)












