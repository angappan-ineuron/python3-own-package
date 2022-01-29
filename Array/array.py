import logging


class List:

    def __init__(self):
        logging.basicConfig(filename='error.logs', filemode='a',
                            format='%(asctime)s %(levelname)s-%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    def sort(self, data):
        try:
            for i in range(len(data)):
                for j in range(i+1, len(data)):
                    if data[i] > data[j]:
                        data[i], data[j] = data[j], data[i]
        except Exception as e:
            self.logging.error(e)

    def append(self, data, value):
        try:
            if type(value) is list or type(value) is dict or type(value) is set:
                data = data + [[value]]
            if type(value) is tuple:
                data = data + ((value))
            else:
                data = data + [value]
        except Exception as e:
            self.logging.error(e)

    def extend(self, data, value):
        try:
            data = data + [value]
        except Exception as e:
            self.logging.error(e)

    def index(self, data, value):
        try:
            for index, val in enumerate(data):
                if val == value:
                    return index
        except Exception as e:
            self.logging.error(e)

    def max(self, data):
        try:
            return self.sort(data)[-1]
        except Exception as e:
            self.logging.error(e)

    def min(self, data):
        try:
            return self.sort(data)[0]
        except Exception as e:
            self.logging.error(e)

    def len(self, data):
        try:
            lenght = 0
            for i in data:
                lenght += 1
            return lenght
        except Exception as e:
            self.logging.error(e)

    def insert(self, data, index, value):
        try:
            data[index:index] = [value]
        except Exception as e:
            self.logging.error(e)

    def count(self, data, value):
        try:
            count = self.len([i for i in data if value == i])
            return count
        except Exception as e:
            self.logging.error(e)

    def pop(self, data):
        try:
            del data[-1]
        except Exception as e:
            self.logging.error(e)

    def remove(self, data, value):
        try:
            for i in data:
                if i == value:
                    del i
        except Exception as e:
            self.logging.error(e)

    def reverse(self, data):
        try:
            return data[::-1]
        except Exception as e:
            self.logging.error(e)


class Tuple:
    def __init__(self):
        logging.basicConfig(filename='error.logs', filemode='a',
                            format='%(asctime)s %(levelname)s-%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    def max(self, data):
        try:
            return self.sort(data)[-1]
        except Exception as e:
            self.logging.error(e)

    def min(self, data):
        try:
            return self.sort(data)[0]
        except Exception as e:
            self.logging.error(e)

    def len(self, data):
        try:
            lenght = 0
            for i in data:
                lenght += 1
            return lenght
        except Exception as e:
            self.logging.error(e)


class Dict:
    def __init__(self):
        logging.basicConfig(filename='error.logs', filemode='a',
                            format='%(asctime)s %(levelname)s-%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    def clear(self, data):
        data = {}
        return data

    def get(self, data, key):
        for k in data.keys():
            if k == key:
                return k

    def update(self, data, values):
        key = list(values.keys())[0]
        value = list(values.values())[0]
        for i in data.keys():
            if i == key:
                data[key] = value

    def copy(self, data):
        return data

    def setdefault(self, data, values):
        key = list(values.keys())[0]
        value = list(values.values())[0]
        for i in data.keys():
            if i == key:
                data[key] = value

    def popitem(self, data):
        count = 0
        for i in data.keys():
            if count == len(data) - 1:
                del data[i]
                break

    def pop(self, data, values):
        key = list(values.keys())[0]
        for i in data.keys():
            if i == key:
                del data[i]

    def pop(self, data, key, value):
        for k, v in data.items():
            if k == key and v == value:
                del data[k]


class Set:
    def __init__(self):
        logging.basicConfig(filename='error.logs', filemode='a',
                            format='%(asctime)s %(levelname)s-%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    def pop(self):
        return
