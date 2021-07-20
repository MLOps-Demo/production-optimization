pipeline {
    environment { 
        registry = "skshreyas714/production-optimization" 
        registryCredential = 'skshreyas714'
        BUILD_NUMBER = 0.11
        dockerImage = '' 
    }
    
    agent {
        kubernetes {
      defaultContainer 'core-builder'
      yamlFile 'kubernetes/podTemplate.yaml'
        }
    }

    stages {
        stage('Clone GitHub Repository Master Branch') {
            steps {
                git branch: 'main', url : 'https://github.com/MLOps-Demo/production-optimization.git'
            }
        }
        stage ('Build Docker Image and Push to Docker Hub') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" model/Dockerfile
                    docker.withRegistry('', registryCredential) { 
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Cleaning up') { 
            steps { 
                sh "docker rmi $registry:$BUILD_NUMBER" 
            }
        } 
    }
}
