## Instruction for pull the docker file from docker hub and run docker in desktop.

## 1) Install Docker Desktop for mac
https://www.docker.com/products/docker-desktop/
Docker desktop gmail >> rishabhvishwakarma015@gmail.com
Docker Hub gmail >> rishabhvishwakarma015@gmail.com

## 2) pull the docker file from docker hub
docker pull {docker-name}
    '''docker file shows in the docker desktop'''

## 3) Run the docker file
docker run {docker-name}
docker run -p 8501:8501 {docker-name}  # Here use the port mapping
http://localhost:8501/                 # Open local host port in chrome

## -d (detach mode) use for run the docker in backend and -p is port number
docker run -d -p 8501:8501 {docker-name}  # Here use the port mapping

## 4) For upload the dockerfile into the DockerHub
    - docker login
    - docker push rishabh013/laptop  (Start upload the docker file in dockerHUb)
    OR
    - docker push {docker-name}  (Start upload the docker file in dockerHUb)


## 5)  List the running container
    -- docker ps

## 6) stop the docker, docker id get from the docker ps command
    -- docker stop {docker id}