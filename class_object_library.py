# 定義一個代表書籍的類別
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            return f"已成功借出 '{self.title}'。"
        else:
            return f"目前不可借出 '{self.title}'。"

    def return_book(self):
        if not self.available:
            self.available = True
            return f"已成功歸還 '{self.title}'。"
        else:
            return f"目前已可借閱 '{self.title}'。"

# 定義一個代表會員的類別
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        message = book.borrow_book()
        if not book.available:
            self.borrowed_books.append(book)
            print(f"{self.name} {message}")

    def return_book(self, book):
        if book in self.borrowed_books:
            message = book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} {message}")

# 建立書籍與會員的實例
# 建立書籍實例
book1 = Book("哈利波特", "J.K.羅琳")
book2 = Book("解忧杂货店", "東野圭吾")
# 建立會員實例
member1 = Member("小明", "M001")
member2 = Member("小華", "M002")

# 演示借還書流程
# 小明借了哈利波特
member1.borrow_book(book1) # 印出 "小明 已成功借出 '哈利波特'。"
# 小華嘗試借哈利波特，但已被借走
member2.borrow_book(book1) # 印出 "小華 目前不可借出 '哈利波特'。"
# 小明歸還哈利波特
member1.return_book(book1) # 印出 "小明 已成功歸還 '哈利波特'。"
# 小華這次成功借到哈利波特
member2.borrow_book(book1) # 印出 "小華 已成功借出 '哈利波特'。"
