from infi.systray import SysTrayIcon
from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection
import re, time, os, webbrowser, sys

rssi = None

def scrape():
    trying = True
    while trying is True:
        try:
            connection = Connection('http://192.168.8.1/')  #Router IP
            client = Client(connection)
            dicto = client.device.signal()
            global rs
            rssi = dicto["rssi"]
            r= re.findall(r'\d+', rssi)[0]
            rs = int(r)
            trying = False
            return rs
        except:
            pass

def open_router(systray):
    webbrowser.open('http://192.168.8.1/') #Router IP
def on_quit_callback(systray):
    os._exit(1)

def status():
    menu_options = (("Open router host", None, open_router),)
    systray = SysTrayIcon("C://Program Files//Router Tray//zero.ico", "Huawei signal", menu_options, on_quit=on_quit_callback)
    systray.start()
    while True:
        rs = scrape()
        print(rs)
        if rs <= 72:
            systray.update(icon="C://Program Files//Router Tray//five.ico")
            systray.update(hover_text= "-"+ str(rs) +"dB")
            time.sleep(3)
        if 73 <= rs <= 79:
            systray.update(icon="C://Program Files//Router Tray//four.ico")
            systray.update(hover_text= "-"+ str(rs) +"dB")
            time.sleep(3)
        if 80 <= rs <= 84:
            systray.update(icon="C://Program Files//Router Tray//three.ico")
            systray.update(hover_text= "-"+ str(rs) +"dB")
            time.sleep(3)
        if 85 <= rs <= 95:
            systray.update(icon="C://Program Files//Router Tray//two.ico")
            systray.update(hover_text= "-"+ str(rs) +"dB")
            time.sleep(3)
        if rs >= 95:
            systray.update(icon="C://Program Files//Router Tray//one.ico")
            systray.update(hover_text= "-"+ str(rs) +"dB")
            time.sleep(3)


if __name__ == "__main__":
    status()
