import socket
import json
import csv

fileOpen = open("data.txt")
# contents = fileOpen.read()
myDictionary = {}
records = tuple()
for line in fileOpen:
    line = line.strip('\n')  # to mark end of line in data file.
    line = line.replace("\t", "")
    records = line.split("|")
    records = tuple(records)
    # print(type(records))
    # print(records)
    if records[0].isspace():  # If record has no name, skip that record.
        continue
    else:
        myDictionary[records[0]] = records[1:]

# print(myDictionary)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp connection made

print('server started')
s.bind(('localhost', 9999))  # binding of socket to server

s.listen(3)  # 3 clients

print('waiting for connections')
c, addr = s.accept()

print('Connection Established From: ', addr)

message = "Welcome to First Python Assignment"
c.send(str.encode(message))
while True:
    choice = c.recv(65535)
    choice = choice.decode('utf-8')
    # print(choice)
    choice = int(choice)
    print("choice -- ",choice)
    # records = re.split('\n', contents.replace("\t", " "))
    # print(records)
    # myDictionary = {}

    # rcrd = ();

    # for data in records:
    # newrecord = tuple(data.split("|"))  # customer record will be a tuple to represnt the value of a key
    # rcrd = (newrecord,) + rcrd

    # listoftuples = list(rcrd)
    # print(listoftuples)

    # print(myDictionary)

    if choice == 1:
        name = c.recv(65535).decode("utf-8")
        print(name)
        if name in myDictionary.keys():
            data = (myDictionary[name])  # getting all the values
            print(data)
            #print(type(data))
            resp = str(data[0]) + "," + data[1] + "," + data[2]
            print(resp)
            c.send(str.encode(resp))
        if name not in myDictionary.keys():
            c.send(str.encode("Customer Does not Exist"))

    if choice == 2:
        name = c.recv(65535).decode("utf-8")
        print(name)
        age = c.recv(65535).decode("utf-8")
        #age = int(age)
        print(age)
        address = c.recv(65535).decode('utf-8', 'ascii')
        print(address)
        phonenumber = c.recv(65535).decode("utf-8")
        print(phonenumber)

        if name not in myDictionary.keys():
            myDictionary.update({name: (age, address, phonenumber)})
            print(myDictionary)
            c.send(str.encode("Customer Record Added SuccessFully!"))
        else:
            c.send(str.encode("Customer Already Exists!"))

    if choice == 3:
        name = c.recv(65535).decode("utf-8")
        if name in myDictionary.keys():
            del myDictionary[name]
            # print(myDictionary)
            c.send(str.encode('Customer Record Deleted Successfully!'))
        else:
            c.send(str.encode("Customer Does not Exist!"))

    if choice == 4:
        name = c.recv(65535).decode("utf-8")
        age = c.recv(65535).decode("utf-8")

        if name in myDictionary.keys():
            data = myDictionary.get(name)
            print(data)
            listValue = list(data)
            listValue[0] = age
            data = tuple(listValue)
            myDictionary.update({name: data})
            print(myDictionary)

            c.send(str.encode("Customer Age Updated Succesfully!"))
            # print(myDictionary)
        if name not in myDictionary.keys():
            c.send(str.encode("Customer Does not Exist!"))

    if choice == 5:
        name = c.recv(65535).decode("utf-8")
        address = c.recv(65535).decode("utf-8")
        if name in myDictionary.keys():
            data = myDictionary.get(name)
            print(data)
            listValue = list(data)
            listValue[1] = address
            data = tuple(listValue)
            myDictionary.update({name: data})
            print(myDictionary)

            c.send(str.encode("Customer Address Updated Succesfully!"))
        if name not in myDictionary.keys():
            c.send(str.encode("Customer Does not Exist!"))

    if choice == 6:
        name = c.recv(65535).decode("utf-8")
        phonenumber = c.recv(65535).decode("utf-8")
        if name in myDictionary.keys():
            data = myDictionary.get(name)
            print(data)
            listValue = list(data)
            listValue[2] = phonenumber
            data = tuple(listValue)
            myDictionary.update({name: data})
            print(myDictionary)

            c.send(str.encode("Customer Phone Number Updated Succesfully!"))
        if name not in myDictionary.keys():
            c.send(str.encode("Customer Does not Exist!"))

    if choice == 7:

        myreport = json.dumps(myDictionary, sort_keys=True).encode("utf-8")
        c.sendall(myreport)

    if choice == 8:

        print("Client Disconnected!")
        c,addr = s.accept()
        print("Connection Established From", addr)
        c.send(str.encode("Welcome to first python assignmnt"))

