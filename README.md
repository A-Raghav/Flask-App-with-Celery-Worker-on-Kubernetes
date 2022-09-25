## Demo for running a simple Flask-based application using Celery Workers and Redis Message Broker

### Pre-Requisites
1. `kubectl` installed
2. `Docker-Desktop` installed
3. `Kubernetes` enabled in `Docker-Desktop`

### Steps:
1. Build the app (`web`) image using docker-compose command or docker build command
2. Create the kubernetes namespaces, secrets, and deployments by running the `.yml` files in the `k8s_config` directory (first run the `namespaces.yml`, then `secrets.yml`, and then the remaining `.yml` files) using the command - `kubectl apply -f <file-name>.yml`
3. Install the `dunn.redis` extension on your VSCode to view the results from CELERY-workers that will be stored in the Redis Backend
4. Open the installed Redis Explorer extension i VSCode, and add a new connection at IP Address: `localhost` and Port: 6379
5. Open Postman for API testing. Create the following POST and GET requests - 
    * [GET] Health-Request
        - URL: `localhost:5000`
    * [POST] Post-Test
        - URL: `localhost:5000/test`
        - Payload: {"input": 2}
    * [POST] Square
        - URL: `localhost:5000/square`
        - Payload: {"input": 6}