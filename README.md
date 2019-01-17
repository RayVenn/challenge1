# How to run this app

**This is for python3, so make sure you are using python3** 
### 1. Use Python PEX file
  * Checkout this repo:
  
    `git clone https://github.com/RayVenn/challenge2.git`
  * Go into project, `cd challenge2`
  * For linux OS,
  
    `./challenge1-linux.pex`
  * For Mac OS,
  
    `./challenge1-osx.pex`
### 2. Docker container
  * You need to build the docker image based on Dockerfile:
  
    `docker build -t challenge:1 .`
  * Run this docker container:
  
    `docker run -p 5000:8080 challenge:1`
  * Open another terminal, and run the curl command:
  
    `curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' http://localhost:8080/messages`
### 3. Pip install
  * You need to install pip and virtualenv first
  * create a new virtualenv:
  
    `virtualenv test`
  * activate this virtualenv:
  
    `source test/bin/activate`
  * pip install the service from github:
  
    `pip install git+https://github.com/RayVenn/challenge1.git`
  * run challenge1 module:
  
    `python -m challenge1.app`
  
