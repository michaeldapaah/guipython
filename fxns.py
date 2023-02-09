from datetime import datetime

def print_time(taskname):
    print(taskname)
    print(datetime.now())
    print()

firstname = 'susan'
print_time()

for x in range(0,10):
    print(x)
print_time()