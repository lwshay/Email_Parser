import xtarfile as tarfile
import email
import pandas


cvsColumns = ['To', 'From', 'Date', 'Subject', 'Message-ID']
        
data = []
messages = tarfile.open("./assets/sampleEmails.tar.gz", "r:gz", encoding='utf-8')
count = 0
for m in messages.getmembers():
     f = messages.extractfile(m)
     if f is not None:
         count = count + 1
         content = f.read()
         print(type(content))
         msg = email.message_from_bytes(content)
         print("From: ", msg["From"])
         print("To: ", msg["To"])
         print("Subject: ", msg["subject"])
         print("Date: ", msg["Date"])
         print("Message-ID: ", msg["Message-ID"])
         em = {}
         em['To'] = msg["To"]
         em['From'] = msg["From"]
         em['Date'] = msg["Date"]
         em['Subject'] = msg["Subject"]
         em['Message-ID'] = msg["Message-ID"]
         data.append(em)
         #print(msg.date)
         #print(content)
         #break
print(count)
df = pandas.DataFrame(data, columns = cvsColumns)
df.to_csv('parsed_email.csv', index=False, header=True)

