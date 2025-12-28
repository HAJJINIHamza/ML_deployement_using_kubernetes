# ML_deployement_using_kubernetes
Deploy ML model and scale using FastAPI, Docker and Kubernetes

### Deployment steps 

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

    Start an ngrok session : `ngrok http --host-header=ml-api.local 80`. This gives you a url 

    Check the ngrok url using `curl url/health`. Check also in browser. 


