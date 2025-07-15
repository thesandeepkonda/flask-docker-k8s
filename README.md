# flask-docker-k8s
# Flask Docker Kubernetes Example

## 🚀 Description
A simple Flask app containerized with Docker and deployed using Kubernetes.

## 🐳 Docker Commands

```bash
# Build Docker image
docker build -t my-flask-app .

# Run locally
docker run -p 5000:5000 my-flask-app


#Kubernetes Commands

# Apply Kubernetes resources
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Access service (if using Minikube)
minikube service flask-service


# Docker Hub
Don't forget to push your image:

docker tag my-flask-app YOUR_DOCKER_USERNAME/my-flask-app
docker push YOUR_DOCKER_USERNAME/my-flask-app
