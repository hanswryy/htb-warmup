# Phreaky

This is quite easy but took a long time.

Today's challenge involve some network sniffing into .pcap file using wireshark. <br>
![image](https://github.com/user-attachments/assets/79627ee8-6fc8-40c8-9633-81baa7896997)

Now I scroll the logs until found some sus traffic.<br>
![image](https://github.com/user-attachments/assets/b8ad9281-36e9-400b-b69f-d539c044ece3)

Some SMTP (Simple Mail Transfer Protocol) involving the title of this challenge phreaks. Particularly on this.<br>
![image](https://github.com/user-attachments/assets/d4d52dc0-86c7-4ecd-932a-9dd5117c49df)

Looking into the TCP Stream we see it's an email from thepreaks to thetalent. <br>
![image](https://github.com/user-attachments/assets/3d10865b-b431-43e5-9ea9-9034255ddc2c)

It said that this email attached a zip file with provided password. The file is encoded in base64.<br>
![image](https://github.com/user-attachments/assets/3745e558-1657-4fc4-870f-0f219d8690a3)

So then we just need to decode it and write it into a .zip file.<br>
```
import base64

# Read the Base64 encoded data from your file
with open("encoded_data.txt", "r") as file:
    base64_data = file.read()

# Decode and save as zip
with open("decoded.zip", "wb") as zip_file:
    zip_file.write(base64.b64decode(base64_data))
```

Inside it was a pdf file, but there is a .part1 extension.<br>
![image](https://github.com/user-attachments/assets/57e4def7-d8cf-413a-817c-b8d7db34aa94)

Soon I know there are actually 15 part of this file. So I need to get the base64, decode it, use the password to extract, and just do for another 14 times :).

Long story short I got all the 15 parts. Now I need to combine it.<br>
![image](https://github.com/user-attachments/assets/ce39aed6-814c-4f21-8dc5-3cfe1adc9f10)

Now what I need to do is to just copy the content of each part and write it to one main file to be opened. Don't forget to save it as .pdf as it originally intended.<br>
```
# combine all pdf part in attachment/phreaks_plan into one file
import os

# open the file
with open("attachment/phreaks_plan_main", "wb") as file:
    # loop through all the parts
    for i in range(1, 16):
        # open the part file
        with open(f"attachment/phreaks_plan/phreaks_plan.pdf.part{i}", "rb") as part_file:
            # read the part file
            part = part_file.read()
            # write the part file to the main file
            file.write(part)

# write file to pdf
os.rename("attachment/phreaks_plan_main", "attachment/phreaks_plan.pdf")
```

Open the file and see this wtf.<br>
![image](https://github.com/user-attachments/assets/a823bcd2-40a7-49e9-ba12-ac24a95f221f)

Oh the flag is under.<br>
![image](https://github.com/user-attachments/assets/5e6a94d3-7327-47d9-a7c5-7f96f4c7210d)

Flag: HTB{Th3Phr3aksReadyT0Att4ck}

Lesson learnt: 
- Look for some sus traffic, maybe search for some particular string from the challenge hint.

