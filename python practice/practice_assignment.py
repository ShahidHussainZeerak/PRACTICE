x=10
y=10
from pynput.keyboard import Key, Listener

def cordinate (x,y):
    
    def on_press(key):
        print("{0} press".format(key))
        if key==key.liftarrow():
         print(x=+1,
            y=10)
    def on_release(key):
        print("{0} release".format(key))
        if key==key.liftarrow():
            print(x=+1 ,y=10)
    with Listener(on_press=on_press, on_release=on_release)as  listener:
        listener.join()

print(cordinate(10,10))
