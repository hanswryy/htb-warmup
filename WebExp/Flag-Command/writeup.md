# Flag Command

This one is really easy.
First go inspect the website and go to Sources tab.<br>
![image](https://github.com/user-attachments/assets/793c6890-ab64-4707-8f8a-fcb75fcbb4dd)

Go read all the three .js files. In main.js you'll find some code that tell about some secret options.<br>
![image](https://github.com/user-attachments/assets/88a43a4d-947e-4fea-ac7c-28a90f918202)

It looks like availableOption is fetched from some API endpoint, it's a clue to see the Network tab where you can find all the HTTP Request happening inside the web.<br>
![image](https://github.com/user-attachments/assets/77edf61c-a4e6-4754-9514-009bf787506a)

Found the endpoint.<br>
![image](https://github.com/user-attachments/assets/dba8b680-023e-4bfc-9974-880ff8213bfa)

Got the secret option in the response tab.<br>
![image](https://github.com/user-attachments/assets/f9d4312e-1c55-4316-b997-e601b1d352e4)

Just copy paste the secret option and boom, flag.<br>
![image](https://github.com/user-attachments/assets/9ec3a596-f062-48d9-8a76-fc65197abb17)

This show the awareness to not show all the important and secret information to the API response.
