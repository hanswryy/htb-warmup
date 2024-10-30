# TIMEKORP

agak curang soalnya nyontek write up orang lain

Looking at the project folder, we saw some exec code. Mosty likely some RCE (Remote Code Execution) vuln.<br>
![Screenshot 2024-10-30 210010](https://github.com/user-attachments/assets/76574eaa-9ffc-4d24-ab57-40f26dfa483c)

If we go to the controller code, we can see if we set format as parameter it is passed to the code before from the model.<br>
![image](https://github.com/user-attachments/assets/45ae1a07-be9b-4504-ae9d-5dc8a23a276a)

Try ls.<br>
![image](https://github.com/user-attachments/assets/af8b6906-c477-44a4-b43d-27bc2b15334a)<br>
![image](https://github.com/user-attachments/assets/52ebc732-eb66-486c-8cae-721462566a7a)

Flag is inside root folder where views is inside the "challange" folder, so we just need to cat the flag using <br>
```
cat ../flag
```
<br>
![image](https://github.com/user-attachments/assets/a11be05c-8251-47fc-8368-d94b5249615f)<br>
![image](https://github.com/user-attachments/assets/246832e2-614e-4c8b-af62-4d033f582e1c)
