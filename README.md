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
