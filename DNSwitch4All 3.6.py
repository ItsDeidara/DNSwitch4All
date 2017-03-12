import re
import requests

regex = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
    r'localhost|' #localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

redirect_url = input("Please enter the URL you want to redirect to: ").strip()
if regex.match(redirect_url):
    response = requests.post("http://107.170.190.128/configure.php", data={"redirect_url": redirect_url}).text
    if response == "1":
        print("Redirect successfully updated!")
    elif response == "0":
        print("Redirect update failed or same URL entered.")
else:
    print("Invalid redirect URL entered.")