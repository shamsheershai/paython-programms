import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("shamsheershaik642@gmail.com" ,"shamsheer@123")
message = "hi hello"
server.sendmail("sriharsha8811@gmail.com","sriharsha8811@gmail.com",message)
print("sss")
server.quit()
