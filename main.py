import json

choice = [1,2,3,4,5,6]
result = None
error = False

def main():
    print("##################################") # #x34
    print("#   Welcome to employee system   #")
    print("##################################")
    print("# Plese select choice")
    print("# 1. Insert Data                 #")
    print("# 2. Delete Data                 #")
    print("# 3. Search Data by EmpID        #")
    print("# 4. Search All Data             #")
    print("# 5. Edit Data                   #")
    print("# 6. Exit                        #")
    print("##################################")
    try:
        result = int(input("Plese select choice (1-6 only) : "))
        # if result == 6:
        #     pass
        # if result > 6:
        #     result = int(input("Plese select choice (1-6 only) : "))
        #     return result
        return result
    except ValueError:
        # print("Data Type Error Plese Try Agian :(")
        pass

def insert_data():
    # trap a error
    try:
        # find last employee id
        with open('./data.txt', "r") as file:
            data = file.readlines() # get employee data
            new_id = json.loads(data[-1].strip(', \n'))['EmpID'] # convert last index employee data from str to dict and get EmpID value
            EmpID = new_id + 1 # generate employee id
            # start input employee data
            print("Plese Insert Employee Data")
            Name = str(input("Name        : ")) # input employee name
            if len(Name) <= 0: # check empty employee name
                print("Employee Name Is Empty, Plese Try Again!!")
                return
            Surname = str(input("Surname     : ")) # input employee surname
            if len(Surname) <= 0: # check empty employee surname
                print("Employee Surname Is Empty, Plese Try Again!!")
                return
            Position = str(input("Position    : ")) # input employee position
            if len(Position) <= 0: # check empty employee position
                print("Employee Position Is Empty, Plese Try Again!!")
                return
            Salary = float(input("Salary      : ")) # input employee salary
            if len(str(Salary)) <= 0:  # check empty employee salary
                print("Employee Salary Is Empty, Plese Try Again!!")
                return
            # insert employee is to file
            with open("./data.txt", "a") as file:
                file.write(f"{{"
                        f"\"EmpID\": {EmpID}, "
                        f"\"Name\": \"{Name}\", "
                        f"\"Surname\": \"{Surname}\", "
                        f"\"Position\": \"{Position}\", "
                        f"\"Salary\": {Salary}"
                        f"}} , \n")
            print("Insert Data Complete!!")
    # print error
    except ValueError:
        print("Data Type Error Plese Try Agian :(")
    except FileNotFoundError:
        print("Plese Insert Employee Data")
        Name = str(input("Name        : ")) # input employee name
        if len(Name) <= 0: # check empty employee name
            print("Employee Name Is Empty, Plese Try Again!!")
            return
        Surname = str(input("Surname     : ")) # input employee surname
        if len(Surname) <= 0: # check empty employee surname
            print("Employee Surname Is Empty, Plese Try Again!!")
            return
        Position = str(input("Position    : ")) # input employee position
        if len(Position) <= 0: # check empty employee position
            print("Employee Position Is Empty, Plese Try Again!!")
            return
        Salary = float(input("Salary      : ")) # input employee salary
        if len(str(Salary)) <= 0:  # check empty employee salary
            print("Employee Salary Is Empty, Plese Try Again!!")
            return
        EmpID = 1
        with open("./data.txt", "a") as file:
            file.write(f"{{"
                f"\"EmpID\": {EmpID}, "
                f"\"Name\": \"{Name}\", "
                f"\"Surname\": \"{Surname}\", "
                f"\"Position\": \"{Position}\", "
                f"\"Salary\": {Salary}"
                f"}} , \n")
            print("Insert Data Complete!!")

def delete_data():
    index = 0
    try:
        with open("./data.txt", "r") as file:
            data = file.readlines()
            data_id = int(input("Enter Employee ID That You Want To Remove : "))
            for i in data:
                index += 1
                i = json.loads(i.strip(', \n'))
                if i['EmpID'] == data_id:
                    print("")
                    print(f"Employee id : {i['EmpID']}")
                    print(f"Name        : {i['Name']}")
                    print(f"Surname     : {i['Surname']}")
                    print(f"Position    : {i['Position']}")
                    print(f"Salary      : {float(i['Salary'])}")
                    check = str(input("Do You Want To Delete This Data (Y or N) : ")).upper()
                    if check == "Y":
                        data[index - 1] = ""
                        with open('./data.txt', 'w') as file:
                            file.writelines(data)
                    elif check == "N":
                        pass
                    else:
                        print("Sory You Can Enter Just (Y or N) Plese Try Agian :(")
                    error = False
                    break
                else:
                    error = True
                    continue
        if error == True:
            print("Can't Found Data :(")
    except ValueError:
        print("Data Type Error Plese Try Agian :(")
    except FileNotFoundError:
        print("You Can Insert Employee First!!!")

def search_data_id():
    try:
        with open('./data.txt', "r") as file:
            data = file.read().split(" , ")
            id = int(input("Plese Enter Employee ID For Search : "))
            for i in data:
                try:
                    i = json.loads(i) # Convert str to dict
                    if i["EmpID"] == id:
                        print("Data Found!!!")
                        print(f"Employee id : {i['EmpID']}")
                        print(f"Name        : {i['Name']}")
                        print(f"Surname     : {i['Surname']}")
                        print(f"Position    : {i['Position']}")
                        print(f"Salary      : {float(i['Salary'])}")
                        error = False
                        break
                    else:
                        error = True
                        continue
                except json.JSONDecodeError as e:
                    pass
            if error == True:
                print("Can't Found Data :(")
    except FileNotFoundError:
        print("You Can Insert Employee First!!!")
            
def search_all():
    try:
        with open("./data.txt", "r") as file:
            data = file.read().split(" , ")
            print("\n")
            for i in data:
                try:
                    i = json.loads(i)
                    print(f"Employee id : {i['EmpID']}")
                    print(f"Name        : {i['Name']}")
                    print(f"Surname     : {i['Surname']}")
                    print(f"Position    : {i['Position']}")
                    print(f"Salary      : {float(i['Salary'])}")
                    print("##################################")
                except json.JSONDecodeError as e:
                    # print("Error decoding JSON:", e)
                    pass
    except FileNotFoundError:
        print("You Can Insert Employee First!!!")

def edit_data():
    try:
        index = 0
        with open('data.txt', 'r') as file:
            data = file.readlines()
            print("\n")
            edit_id = int(input("Plese Enter Employee ID For Edit : "))
            for i in data:
                index += 1
                i = json.loads(i.strip(', \n'))
                if i['EmpID'] == edit_id:
                    print("\n")
                    print("Current Data")
                    print(f"Employee id : {i['EmpID']}")
                    print(f"Name        : {i['Name']}")
                    print(f"Surname     : {i['Surname']}")
                    print(f"Position    : {i['Position']}")
                    print(f"Salary      : {float(i['Salary'])}")
                    print()
                    want_edit = str(input("Do You Want To Edit Data (Y or N) : ")).upper()
                    if want_edit == "Y":
                        print("Plese Enter New Data")
                        Name = str(input("Name        : ")) # input employee name
                        if len(Name) <= 0: # check empty employee name
                            print("Employee Name Is Empty, Plese Try Again!!")
                            return
                        Surname = str(input("Surname     : ")) # input employee surname
                        if len(Surname) <= 0: # check empty employee surname
                            print("Employee Surname Is Empty, Plese Try Again!!")
                            return
                        Position = str(input("Position    : ")) # input employee position
                        if len(Position) <= 0: # check empty employee position
                            print("Employee Position Is Empty, Plese Try Again!!")
                            return
                        Salary = float(input("Salary      : ")) # input employee salary
                        if len(str(Salary)) <= 0:  # check empty employee salary
                            print("Employee Salary Is Empty, Plese Try Again!!")
                            return
                        data[index -1] = (
                            f'{{'
                            f'"EmpID": {edit_id}, '
                            f'"Name": "{Name}", '
                            f'"Surname": "{Surname}", '
                            f'"Position": "{Position}", '
                            f'"Salary": {Salary}'
                            f'}} , \n'
                        )
                        with open('data.txt', "w") as file:
                            file.writelines(data)
                            print("Edit Data Complete!!!")
                    elif want_edit == "N":
                        pass
                    else:
                        print("Sory You Can Enter Just (Y or N) Plese Try Agian :(")
                    error = False
                    break
                else:
                    error = True
                    continue
        if error == True:
            print("Can't Found Data :(")
    except ValueError:
        print("Data Type Error Plese Try Agian :(")
    except FileNotFoundError:
        print("You Can Insert Employee First!!!")

if __name__ == "__main__":
    try:
        result = main()
        while result not in choice:
            result = int(input("Plese select choice (1-6 only) : "))
        if result == 1:
            insert_data()
        elif result == 2:
            delete_data()
        elif result == 3:
            search_data_id()
        elif result == 4:
            search_all()
        elif result == 5:
            edit_data()
        elif result == 6:
            pass
        else:
            print("Somthing Error :(")
    except ValueError:
        print("Somthing Error Plese Try Again :(")
        
# pyinstaller <FILENAME>.py --onefile