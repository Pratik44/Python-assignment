from com.pratik.books_utility.books import Books

while True:
    print('a. Enter book details.','b. View Books.','c. Search Book.','d. Remove book.','e. Exit',sep='\n')
    choice = input('Please enter a choice: ')
    if choice ==  'a':
        book_data = Books.enter_book_details()
        #Books(book_data[0],book_data[1],book_data[2],book_data[3])
        Books.books_details.update({book_data[0]:Books(book_data[0],book_data[1],book_data[2],book_data[3])})
        print(Books.books_details)
    elif choice ==  'b':
        print('View Books')
    elif choice ==  'c':
        print('Search Books')
    elif choice ==  'd':
        print('Remove Books')
    elif choice ==  'e':
        break
    else:
        print('Invalid entry. Please try again.', '-------------------------', sep='\n')


