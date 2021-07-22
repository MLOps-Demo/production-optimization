pipeline {
    environment { 
        registry = "skshreyas714/production-optimization" 
        registryCredential = 'skshreyas714'
        BUILD_NUMBER = 0.12
        dockerImage = '' 
    }
    
    agent {
        kubernetes {
      defaultContainer 'core-builder'
      yamlFile 'podTemplate.yaml'
        }
    }

    stages {
        stage('Clone GitHub Repository Master Branch') {
            steps {
                git branch: 'main', url : 'https://github.com/MLOps-Demo/production-optimization.git'
            }
        }
        stage ('Start the docker engine') {
            steps {
                sh '''
                service docker start
                # the service can be started but the docker socket not ready, wait for ready
                WAIT_N=0
                while true; do
                  # docker ps -q should only work if the daemon is ready
                  docker ps -q >/dev/null 2>&1 && break
                  if [[ ${WAIT_N} -lt 5 ]]; then
                    WAIT_N=$((WAIT_N + 1))
                    echo "[SETUP] Waiting for Docker to be ready, sleeping for ${WAIT_N} seconds ..."
                    sleep ${WAIT_N}
                  else
                    echo "[SETUP] Reached maximum attempts, not waiting any longer ..."
                    break
                  fi
                done
                '''
            }
        } 
        stage ('Build Docker Image and Push to Docker Hub') {
            steps {
                sh '''
                cd model
                pwd
                ls -lh
                '''
                script {
                    def dockerfile = "model/Dockerfile"
                    dockerImage = docker.build("${env.registry}:${env.BUILD_NUMBER}", "-f ${dockerfile} ./model")
                    docker.withRegistry('https://registry.hub.docker.com/', registryCredential) { 
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
