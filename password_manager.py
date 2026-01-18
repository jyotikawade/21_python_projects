mode = input("Would you like to add a new password or get an existing password? (add/get): ").lower()

FILE_NAME = "passwords.txt"

# ---------------- ADD PASSWORD ----------------
if mode == "add":
    name = input("Enter the name for the password (e.g., email, facebook): ")
    pwd_to_store = input("Enter the password to store: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name}|{pwd_to_store}\n")

    print(f"Password for '{name}' added successfully.")

# ---------------- GET PASSWORD ----------------
elif mode == "get":
    name = input("Enter the name for the password you want to retrieve: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                stored_name, stored_pwd = line.strip().split("|")
                if stored_name == name:
                    print(f"The password for '{name}' is: {stored_pwd}")
                    found = True
                    break

        if not found:
            print(f"No password found for '{name}'.")

    except FileNotFoundError:
        print("No password file found. Please add a password first.")

# ---------------- INVALID MODE ----------------
else:
    print("Invalid mode selected. Please choose 'add' or 'get'.")
