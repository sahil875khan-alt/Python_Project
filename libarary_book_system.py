class BooknotAvailableError(Exception):
    def __init__(self, message=("book is not availble!")):
        self.message = message
        super().__init__(self.message)
def borrow_book(book_name):
    book_collection = ["Python Basics","Data Sceince 101","ML crash Course"]
    if book_name not in book_collection:
        raise BooknotAvailableError(f"Sorry,{book_name} book is not availble!") 
    return book_name
try:
   
    book_name = input("Enter the book name:") 
    borrow_book(book_name)  
except BooknotAvailableError as b:
    print(b) 
else:
    print(f"{book_name} Book is issued✅")          