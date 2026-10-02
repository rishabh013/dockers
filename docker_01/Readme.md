1) Create a simple flask code from the chatgpt and paste in the app.py
2) add requirements.txt file
3) Create a 'Dockerfile' file
    - Write the dependencies in the docker file
4) Build the docker
    - docker build -t rishabh013/table .
    ''' docker file is building now, after building the docker you can check in the docker desktop, there the docker file will be show '''
5) Run the docker file in VS code console.
    - docker run -p 8888:5000 rishabh013/table
    ''' In the docker run code, 8888 is the local host port, and 5000 is the docker run port (which is mention in the dockerfile port section) '''

