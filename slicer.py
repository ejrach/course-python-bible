# get the user email address
email = input("What is your email address: ").strip()

# slice out user name
user = email[:email.index("@")]

# slide domain name
domain = email[email.index("@") + 1:]

# format message
output = "Your user name is {} and your domain name is {}".format(user,domain)

# display output message
print(output)
