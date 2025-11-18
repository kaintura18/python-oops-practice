class user:
    def __init__(self,name,student_id,isseued_id,role):
       self.name=name
       self.student_id=student_id
       self.book_issued= True
       self.role=role
       


class admin(user):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, "admin")

class members(user):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, "member")
        self.books_issued=[]

    MAX_limit=2

    def limited(self):
        if len(self.books_issued)>=self.MAX_limit:
            return f"issue limit reached"

    def issue_book(self,book):
        if self.limited():
            return 
        self.books_issued.append(book)

    def return_book(self,book):
        if book in self.books_issued:
            self.books_issued.remove(book)
        else:
            print("not issued")

