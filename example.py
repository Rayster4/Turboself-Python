from turboself.clients import turboself
import os
import stdiomask

os.system("cls")
client_username = stdiomask.getpass("Enter your email : ", mask="*")
client_password = stdiomask.getpass("Enter your password : ",mask="*")
Client = turboself(client_username,client_password)
Client.connect_()
price, each, left = Client.CrediterCompte()
print(f"You have in your account : {price}€")
print(f"A dinner cost : {each}€")
print(f"So you can buy at least : {left} dinner.")