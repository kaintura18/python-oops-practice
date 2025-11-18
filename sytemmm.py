from books import book
from user import admin,members


class lib_system:
    def __init__(self):
        self.books = []
        self.users = []

    def add_member(self, user_id, name):
        if any(u.user_id == user_id for u in self.users):
            return f"Member {user_id} already exists"
        new_member = members(user_id, name)
        self.users.append(new_member)
        return new_member

    def add_admin(self, user_id, name):
        if any(u.user_id == user_id for u in self.users):
            return f"User {user_id} already exists"
        new_admin = admin(user_id, name)
        self.users.append(new_admin)
        return new_admin

    def add_book(self,book_id,title,author):
        if self.book_id not in self.Books:
            new_book=book(book_id,title,author)
            self.Books.append(new_book)
     
    def remove_book(self,book_id):
        for self.book_id in self.Books:
                self.Books.remove(self.book_id)
                return f"Book with id {book_id} removed"
        print("Book not found")
        
