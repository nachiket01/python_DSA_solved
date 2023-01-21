from typing import Dict


Dict= {"name":"kelly", "age":25,"salary":8000, "city":"New York"}
Dict["location"]=Dict["city"]
del(Dict["city"])
print(Dict)