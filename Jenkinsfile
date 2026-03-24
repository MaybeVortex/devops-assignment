pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        DOCKER_USERNAME = "yourusername"
        IMAGE_FRONTEND = "${DOCKER_USERNAME}/reg_roll_frontend"
        IMAGE_BACKEND = "${DOCKER_USERNAME}/reg_roll_backend"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'your-github-repo-link'
            }
        }

        stage('Build Images') {
            steps {
                sh 'docker build -t $IMAGE_FRONTEND ./frontend'
                sh 'docker build -t $IMAGE_BACKEND ./backend'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKER_USERNAME --password-stdin'
                sh 'docker push $IMAGE_FRONTEND'
                sh 'docker push $IMAGE_BACKEND'
            }
        }
    }
}
