import logging


logging.basicConfig(filename='error.txt', filemode='a',
                    format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level='DEBUG')


class List:

    def sort(self, data):
        try:
            for i in range(len(data)):
                for j in range(i+1, len(data)):
                    if data[i] > data[j]:
                        data[i], data[j] = data[j], data[i]
            logging.info(f'Value sorted.')
        except Exception as e:
            logging.error(str(e))

    def append(self, data, value):
        try:
            if type(value) is list or type(value) is dict or type(value) is set:
                data = data + [[value]]
                logging.info(f'List appended')
            if type(value) is tuple:
                data = data + ((value))
            else:
                data = data + [value]
        except Exception as e:
            logging.error(str(e))

    def extend(self, data, value):
        try:
            data = data + [value]
            logging.info(f'List Extended {data}')
        except Exception as e:
            logging.error(str(e))

    def index(self, data, value):
        try:
            for index, val in enumerate(data):
                if val == value:
                    logging.info(f'Value {value} found in {index} index')
                    return index
        except Exception as e:
            logging.error(str(e))

    def max(self, data):
        try:
            max_val = self.sort(data)[-1]
            logging.info(f'Max value {data} is {max_val}')
            return max_val
        except Exception as e:
            logging.error(str(e))

    def min(self, data):
        try:
            min_val = self.sort(data)[0]
            logging.info(f'Min value {data} is {min_val}')
            return min_val
        except Exception as e:
            logging.error(str(e))

    def len(self, data):
        try:
            lenght = 0
            for i in data:
                lenght += 1
            logging.info(f'Length of {data} is {lenght}')
            return lenght
        except Exception as e:
            logging.error(str(e))

    def insert(self, data, index, value):
        try:
            data[index:index] = [value]
            logging.info(f'Element {data} assigned in {index}')
        except Exception as e:
            logging.error(str(e))

    def count(self, data, value):
        try:
            if data:
                count = self.len([i for i in data if value == i])
                logging.info(f'Value {value} found {count} times')
                return count
            else:
                logging.warning('List is empty')
        except Exception as e:
            logging.error(str(e))

    def pop(self, data):
        try:
            if data:
                logging.info(f'Element {data[-1]} is poped')
                del data[-1]
        except Exception as e:
            logging.error(str(e))

    def remove(self, data, value):
        try:
            for i in data:
                if i == value:
                    logging.info(f'Element {i} is removed.')
                    del i
        except Exception as e:
            logging.error(str(e))

    def reverse(self, data):
        try:
            if type(data) is list or type(data) is tuple:
                rev = data[::-1]
                logging.info(f'Reverser value of {data} is {rev}')
                return rev
            else:
                logging.warning("Data is not a list or tuple.")
        except Exception as e:
            logging.error(str(e))


class Tuple:

    def max(self, data):
        try:
            max_val = self.sort(data)[-1]
            logging.info(f'Max value of {data} is {max_val}')
            return max_val
        except Exception as e:
            logging.error(str(e))

    def min(self, data):
        try:
            min_val = self.sort(data)[0]
            logging.info(f'Min value of {data} is {min_val}')
            return min_val
        except Exception as e:
            logging.error(str(e))

    def len(self, data):
        try:
            lenght = 0
            for i in data:
                lenght += 1
            logging.info(f'Length of {data} is {lenght}')
            return lenght
        except Exception as e:
            logging.error(str(e))


class Dict:

    def clear(self, data):
        data = {}
        logging.info(f"Data is cleared")
        return data

    def get(self, data, key):
        for k in data.keys():
            if k == key:
                logging.info(f"Key {k} returned")
                return k
            else:
                logging.warning(f"Key {k} not found in {data}")

    def update(self, data, values):
        key = list(values.keys())[0]
        value = list(values.values())[0]
        for i in data.keys():
            if i == key:
                data[key] = value
                logging.info(f"Element {data[i]} assigned to {data}")
            else:
                logging.warning(f"Element {data[i]} not found in {data}")

    def copy(self, data):
        logging.info(f"Element {data} is copied.")
        return data

    def setdefault(self, data, values):
        key = list(values.keys())[0]
        value = list(values.values())[0]
        for i in data.keys():
            if i == key:
                data[key] = value
                logging.info("Default value is fixed")
            else:
                logging.warning(f"Element {data[i]} not found in {data}")

    def popitem(self, data):
        count = 0
        for i in data.keys():
            if count == len(data) - 1:
                logging.info(f"Element {data[i]} deleted from {data}")
                del data[i]
                break
            else:
                logging.warning(f"Element {data[i]} not found in {data}")

    def pop(self, data, values):
        key = list(values.keys())[0]
        for i in data.keys():
            if i == key:
                logging.info(f"Element {data[i]} deleted from {data}")
                del data[i]
            else:
                logging.warning(f"Element {data[i]} not found in {data}")

    def pop(self, data, key, value):
        for k, v in data.items():
            if k == key and v == value:
                logging.info(f"Element {data[k]} deleted from {data}")
                del data[k]
            else:
                logging.warning(f"Element {data[k]} not found in {data}")


class Set:

    def clear(self, data):
        data = {}

    def add(self, data, value):
        if type(data) is not list or type(data) is not dict or type(data) is not tuple or type(data) is not str:
            list_data = list(data) + [data]
            return set(list_data)

    def difference(self, a, b):
        return a - b

    def copy(self, data):
        return data
