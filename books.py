
class book:
  def __init__(self, book_id, title, author):
    self.book_id = book_id
    self.title = title
    self.author = author
    self.issued = False
    self.issued_to = None

    def issue_book(self, member_id):
        
        if self.issued:
          print(f"already issseud to {self.issued_to}")
        else:
          self.issued=True
          self.issued_to=member_id
        
    def return_book(self):
       if self.issued:
          self.issued=False
          self.issued_to=None
       else:
          print("already available in lib" )
          
   
