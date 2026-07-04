class MyHashMap:

    def __init__(self):
        self.storage = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.storage[key] = value

    def get(self, key: int) -> int:
        return self.storage[key]

    def remove(self, key: int) -> None:
        self.storage[key] = -1