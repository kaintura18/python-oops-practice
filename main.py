from sytemm import lib_system 


lib=lib_system()


lib.add_admin("A001","Admin One")
lib.add_admin("A001","ken")
lib.add_member("M001","amine") 


lib.add_book("B001","The Great Gatsby","F. Scott Fitzgerald")
lib.add_book("B002","To Kill a Mockingbird","Harper Lee")

print(lib.issue_book("B001","M001"))
print(lib.issue_book("B001","M001"))  # Trying to issue the same book 

print(lib.return_book("B001","M001"))
print(lib.return_book("B001","M001"))  # Trying to return the same book
print(lib.remove_book("B002"))
