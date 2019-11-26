class Books:
    
    books_details = {}

    def __init__(self,bid,title,pages,price):
        self.bid = bid
        self.title = title
        self.pages = pages
        self.price = price

    def view_books():
        pass
    
    def remove_book():
        pass
    
    def search_book(self):
        pass
    
    def get_details(self):
        return('Bid: {0}\nTitle: {1}\nPages: {2}\nPrice: {3}').format(self.bid,self.title,self.pages.self.price)
    
    def enter_book_details():
        book_data = []
        bid = int(input('Enter book id: '))
        title = input('Enter book title: ')
        pages = int(input('Enter book pages: '))
        price = int(input('Enter book price: '))
        book_data.append(bid)
        book_data.append(title)
        book_data.append(pages)
        book_data.append(price)
        return book_data

