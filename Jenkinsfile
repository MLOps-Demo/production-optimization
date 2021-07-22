pipeline {
  agent {
    kubernetes {
      label 'jenkins-slave'
      defaultContainer 'jnlp'
      yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: dind
    image: docker:18.09-dind
    securityContext:
      privileged: true
  - name: docker
    env:
    - name: DOCKER_HOST
      value: 127.0.0.1
    image: docker:18.09
    command:
    - cat
    tty: true
  - name: tools
    image: argoproj/argo-cd-ci-builder:v1.0.0
    command:
    - cat
    tty: true
"""
    }
  }
  stages {
    stage('Checkout GitHub Repository Main Branch') {
            steps {
                git branch: 'main', url : 'https://github.com/MLOps-Demo/production-optimization.git'
            }
        }
      
    stage('Build and Push Docker Image') {
      environment {
        DOCKERHUB_CREDS = credentials('docker-hub')
      }
      steps {
        container('docker') {
          // Build new image
          sh "pwd"
          sh "ls -lh"
          sh "until docker ps; do sleep 3; done && docker build -t skshreyas714/production-optimization:${env.GIT_COMMIT} -f model/Dockerfile model/"
          // Publish new image
          sh "docker login --username $DOCKERHUB_CREDS_USR --password $DOCKERHUB_CREDS_PSW && docker push skshreyas714/production-optimization:${env.GIT_COMMIT}"
        }
      }
    }

    stage('Deploy E2E to ArgoCD') {
      environment {
        GIT_CREDS = credentials('git')
      }
      steps {
        container('tools') {
          sh "git clone https://$GIT_CREDS_USR:$GIT_CREDS_PSW@github.com/MLOps-Demo/argocd-demo.git"
          sh "git config --global user.email 'skshreyas714@gmail.com'"

          dir("argocd-demo") {
            sh "cd ./e2e && kustomize edit set image skshreyas714/production-optimization:${env.GIT_COMMIT}"
            sh "git commit -am 'Publish new version' && git push || echo 'no changes'"
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

