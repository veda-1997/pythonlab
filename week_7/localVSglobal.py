counter = 0       # Global variable

def show_local():
    counter = 10  # Local variable
    print("Local counter:", counter)

show_local()

print("Global counter:", counter)
#Local counter: 10
#Global counter: 0
