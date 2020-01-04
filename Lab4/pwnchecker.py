import hashlib as hl
import requests
import sys

def main():
    password = sys.argv[1]
    sha1 = hl.sha1(password.encode('utf-8')).hexdigest().upper()

    r=requests.get("https://api.pwnedpasswords.com/range/"+sha1[0:5])
    print (r.status_code)
    response = r.content.decode().split("\r\n")
    success = False
    for i in response:
        if sha1[5:] not in i:
           continue
        else:
            success=True
            print(i) 
    if not success:
        print("Password not found")

if __name__ == "__main__":
    main()
