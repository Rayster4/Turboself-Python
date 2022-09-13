from turboself.clients import turboself
import os
import stdiomask

os.system("cls")

Client = turboself(stdiomask.getpass("Enter your email : ", mask="*"), stdiomask.getpass("Enter your password : ",mask="*"))
Client.connect_()
price, each, left = Client.CrediterCompte()
print(f"You have in your account : {price}€")
print(f"A dinner cost : {each}€")
print(f"So you can buy at least : {left} dinner.")