# Parse through the portions of an email address
# Name: Cassiddy Ginoza
# Date: Feb. 3, 2026

#Method 1: Using split() to separate username and domain
email = input("Enter your email address: ")

parts = email.split("@")
#splits string into two on the @ sign
username = parts[0]
domain = parts[1]

print("Username: ", username)
print("Domain Full: ", domain)

#Method 2: Using index() and slicing
at_symbol_index = email.index("@")
username_manual = email[:at_symbol_index]
domain_manual = email[at_symbol_index + 1 :]
# + 1 because we don't want to include the @ sign

print("Username (manual): ", username_manual)
print("Domain Full (manual): ", domain_manual)