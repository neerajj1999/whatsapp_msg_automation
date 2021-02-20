import pywhatkit

phone_number = input("Enter the Reciver Number: ")
message = input("Enter the message you want to send: ")
print("Enter the Time to send the message: ")

Time_HRS=int(input("--Hour Time: "))
Time_MINTS = int(input("--Minute Time: "))

pywhatkit.sendwhatmsg(phone_number,message,Time_HRS,Time_MINTS)
