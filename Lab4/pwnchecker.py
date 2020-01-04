import hashlib as hl
import requests
import sys

def main():
    password = sys.argv[1] #pobranie hasła z konsoli
    sha1 = hl.sha1(password.encode('utf-8')).hexdigest().upper() #zamiaana hasła na zapis heksadecymalny w kodowaniu utf-8, zamienia małe litery na wielkie i hashuje algorytmem sha1

    r=requests.get("https://api.pwnedpasswords.com/range/"+sha1[0:5]) #pobiera wszystkie hasła, które zaczynają się od takich samych pięciu znaków sha
    print (r.status_code) # wypisuje kod odpowiedzi dla request
    response = r.content.decode().split("\r\n") 
    success = False
    for i in response: # dla każdego sha zwroceonego z requestu
        if sha1[5:] not in i: # sprawdza czy jest identyczne z sha naszego hasła
           continue # sprawdz kolejny
        else:
            success=True #znaleziono takie samo hasło w bazie
            print(i)  # wypisz sha tego hasła
    if not success:
        print("Password not found") # wypisuje informację o tym, że nie ma takiego samego hasła w bazie

if __name__ == "__main__":
    main() # uruchamia główną metodę
