import time
from plyer import notification

if __name__ == "__main__":
	while True:
     notification.notify(  
     title = "Please change Your mood",
     message ="10 min break refresh your mood After work energtic", 
     app_icon = "C:\Users\HP\Desktop\js\apps\icon.ico",
     timeout=10
     	)
     time.sleep(60*60)