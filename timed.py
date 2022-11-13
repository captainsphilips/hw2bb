import time

# Decorator
def calculate_time(func):
    
    def inner_time():
        begin = time.time()
        func()
        end = time.time()
        print("Total time ",end - begin)
    return inner_time
  
@calculate_time
def on_time():
    print('time!')
on_time()