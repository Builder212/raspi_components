from tkinter import *
import MainDHT as dht

DHT = dht.DHT(11)
hum, temp = DHT.read_dht()

root = Tk()
var = StringVar()
label = Label(root, textvariable = var)
label.pack()
var.set("Temperature: %d\nHumidity %d" %(temp, hum))

def var_update():
    hum, temp = DHT.read_dht()
    var.set("Temperature: %d\nHumidity %d" %(temp, hum))

B = Button(root, text = "Update", command = var_update)
B.pack()

root.mainloop()
