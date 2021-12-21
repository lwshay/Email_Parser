import xtarfile as tarfile
import pandas
import email
from email import policy

#define column heaaders
cvsColumns = ['To', 'From', 'Date', 'Subject', 'Message-ID']
        
data = []
messages = tarfile.open('assets/sampleEmails.tar.gz', 'r', encoding='utf-8')
for m in messages.getmembers():
    try: 
        f = messages.extractfile(m)
    except KeyError:
        print('ERROR: Could not extract file.'.format(m))
    else:
        if f is not None:
            #read email
            msg = email.message_from_bytes(f.read(), policy=policy.SMTP)

            #save email paramers
            em = {}
            em['To'] = msg["To"]
            em['From'] = msg["From"]
            em['Date'] = msg["Date"]
            em['Subject'] = msg["Subject"]
            em['Message-ID'] = msg["Message-ID"]
            data.append(em)

try: 
    #save csv
    df = pandas.DataFrame(data, columns = cvsColumns)
    df.to_csv('parsed_email.csv', index=False, header=True)
    print("File Saved")
except KeyError:
    print('ERROR: Data could not be saves.')


