
# Simple Program that sends a set of random integers within the range of 1-49 as your lucky lottery numbers of the week.
import random, smtplib, getpass

for i in range(7):
    lotterynums = random.sample(range(49), 7)

# Parameters for the mail server and initiating a security function for your password
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
password = getpass.getpass("Password: ")
server.login("YOUR EMAIL ADDRESS", password)

# Message Content, From and To emails
msg = "Here are this weeks Lucky Lottery Numbers -  " + str(lotterynums)
server.sendmail("YOUR EMAIL ADDRESS", "RECIEVING EMAIL HERE", msg)
server.quit()
print("Lucky Lottery Numbers have been sent!")