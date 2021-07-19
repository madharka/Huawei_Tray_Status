# Huawei_Tray_Status

Python script that creates a Windows tray icon for signal strength tracking. 
It uses infi.systray library for tray icon display and huawei_lte_api library to get the frequency information from the Huawei router.

It only tracks router's RSSI frequency and displays tray icons (signal strength bars) according to the RSSI dB value.
These values are not official, I set them up myself. Therefore, it is not 100% accurate.

By right-clicking on the tray icon you can go to the router's home page or quit the script.

To make this script as an executable file I used pyinstaller.
"pyinstaller --hidden-import pkg_resources --hidden-import infi.systray --onefile --noconsole track_router.py"

Location of the tray icons is set to "C://Program Files//Router Tray//"
