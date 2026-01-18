# ML_deployement_using_kubernetes
This repo will teach you how to deploy and  scale you machine learning application, using FastAPI, Docker and kubernetes.

### Content
    - Deployment configuration, deployment files
    - Service configuration
    - Adding Health and readiness to check application health and readiness for usage
    - Autoscaling using HPA
    - Add ingress to expose service via HTTP
    - Add ngrok to create a URL for public demos 

### Deployment steps 
ML Project steps : 

prepare data --> train model --> evaluate model --> build docker image --> push docker image to docker hub --> deployment with kubernetes (We stand here)

1. Deployment configuration 

    Add deployment config to deployment.yaml
    
    Start minikube `minikube start`
    
    Run `kubectl apply -f deployment.yaml`
    
    Check by `kubectl get pods`

2. Service configuration 

    Add service config to service.yaml
    
    Run `kubectl apply -f service.yaml`
    
    Check by `kubectl get service`

3. (Optional) Now you can check if application work correctly

    Run `minikube service service_name` --url
    
    You find service_name in `kubectl get service`

4. Health and readiness (before using application check if application is healthy and model is loaded and ready to be used)

    Go to main.py (FastAPI) and add /health, def health(), /ready, and def ready() endpoints and functions
    
    rebuild you docker image `docker build -t docker_image_name .`
    
    push your image to docker hub `docker push `


5. HPA : horizontal pods autoscaling 

    Add hpa config to hpa.yaml 
    
    Then run commands : `kubectl apply -f hpa.yaml`
    
    Check if working by : `kubectl get hpa`
    
    If doesn't have access to metrics service (CPU ressources) use : `kubectl addons enable metrics-server`

6. Check if HPA works, using Hey 

    Install Hey first
    
    Check if Hey correctly installed using : `Hey`
    
    First find service url `minikube service your_service_name --url`
    
    In terminal 1 run : `hey -z 2m -c 20 your_url/predict`
    
    In terminal 2 : `kubectl get pods -w`
    
    In terminal 3 : `kubectl get service -w`

7. Add ingress :

    Enable ingress controler `kubectl addons enable ingress`

    Add ingress configuration to ingress.yaml
    
    Open notepad as administrator, open this file : C:\Windows\System32\drivers\etc\hosts, then add this to hosts : `127.0.0.1 ml-api.local`
    
    Now normaly this link : http://ml-api.local/health should work.
    
    If link doesn't work it could be a kubernetes <-> docker problem
    
    how to debug ingres : `kubectl get ingress`, `kubectl describe ingress <name>` and `kubectl get pods -n ingress-nginx`

8. (Optional) you can create a public URL, that others can use using ngrok

    Download ngrok from https://ngrok.com/download

    Put it in C:/system/ngrok, and add its path to you path

    Verfiy installation with : `ngrok version`

    In terminal 1 : `ngrok tunnel`

    In terminal 2 : Start an ngrok session : `ngrok http --host-header=ml-api.local 80`. This gives you a url 

    In terminal 3 : Check the ngrok url using `curl url/health`. Check also in browser. 


### CI/CD (via Github actioins) steps 

1. Add CI workflow configuration 
- Create .github/workflows/file.yaml
- Add config to yaml file, now eveytime you push code, steps in configuration will be executed

2. Add requirements-dev.txt, it will contain necessary dependencies for github actions to be executed
- You might need to add pytest library to the file

3. Add code quality test using black and ruff
- Add balck and ruff to requirements-dev.txt
- Add new file : pyproject.toml, it will contain black and ruff parameters and config (what qualities to verify in code)
- Add commands (`balck --check .` and `ruff check .`) to file.yaml
- Git Push and check github actions 




