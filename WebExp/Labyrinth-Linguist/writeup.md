# Labyrinth Linguist

yang ini rada ngecheat dikit juga hehe

Tried exploring the sources, netword, element and got nothing special.<br>
Now I tried to go to the project folder that provided by htb.<br>

Parameter + Template = SSTI (Server-Side Template Injection)<br>
![image](https://github.com/user-attachments/assets/0a8ed43b-c5c3-4af5-8628-f31f7885b981)

Google some SSTI payload.<br>
![image](https://github.com/user-attachments/assets/13001688-4ea6-4738-a565-30deb0538a46)

Got stuck trying various payload. But I'm too dumb to try find some clue in the code, which is to try to find what kind of template-engine it used. Here they used velocity.<br>
![image](https://github.com/user-attachments/assets/3a4ffbb1-7ee8-453c-ae45-87b8fe9bd18a)
![image](https://github.com/user-attachments/assets/2aa54843-9ee4-4252-a474-f0cf6247327d)

Using burp so that we can encode the payload (Block the text and then press CTRL+U).<br>
![image](https://github.com/user-attachments/assets/0cba41d7-70ef-41c7-8838-4c30a3c0f1cd)

Jackpot.png<br>
![image](https://github.com/user-attachments/assets/425a3f5a-9f61-4997-b968-ac893c50d737)

Now we just need to get the flag which is up above this file.<br>
![image](https://github.com/user-attachments/assets/cb0f1bef-e53c-464e-9703-b9612a9a60b2)

Change the exec code to cat flag.txt <br>
![image](https://github.com/user-attachments/assets/3b4cb50a-1b3d-4d95-97fb-be3cf5398967)

![image](https://github.com/user-attachments/assets/7efd546a-a15a-432d-8b9b-3c254fc15a3d)

lesson learnt:<br>
- Don't give up searching some clue in the code.
- Don't afraid to google some payload that might work.
- Don't forget to use neccesery tools you might find useful like Burp.
