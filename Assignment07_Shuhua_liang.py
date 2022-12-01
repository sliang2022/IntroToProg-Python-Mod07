# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# Shuhua Liang, 2022-11-30, Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []
list_of_data =[]

# Processing  --------------------------------------------------------------- #
class Processor:
    def save_data_to_file(file_name, list_of_data):
        with open(file_name, 'wb') as f:
            pickle.dump(list_of_data, f)
        return list_of_data


    def read_data_from_file(file_name):
        with open(file_name, 'rb') as file_obj:
            list_of_data = pickle.load(file_obj)
        return list_of_data



class IO:
    @staticmethod
    def input_menu_choice():
        choice = str(input("Do you want to add new data? [Yes or No] - ")).lower()
        return choice

    @staticmethod
    def input_new_int_ID_and_Name():
        # pass  # TODO: Add Code Here!
        int_ID = input("Add ID: ")
        Name = input("Please enter Name: ")
        return (int_ID, Name)

    @staticmethod
    def output_current_tasks_in_list(list_of_data):
        print("******* The current ID and Name list: *******")
        for row in list_of_data:
            print("ID:", row["int_ID"], " Name:", row["Name"] )
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def add_data_to_list(int_ID, Name, list_of_data):
        row = {"int_ID": int(int_ID), "Name": str(Name)}
        # TODO: Add Code Here!
        list_of_data.append(row)
        # append a new dictionary to the list

        return list_of_data


# Presentation ------------------------------------ #
# TODO: Get int_ID and NAME From user, then store it in a list object
while True:
    choice_str = IO.input_menu_choice()  # Get menu option

    if choice_str == 'no':
        break
    elif choice_str == 'yes':
        int_ID, Name = IO.input_new_int_ID_and_Name()
        #print(int_ID, Name)
        try:
            lstCustomer = IO.add_data_to_list(int_ID=int_ID, Name=Name, list_of_data=lstCustomer)
# TODO: add more except sections to capture the specific derived exceptions!
        except ValueError as e:
            print("*****************Error Message!******************")
            print("Please enter an integer as ID. Name should be a string!!")
            print("*****************Data not added!******************")
    else:
        print('please enter Yes or No')


# TODO: store the list object into a binary file
table_lst = Processor.save_data_to_file(file_name=strFileName, list_of_data=lstCustomer)
#print("Data Saved!")


# TODO: Read the data from the file into a new list object and display the contents
lstCustomer = Processor.read_data_from_file(strFileName)
IO.output_current_tasks_in_list(list_of_data=lstCustomer)  # Show current data in the list/table
