class MyHashSet:

    def __init__(self):
        # This creates our massive checklist of 1,000,001 slots, all starting as False
        self.arr = [False] * 1000001

    def add(self, key: int) -> None:
        # To add a key, we just flip its slot to True
        self.arr[key] = True

    def remove(self, key: int) -> None:
        # To remove a key, we flip its slot back to False
        self.arr[key] = False

    def contains(self, key: int) -> bool:
        # To check if it exists, we just look at that slot and return True or False
        return self.arr[key]