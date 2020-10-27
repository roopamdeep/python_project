import socket
import json
import csv

c = socket.socket()

c.connect(('localhost', 9999))
msg = c.recv(65535)
print(msg.decode('utf-8'))

def mainMenu():
    print("Python DB Menu")
    print("-----------------------------")
    print("1. Find customer")
    print("2. Add customer")
    print("3. Delete customer")
    print("4. Update customer age")
    print("5. Update customer address")
    print("6. Update customer phone")
    print("7. Print Report")
    print("8. Exit")
    while True:
        choice = int(input("Select: "))
        #print(choice)
        if  choice==1:
            choice = str(choice).strip()
            c.send(str.encode(choice))
            findCustomer()
            break
        elif choice==2:
             choice = str(choice).strip()
             c.send(str.encode(choice))
             addCustomer()
             break
        elif choice==3:
            choice = str(choice)
            c.send(str.encode(choice))
            delCustomer()
            break
        elif choice == 4:
             choice = str(choice)
             c.send(str.encode(choice))

             update_age()
             break
        elif choice == 5:
            choice = str(choice)
            c.send(str.encode(choice))

            update_address()
            break
        elif choice == 6:
            choice = str(choice)
            c.send(str.encode(choice))

            update_phone()
            break
        elif choice == 7:
            choice = str(choice)
            c.send(str.encode(choice))
            printReport()
            break
        elif choice == 8:
            choice = str(choice)
            c.send(str.encode(choice))
            bye()
            break
        else:
            print('Sorry, Invalid Choice. Enter numbers between 1-8')
            mainMenu()

    exit


def findCustomer():
    name = input('Enter name: ').strip()
    if not(name.isspace() or name == ""):
        pass
    else:
        print('Name Field cannot be empty')
        name = input('Enter name: ').strip()

    c.send(str.encode(name))

    message = c.recv(65536).decode('utf-8')
    #print(message)
    valuelist = message.split(",")
    #print(valuelist)
    #print(len(valuelist))
    if(len(valuelist) == 1):
        print(message)
    else:

        print("Age: ", valuelist[0])
        print("Address: ", valuelist[1])
        print("Phone Number: ", valuelist[2])

    #print(message)
    pressrandomkey = input("Enter any key to return to main menu")
    mainMenu()


def addCustomer():
    name = input('Enter Name Of The Customer to be added: ').strip()
    if not(name == "" or name.isspace()):
        pass
    else:
        print('Name Field cannot be empty')
        name = input('Enter Name Of The Customer to be added: ').strip()
    c.send(str.encode(name))

    age = (input('Enter Age:')).strip()
    #age = str(age)
    if(age.isspace() or age == ""):
        c.sendall(str.encode("\00",'ascii'))
    else:
        try:
            age = float(age)
        except Exception:
            print("Enter Age In Integers`:")
            age = float(input("Enter Age:"))


        if not (age.is_integer()):
            print("Please enter age in Integers.")
            age = (input('Enter Age:'))
        else:
            age = int(age)
        c.send(str.encode(str(age).strip()))
    address = input('Enter Address:').strip()
    if(address.isspace() or address == ""):
        c.sendall(str.encode("\00", 'ascii'))
    else:
        c.sendall(str.encode(address))
    phonenumber = input('Enter Phone No:').strip()
    if(phonenumber.isspace() or phonenumber == ""):
        #print("phne", phonenumber)
        c.sendall(str.encode("\00",'ascii'))
    else:
        c.sendall(str.encode(phonenumber))

    message = c.recv(65536).decode('utf-8')
    print(message)
    pressrandomkey = input("Enter any key to return to main menu")
    mainMenu()


def delCustomer():
    name = input('Enter Name Of The Customer to be deleted: ').strip()
    if name is not "" or name.isspace():
        pass
    else:
        print('Name Field cannot be empty')
        name = input('Enter Name Of The Customer to be deleted: ').strip()
    c.send(str.encode(name))

    message = c.recv(65535).decode()
    print(message)
    pressrandomkey = input("Enter any key to return to main menu")
    mainMenu()

def update_age():
    name = input('Enter Name Of The Customer to be updated: ').strip()
    if (name is not "" or name.isspace()):
        pass
    else:
        print('Name Field cannot be empty')
        name = input('Enter Name Of The Customer to be updated: ').strip()
    c.send(str.encode(name))
    age = input('Enter Age:')
    #age = str(age)
    if(age.isspace() or age == ""):
        c.sendall(str.encode("\00",'ascii'))
    else:
        age = float(age)
        if not (age.is_integer()):
            print("Please add age in integers.")
        else:
            age = int(age)
            c.sendall(str.encode(str(age).strip()))

        #c.send(str.encode(str(age).strip()))

    message = c.recv(1024).decode()
    print(message)
    pressrandomkey = input("Enter any key to return to main menu")
    mainMenu()
def update_address():
    name = input('Enter Name Of The Customer to be updated: ').strip()
    if (name is not "" or name.isspace()):
        pass
    else:
        print('Name Field cannot be empty')
        name = input('Enter Name Of The Customer to be updated: ').strip()
    c.send(str.encode(name))
    address = input('Enter Address:').strip()
    if(address.isspace() or address == ""):
        c.sendall(str.encode("\00",'ascii'))

    c.send(str.encode(address))
    message = c.recv(1024).decode()
    print(message)
    pressrandomkey = input("Enter any key to return to main menu")
    mainMenu()
def update_phone():
    name = input('Enter Name Of The Customer to be updated: ')
    if (name is not "" or name.isspace()):
        pass
    else:
        print('Name Field cannot be empty')
        name = input('Enter Name Of The Customer to be updated: ').strip()
    c.send(str.encode(name))
    phonenumber = input('Enter Phone No:').strip()
    if(phonenumber.isspace() or phonenumber == ""):
        c.sendall(str.encode("\00",'ascii'))
    c.send(str.encode(phonenumber))
    message = c.recv(1024).decode()
    print(message)
    pressrandomkey = input("Enter any key to return to main menu")
    mainMenu()

def printReport():
    message = json.loads(c.recv(65535).decode('utf-8'))
    data = message
    print("------------------------------------------------------------------------------------")
    print('{:<15}{:<6}{:<40}{:<}'.format("Name", "Age", "Address", "Phone-Number"))
    print("------------------------------------------------------------------------------------")
    # print(data)
    for value in data.items():
        name = value[0]
        age = value[1][0]
        address = value[1][1]
        phone = value[1][2]
        print('{:<15}{:<6}{:<40}{:<}'.format(name, age, address, phone))

    pressrandomkey = input("Enter any key to return to main menu")
    mainMenu()

def bye():
    # c.send(str.encode("bye"))
    message = "Good-Bye!"
    print(message)
    exit(0)




mainMenu()

