import requests
import replit

def check_url(urls):
  urls = urls.split(",")
  domains = [".com", "co.kr", ".net"]
  for url in urls:
    url = url.strip()
    url = url.lower()
    if not any(domain in url for domain in domains):
      return print(url + " is not valid.")
    if "http://" not in url:
      url = "http://" + url
    
    try:
      response = requests.get(url)
      status_code = response.status_code
      if status_code == 200:
        print(url + " is up!")
      else:
        print(url + "is down!")
    except:
      print(url + " is error!")

def restart_message():
  while True:
    print("Do you want to start over? y/n ")
    answer = input()
    if answer == "y" or answer == "n":
      break
    else:
      print("That's not a valid answer.")

  if answer == "y":
    clear()
  else:
    print("k.bye")  

def send_message():
  urls = input()
  check_url(urls)
  restart_message()

def start():
  print("Welcome to IsItDown.py")  
  print("Please write a URL or URLs you want to check. (separated by comma)")
  send_message()

def clear():
  replit.clear()
  start()

start()  