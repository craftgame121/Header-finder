import requests
import time
import os

#with open("art.txt.txt", "r") as f:
    #lines = f.readline()
    #for i in lines:
        #print(i)


url = input("Enter your url: ")

print("---------------------------------------------------")

rs = requests.get("https://"+url)

print(rs.headers)

print("---------------------------------------------------")

time.sleep(1.6)
close = input("are you sure close it? (y/n) : ")

if close == "y":
    for i in range(1,11):
        print(i)
    time.sleep(0.5)
    #os.close()

elif close == "n":
    os.system('cls')
    link = input("Enter your url: ")
    print("---------------------------------------------------")
    ris = requests.get("https://"+link)
    print(ris.headers)
    print("---------------------------------------------------")

else:
    print("this is false")
    
    
    

#logo = open("art.txt.txt", "r").readlines
#print(logo)

print("Discord:craftgame#2022\ngithub:craftgame121")
print(input("enter a key"))
for i in range(1,11):
    print(i)
time.sleep(0.4)
os.close()






#if __name__ == "__main__":
    #lock = thread.allocate_lock()
    #thread.start_new_thread(myfunction, ("Thread #: 1", 2, lock))
    #thread.start_new_thread(myfunction, ("Thread #: 2", 2, lock))
#with open('head.txt', 'w') as f:
    #for i in apps:
        #f.write(i + "\n")

