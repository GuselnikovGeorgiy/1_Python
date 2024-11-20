class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self, obj):
        if obj.get_prev() is not None and obj.get_next() is not None:
            obj.get_prev().set_next(obj.get_next())
            obj.get_next().set_prev(obj.get_prev())
        elif obj.get_prev() is not None and obj.get_next() is None:
            obj.get_prev().set_next(None)
            self.tail = obj.get_prev()
        elif obj.get_prev() is None and obj.get_next() is not None:
            obj.get_next().set_prev(None)
            self.head = obj.get_next()
        elif obj.get_prev() is None and obj.get_next() is None:
            self.head = None
            self.tail = None

    def get_data(self):
        data = []
        obj = self.head
        while obj is not None:
            data.append(obj.get_data())
            obj = obj.get_next()
        return data


class ObjList:

    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def get_next(self):
        return self.__next

    def set_prev(self, obj):
        self.__prev = obj

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def __str__(self):
        return str(self.__data)

