#get user email address

email = input("Enter your email addess: ").strip()

#slice out user name

username = email[:email.index("@")]

#slice domain name

domain = email[email.index("@") + 1:]

#format message

output = "Your username is {} and your domain is {}".format(username,domain)

#display output message
print(output)
