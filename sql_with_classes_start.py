from main import Database

"""
class MyDataBase(Database):
    con = None
    cur = None
    class Users(Database.Table):
        args = ['ID']
        class name(Database.Table.Text):
            pass
        class password(Database.Table.Text):
            pass
    class Posts(Database.Table):
        args = ['ID']
        class text(Database.Table.Text):
            pass
        class date(Database.Table.Text):
            pass
MyDataBase.commit()
MyDataBase.add(MyDataBase.Users, ('User', 'Password'))
MyDataBase.add(MyDataBase.Posts, ('New post', '18.01.2022'))
request = MyDataBase.get(MyDataBase.Users)
for obj in request:
    print(obj)
request = MyDataBase.get(MyDataBase.Posts)
for obj in request:
    print(obj)
print("-" * 12)
"""
class MyNewDataBase(Database):
    con = None
    cur = None

    class Users(Database.Table):
        args = ['ID']

        class name(Database.Table.Text):
            pass

        class password(Database.Table.Text):
            pass

    class Posts(Database.Table):
        args = ['ID']

        class text(Database.Table.Text):
            pass

        class date(Database.Table.Text):
            pass
        class image(Database.Table.Text):
            pass
        class user_id(Database.Table.Reference):
            reference = "Users"




MyNewDataBase.commit()
MyNewDataBase.add(MyNewDataBase.Users, ('User1', 'Password1'))
MyNewDataBase.add(MyNewDataBase.Posts, ('New post1', '20.01.2022', 0))
print("-" * 12)

request = MyNewDataBase.get(MyNewDataBase.Users)
for obj in request:
    print(obj)
request = MyNewDataBase.get(MyNewDataBase.Posts)
for obj in request:
    print(obj)
print("-" * 12)
"""
MyNewDataBase.update(MyNewDataBase.Users, id=0, arg='name', value='name')
print("-" * 12)
request = MyNewDataBase.get(MyNewDataBase.Users)
for obj in request:
    print(obj)
request = MyNewDataBase.get(MyNewDataBase.Posts)
for obj in request:
    print(obj)
print("-" * 12)
class BadBase(Database):
    con = None
    cur = None
    class students(Database.Table):
        args = ['ID']
        class name(Database.Table.Text):...
        class teacher(Database.Table.Text):...
        class lessons(Database.Table.Text):...
        class group_leader(Database.Table.Text):...
    class students_lessons(Database.Table):
        args = ['ID']
        class student_id(Database.Table.Integer): ...
        class lesson_id(Database.Table.Integer): ...
    class lessons(Database.Table):
        args = ['ID']
        class lesson(Database.Table.Integer): ...
BadBase.commit()
result = BadBase.get(BadBase.students)
for row in result:
    print(row)
result = BadBase.get(BadBase.lessons)
for row in result:
    print(row)
result = BadBase.get(BadBase.students_lessons)
for row in result:
    print(row)
"""
