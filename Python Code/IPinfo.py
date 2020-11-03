import json
import requests
import base64, PIL, urllib
from PIL import ImageTk
from urllib import *
from tkinter import messagebox
from tkinter import *
import tkinter
master = tkinter.Tk()
master.resizable(0,0)
master.title("IP")
raw_data = urllib.request.urlopen("https://cdn.icon-icons.com/icons2/37/PNG/512/IPaddress_IP_3219.png").read()
b64_data = base64.encodestring(raw_data)
image = PhotoImage(data=b64_data)
master.tk.call('wm', 'iconphoto', master._w, image)
api = "http://ip-api.com/json/"
def ipdata():
    ipaddr = ((ip.get()))
    addr = api + ipaddr
    apidata = requests.get(addr)
    data = apidata.text
    y = json.loads(data)
    lines = ["IP: " + y["query"], "Country: " + y["country"], "Country Code: " + y["countryCode"], "Region: " + y["region"], "Region Name: " + y["regionName"], "City: " + y["city"], "Zip-Code: " + y["zip"], "Timezone: " + y["timezone"], "ISP: " + y["isp"], "Org:" + y["org"], "AS: " + y["as"], "IPinfo by eliakessler.ch"]
    tkinter.messagebox.showinfo("IPinfo: " + ((ip.get())), "\n".join(lines))
Button(master, text='Get IP Info', command=ipdata).grid(row=8, column=1, sticky=W, pady=4)
Label(master, text="IP-Adress: ").grid(row=4, column=0)
ip = Entry(master)
ip.grid(row=4, column=1)
master.mainloop()