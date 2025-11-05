pipeline {
    agent any

    triggers {
        pollSCM('H/10 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AlexanderYanuchkovskiy/io_simp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('keply186/io_simp:latest')
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-login') {
                        docker.image('keply186/io_simp:latest').push()
                    }
                }
            }
        }
    }
}
