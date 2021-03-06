# k8-demo-test

Eclipse marketplace yaml editor
===============================
Install eclipse marketplace - Help -> Install New Software (search for marketplace)



Build a docker image
====================

Dockerfile
FROM python:2.7

## make a local directory
RUN mkdir /opt/helloflask

# set as the working directory from which CMD, RUN, ADD references
WORKDIR /opt/helloflask

# copy the local requirements.txt to the directory
ADD requirements.txt .

# pip install the local requirements.txt
RUN pip install -r requirements.txt

# now copy all the files in this directory to /helloflask directory
ADD . .

# Listen to port 5000 at runtime
EXPOSE 5000

# Define our command to be run when launching the container
CMD ["python", "helloflask.py"]

Build
-----

cd /home/david/k8/helloflask/build
docker build -t helloflask .


Test image
----------
docker run -t -i -p 5000:5000 helloflask
docker run -d -p 5000:5000 helloflask
docker exec -i -t 00d1f9bf1419 /bin/bash    < log in to container bash

Push image to docker hub
------------------------
rename docker tags/image

docker tag helloflask:latest dev/helloflask:1.0
docker rmi helloflask:latest

docker login -u="user" -p="pass"
docker push dev/helloflask:1.0


Deployments and Replica sets are new in v1.6
============================================
pattern is declarative on the server side
supports rolling updates and rollback on server
recommended for new deployments
replication controller is more older approach

Example with Replication Controller
===================================
example yaml
------------
apiVersion: v1
kind: ReplicationController
metadata:
  name: helloflask-replicationctrl
spec:
  replicas: 3
  selector:
    app: helloflask
  template:
    metadata:
      name: helloflask
      labels:
        app: helloflask
        tier: web
    spec:
      containers:
      - name: helloflask
        image: dev/helloflask:1.0
        ports:
        - containerPort: 5000

create
------
kubectl create -f helloflaskdeploy.yaml

kubectl get rc
NAME                         DESIRED   CURRENT   READY     AGE
helloflask-replicationctrl   3         3         3         7m

kubectl describe rc
kubectl scale replicationcontroller --replicas=2 helloflask-replicationctrl

expose as service
-----------------
kubectl expose replicationcontroller helloflask-replicationctrl --type=NodePort

kubectl get services
NAME                         CLUSTER-IP   EXTERNAL-IP   PORT(S)          AGE
example-service              10.0.0.174   <nodes>       8080:32019/TCP   2d
helloflask-replicationctrl   10.0.0.176   <nodes>       5000:32001/TCP   4s
kubernetes                   10.0.0.1     <none>        443/TCP          2d

(providing a specific name)
kubectl expose replicationcontroller helloflask-replicationctrl --type=NodePort --name=helloflask-service

kubectl describe services

curl to dashboard ip:32001

expose using a service yaml file
--------------------------------
yaml
----
The configuration file, you can see that the Service routes traffic to Pods that have the labels app: helloflask and tier: web

kubectl get pods --selector="app=helloflask"
NAME                               READY     STATUS    RESTARTS   AGE
helloflask-replicationctrl-8kpmj   1/1       Running   0          1h
helloflask-replicationctrl-j8r8d   1/1       Running   0          1h
helloflask-replicationctrl-x0dl2   1/1       Running   0          1h

kind: Service
apiVersion: v1
metadata:
  name: helloflask-service
  labels: 
    run: helloflask
    tier: web
spec:
  selector:
    app: helloflask
    tier: web
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
  type: NodePort
    
    
kubectl describe service helloflask-service
Name:			helloflask-service
Namespace:		default
Labels:			run=helloflask
			tier=web
Annotations:		<none>
Selector:		app=helloflask,tier=web
Type:			NodePort
IP:			10.0.0.149
Port:			<unset>	5000/TCP
NodePort:		<unset>	31326/TCP
Endpoints:		172.17.0.7:5000,172.17.0.8:5000,172.17.0.9:5000
Session Affinity:	None
Events:			<none>

kubectl delete service helloflask-service


**To complete**
Deployments and replica set on a cluster
========================================

example yaml file

create the deployment
---------------------




Sudo docker fix
===============
sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo systemctl restart docker.service
newgrp docker


Portainer docker manager
========================
											
docker run -d -p 9000:9000 -v "/var/run/docker.sock:/var/run/docker.sock" portainer/portainer 


										

