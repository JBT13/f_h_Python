# def func1(nums):
#     ls = []
#     for x in nums:
#         if x > 0:
#             ls.append(x)
#     return ls

# def func2(nums):
#     return sum(nums) / len(nums)

# def main():
#     data = [-2,-1,0,2,3]
#     a_list = func1(data)
#     an_list = func2(a_list)
#     print(a_list)
#     print(an_list)

# main()

# def make_unique(i_list):
#     unique_list = []
#     for item in i_list:
#         if item not in unique_list:
#             unique_list.append(item)

#     return unique_list

# i_list = [4,2,2,3,4]

# h = make_unique(i_list)

# print(h)

# def string_i(name):
#     list_1 = name.split(" ")
#     first = list_1[0] 
#     middle = list_1[1]
#     last = list_1[2]

#     initial = " "
#     names = name.split()
#     for name in names:
#         initial += name[0].upper()

#     return f"{first[0].upper()} {middle[0].upper()} {last[0].upper()}"


# name = "olafur ragnar grimson"
# intial = string_i(name)
# print(intial)

# def count_v(text):
#     vowels = ("a","e","i","o","u")
#     count = 0
#     for i in text:
#         if i in vowels:
#             count += 1

#     return count

# def elevate(grades, num):
#     for student in grades:
#         for i in range(len(grades[student])):
#             grades[student][i] = min(grades[student][i] + num, 100)

#     return grades

# try:
#     file_name = "my_file.txt"
#     file = open(file_name)
#     count = 0
#     for lines in file:
#         count += 1
#     print(f"Lines = {count}")
#     file.close()

# except FileNotFoundError:
#     print("The file does not exist")

# choice = input("Enter to append or write")
# if choice == "a":
#     file_name = "my_file.txt"
#     file = open(file_name, "a")
#     user_input = input()

#     while user_input != "":
#         user_input = input() 
    

# class StoredNumber:
#     def __init__(self, number):
#         self.number = number 

#     def get_number(self):
#         return self.number

#     def set_number(self, new_number):
#         self.number = new_number
        
#     def __str__(self):
#         return f"The number : {self.number}" 
    

# def elevate_grades(grades, num):
#     for student in grades:
#         for grade in range(len(grades[student])):
#             grades[student][grade] = min(grades[student][grade] + num, 100) 
#     return grades

# grades = {"hello": [1,2,3]}

# h = elevate_grades(grades, 5)
# print(h)

# def elevate_grades(grades, points):
#     new_result = {}
#     for student in grades:
#         new_grades = []
#         for grade in grades[student]:
#             new_grades.append(min(100, grade + points))
#         new_result[student] = new_grades
#     return new_result

# def count_lines():
#     line_list = []
#     try:
#         count = 0
#         with open("my_file.txt", "r") as file:
#             for lines in file:
#                 line_list.append(lines.strip("\n"))
#                 count += 1
#             print(f"The file has {count} lines")
        
#     except FileNotFoundError:
#         print("The file does not exist")
#     return line_list

# def should_append():
#     choice = input("Enter a to append or w to overwrite: ")
#     return choice == "a"

# def enter_lines(lines):
#     hello = "1"
#     while hello != "":
#         hello = input()
#         lines.append(hello)

# def save_files(lines):
#     with open("my_file.txt", "w") as f:
#         for line in lines:
#             f.write(line + "\n")

# def main():
#     lines = count_lines()
#     append = should_append()
#     if not append:
#         lines = []
#     print(lines)
#     enter_lines(lines)
#     save_files(lines)


# class StoredNumber:
#     def __init__(self, num):
#         self.num = num

#     def __str__(self):
#         return f"The number: {self.num}"

#     def get_number(self):
#         return self.num 

#     def set_number(self, num):
#         self.num = num

# class Book:
#     def __init__(self, id, title, author, is_loaned = False):
#         self.id = id
#         self.title = title
#         self.author = author
#         self.is_loaned = is_loaned 
    
#     def __str__(self):
#         return f"{self.id},{self.title},{self.author},{self.is_loaned}"
    
#     def is_loaned(self):
#         return self.is_loaned
    
#     def borrow(self):
#         self.is_loaned = True

# class Library:
#     def __init__(self, books, filename):
#         self.books = books
#         self.filename = filename
    
#     def load_books(self):
#         try:
#             with open(self.filename, "r") as file:
#                 for line in file:
#                     attrs = line.strip("\n").split(",")
#                     book = Book(attrs[0], attrs[1], attrs[2], attrs[3] == "True")
#                     self.books.append(book)

#         except FileNotFoundError:
#             self.books = []

#     def find_book(self,book_id):
#         for book in self.books:
#             if book.id == book_id:
#                 return book
#         return None
            
#     def borrow_book(self, book_id):
#         book = self.find_book(book_id)
#         if book is None:
#             return "Error: Book not found"

#         elif book.is_loaned():
#             return "Book is already in Loaned."
        
#         else:
#             book.borrow()
#             self.save_books()
#             return (f" You have sucessfully borrowed {book.get_title()}")
    
#     def save_books(self):
#         with open(self.filename, "w") as f:
#             for book in self.books:
#                 f.write(str(book) + "\n")

# def main():
#     library = Library("books.txt")
#     inp = input("Enter book ID to borrow")
#     msg = library.borrow_book(inp)
#     print(msg)

def greet(name):
    return "Hello, " + name

msg = greet("Bob")
print(msg)

st = {"hello": 123, "jel": 25, "mama": 25}

new_d = {}

for key, value in st.items():
    if value not in new_d:
        new_d[value] = [key]
    else:
        new_d[value].append(key)

print(new_d)

dic1 = {"a": 1, "b": 3, "c": 4}
dic2 = {"b": 3, "c": 1, "d": 3}

new_dict = {}

for key1, value1 in dic1.items():
    if key1 in dic2:
        new_dict[key1] = value1 + dic2[key1]
    else:
        new_dict[key1] = value1

for key2, value2 in dic2.items():
    if key2 in dic1:
        new_dict[key2] = value2 + dic1[key2]
    else:
        new_dict[key2] = value2

# print(new_dict)

words = ["apple", "banana", "cherry"]
new_dic = {}
vowels = "aeiouyAEIOUY"
new_count = []
for word in words:
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
            new_dic[word] = count 


# print(new_dic)

grades = {
    "alice": [85, 90, 88],
    "bob": [78, 81, 86],
    "Charlie": [92, 87, 85]
}

for student, value in grades.items():
    new_list = []
    for item in value:
            new_list.append(item)
    size = len(new_list)
    total = sum(new_list)
    grades[student] = round(total / size)

print(grades)   

s, k = input().split()

for key, values in grades.items():
      if key == s:
        grades[key].append(int(k))

print(grades)

# class  Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


#     def __str__(self):
#         return f"The dog's name is  {self.name} and age is {self.age}"


#     def bark(self):
#         return "WOOOF"

# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def __str__(self):
#         return f"The name of the person is{self.name} and the age of the person is {self.age} "

# class Student(Person):
#     def __init__(self, name, age, student_id, grades ):
#         super().__init__(name, age)
#         self.student_id = student_id
#         self.grades = grades
    
#     def __str__(self):
#         return f"The name of the student is {self.name} and the age of the person is {self.age} and {self.student_id},  {self.grades} "


# class Vehicle:
#     def __init__(self, id, brand, is_rented = False):
#         self.id = id 
#         self.brand = brand
#         self.is_rented = is_rented

#     def __str__(self):
#         return f"{self.id}, {self.brand}, {self.is_rented}"

# class RentalService:
#     def __init__(self, vehicles):
#         self.vehicles = vehicles

#     def add_vehicle(self, vehicle):
#         self.vehicle = vehicle
#         self.vehicles.append(vehicle)

#     def find_vehicle(self, id):
#         self.id = id
#         for car in self.vehicles:
#             if id == car.id:
#                 return car
#         return None

#     def rent_vehicle(self, id):
#         self.id = id
#         for car in self.vehicles:
#             if id == car.id and car.is_rented == True:
#                 return f"Vehicle is already rented"
#             elif id != car.id:
#                 return f"Vehicle not found"
#             else:
#                 car.is_rented = True
#                 return f"You have rented the car"

# car1 = Vehicle(5, "toyota", False)

# rental = RentalService([car1])

# print(rental.find_vehicle(id = 5))
# print(rental.rent_vehicle(id = 5))
# print(rental.rent_vehicle(id = 5))

inp = input().split()
a_dict = {}

for word in inp:
    if word in a_dict:
        a_dict[word] += 1
    else:
        a_dict[word] = 1

print(a_dict)

n, k =  map(int, input().split())
a_set = set()

for _ in range(n):
    x = int(input())
    a_set.add(x)
    
print(len(a_set))

