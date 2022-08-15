
# Welcome to CLO835 Project!

## Create docker image and pushing the image in ECR

Pull the latest changes

    git pull

Run the application locally

- Move to sub folder `cd ./simple-webapp-mysql`
- Build the application in docker `docker build -t webapp-mysql .`
- Run docker image in local `docker run -it --env IMAGE_URL=/img --env USER_NAME=dipen -p 8080:81 webapp-mysql`

Push the image to ECR

- Login AWS ECR `aws ecr get-login-password --region {REGION} | docker login --username AWS --password-stdin {ACCOUNTID}.dkr.ecr.{REGION}.amazonaws.com`
- Tag docker image `docker tag simple-web-mysql:latest {ACCOUNTID}.dkr.ecr.{REGION}.amazonaws.com/simple-web-mysql:latest`
- Push the docker Image `docker push {ACCOUNTID}.dkr.ecr.{REGION}.amazonaws.com/simple-web-mysql:latest`


## Step by Step command to create infrastructure 

     cd manifestfiles
     k create ns final
     eksctl create iamserviceaccount --name clo835 --namespace final --cluster clo835 --attach-policy-arn arn:aws:iam::083477265364:policy/awss3roleaccessbucket --approve
     k apply -f serviceaccount.yaml
     k apply -f configmap.yaml
     k apply -f secret.yaml
     k apply -f pvc.yaml 
     k apply -f mysql-pod-definition.yaml
     k apply -f mysql-service.yaml
     k apply -f frontend-flask.yaml
     k apply -f frontend-service.yaml


### Helpful command for Testing HPA 

  

      k autoscale deployment simple-webapp-mysql --cpu-percent=50  --min=1 --max=10 -n final
      k run -i --tty load-generator --image=busybox /bin/sh -n final
      while true; do wget -q -O - http://simple-webapp-mysql; done
      k get hpa -w -n final
      k get pods -n final
