import base64

FILE_NAME = "passwords.txt"


# ----------- ENCRYPT PASSWORD -----------
def encrypt_password(password):
    encoded_bytes = base64.b64encode(password.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


# ----------- DECRYPT PASSWORD -----------
def decrypt_password(encoded_password):
    decoded_bytes = base64.b64decode(encoded_password.encode("utf-8"))
    return decoded_bytes.decode("utf-8")


mode = input(
    "Would you like to add a new password or get an existing password? (add/get): "
).lower()


# ---------------- ADD PASSWORD ----------------
if mode == "add":
    name = input("Enter the name for the password (e.g., email, facebook): ")
    pwd_to_store = input("Enter the password to store: ")

    encrypted_pwd = encrypt_password(pwd_to_store)

    with open(FILE_NAME, "a") as file:
        file.write(f"{name}|{encrypted_pwd}\n")

    print(f"Password for '{name}' added securely 🔐")


# ---------------- GET PASSWORD ----------------
elif mode == "get":
    name = input("Enter the name for the password you want to retrieve: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                stored_name, stored_pwd = line.strip().split("|")

                if stored_name == name:
                    decrypted_pwd = decrypt_password(stored_pwd)
                    print(f"The password for '{name}' is: {decrypted_pwd}")
                    found = True
                    break

        if not found:
            print(f"No password found for '{name}'.")

    except FileNotFoundError:
        print("No password file found. Please add a password first.")


# ---------------- INVALID MODE ----------------
else:
    print("Invalid mode selected. Please choose 'add' or 'get'.")
