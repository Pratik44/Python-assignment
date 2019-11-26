import csv, pathlib

csv_file = pathlib.Path("C:\\Users\\pratik.deenbandhu\\Documents\\SRE training\\PythonAssignment\\com\\pratik\\books_utility\\book_register.csv")

class Book_register:

    def set_heading():

        if csv_file.exists():
            print("file exists")
        else:
            header = ['ID', 'TITLE', 'NO_PAGES', 'PRICE']
            print("Book register do not exist, creating new register")
            with open(csv_file, 'a') as newFile:
                writer = csv.DictWriter(newFile, fieldnames=header)
                writer.writeheader()
                writer.writerow(append_books())

            newFile.close()
'''
        with open(csv_file,'r') as readfile:
            newFileReader = csv.reader(readfile)
            for row in newFileReader:
                print(row)
'''

    def append_books():
        if csv_file.exists():
            print("Please enter new row for book: \n 'ID', 'TITLE', 'NO_PAGES', 'PRICE' " )
        else:
            Book_register.set_heading()
            print("Please enter new row for book: \n 'ID', 'TITLE', 'NO_PAGES', 'PRICE' " )
            book_dict.add()




entry_header = Book_register()
Book_register.set_heading()
'''Book_register.append_book_reg()'''



class book_dict(dict):  
  
    # __init__ function  
    def __init__(self):  
        self = dict()  
          
    # Function to add key:value  
    def add(self, ID, TITLE, NO_PAGES, PRICE):  
        self[key] = value  
  
    # Main Function  
        dict_obj = book_dict()  
        
        # Taking input key = 1, value = Geek 
        dict_obj.ID = input("Enter the ID: ") 
        dict_obj.TITLE = input("Enter the TITLE: ")       
        dict_obj.NO_PAGES = input("Enter the NO_PAGES: ") 
        dict_obj.PRICE = input("Enter the PRICE: ") 
            
        print(dict_obj)  