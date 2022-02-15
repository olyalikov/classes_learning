import sqlite3


class Database:
    """ класс базы даннх"""

    @classmethod
    def inner_classes_list(cls):
        results = []
        for attrname in dir(cls):
            obj = getattr(cls, attrname)
            if isinstance(obj, type) and issubclass(obj, Database.Table) and obj != Database.Table:
                results.append(obj)
        return results

    @classmethod
    def commit(cls):
        """ метод для создания таблиц
                    и
          добавления колонок"""
        cls.tables = cls.inner_classes_list()
        cls.con = sqlite3.connect(f'{cls.__name__}.db')
        cls.cur = cls.con.cursor()
        for table in cls.tables:
            if table.status:
                try:
                    cls.cur.execute(f'CREATE TABLE {table.__name__}(ID INTEGER PRIMARY KEY)')
                    print(f"TABLE {table.__name__} succsesfully created!")
                    table.status = False
                except:
                    pass

            for arg in table.__dict__.values():

                if isinstance(arg, type):
                    if arg.status:
                        if arg.__name__ not in table.args:
                            arg.status = False
                            table.args.append(arg.__name__)
                            try:
                                if issubclass(arg, Database.Table.Reference):

                                    cls.cur.execute(
                                        f"""ALTER TABLE {table.__name__} ADD COLUMN {arg.__name__} INTEGER 
                                        REFERENCES {arg.reference} (ID) ON DELETE CASCADE ON UPDATE CASCADE""")
                                    print(
                                        f"COLUMN {arg.__name__} is {arg.type} to {arg.reff} succsesfully add to TABLE {table.__name__}")

                                else:
                                    cls.cur.execute(
                                        f"ALTER TABLE {table.__name__} ADD COLUMN {arg.__name__} {arg.type}")
                                    print(
                                        f"COLUMN {arg.__name__} of {arg.type} succsesfully add to TABLE {table.__name__}")
                            except:
                                pass

    @classmethod
    def add(cls, table, args):
        """ метод для записи данны в таблицу """
        try:
            pk = list(cls.cur.execute(f"SELECT ID FROM {table.__name__} ORDER BY ID"))[-1][0] + 1
        except:
            pk = 0
        try:
            args = (pk,) + args
            if issubclass(table, Database.Table.Reference):
                pass
            else:
                cls.cur.execute(f"INSERT INTO {table.__name__} VALUES {str(args)}")
                for index, arg in enumerate(table.args):
                    print(f"Parametor {arg}: {args[index]} added to {table.__name__}")
        except:
            pass
        cls.con.commit()

    @classmethod
    def update(cls, table, id, arg, value):
        """ метод для обновления записи данны в таблицу """

        if issubclass(table, Database.Table.Reference):
            pass
        else:
            cls.cur.execute(f"UPDATE {table.__name__} SET {arg} = ? WHERE ID = {id}", (value,))
            print(f"Parametor {arg} for id = {id} updated to {value} in {table.__name__}")
        cls.con.commit()

    @classmethod
    def get(cls, table):
        result = []
        for row in cls.cur.execute(f"SELECT * FROM {table.__name__} ORDER BY ID"):
            obj = {}
            for index, arg in enumerate(table.args):
                obj[arg] = row[index]
            result.append(obj)
        return result

    class Table:
        """ класс таблицы """
        status = True

        class Integer:
            """ класс типа целочисленных данных """
            status = True
            type = "Integer"

        class Text:
            """ класс типа текст """
            status = True
            type = "Text"

        class Real:
            """ класс типа нецелочисленных данных """
            status = True
            type = "Real"

        class Reference:
            """ класс связи нескольких таблиц """
            status = True
            type = "Reference"
