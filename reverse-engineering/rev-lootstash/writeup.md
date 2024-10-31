# Rev-lootstash

very very easy.

wtf is this file.png<br>
![image](https://github.com/user-attachments/assets/e04af642-61b3-4c4f-9016-ffc192c27e81)

It's ELF, basically linux executable (.exe for linux).
Boot up ghidra, we boutta get a headache from variable name.<br>
![image](https://github.com/user-attachments/assets/fa01cd12-da38-4b05-875c-c28844e8607d)

First thing first check for some notable function in Symbol Tree. I think only main function that we need to look for.<br>
![image](https://github.com/user-attachments/assets/1f85c57d-1170-4b24-9d97-39a1ded1685d)

Lmao looks confusing right.<br>
![image](https://github.com/user-attachments/assets/213eff97-6978-4316-95ee-258c09d179aa)

Ask your buddy to rename the vars for you.<br>
![image](https://github.com/user-attachments/assets/fa7b7739-07bc-4f53-adcb-07867c337d74)

It looks like they try to randomize something from an array called gear.<br>
![image](https://github.com/user-attachments/assets/e2427578-7cd7-4a69-934f-8bae927093a4)

Let's try running the executable.<br>
![image](https://github.com/user-attachments/assets/622d07c9-ec96-400c-88eb-68ebc2712bc0)

We can search for that particular string in ghidra using Search -> Memory and select string format.<br>
![image](https://github.com/user-attachments/assets/dbd0e794-f11d-4cd7-82bb-303385102e39)

Now we got the list of things that are supposed to be in gear array.
Let's try to find the something unusual- whoops there you go.<br>
![image](https://github.com/user-attachments/assets/654e56fc-87a9-4317-bdd8-0d62660d453d)

Alternatively since we know the flag will have HTB prefix we can just search for that string immediately.<br>
![image](https://github.com/user-attachments/assets/24ffe67c-ebe2-4ba9-84f3-24985ac46539)

Lesson learnt:
- Search for particular string with ghidra.
- Check for Symbol Tree for functions and global references.
