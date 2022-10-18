class TimeMap:
    def __init__(self):
        self.store=dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[(key,timestamp)]=value
        

    def get(self, key: str, timestamp: int) -> str:
        temp=timestamp
        while temp>0:
            if (key,temp) in self.store:
                return self.store[(key,temp)]
            temp-=1
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
