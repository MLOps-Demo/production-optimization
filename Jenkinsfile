pipeline {
    agent {
        kubernetes {
      defaultContainer 'core-builder'
      yamlFile 'models/podTemplate.yaml'
        }
    }

    stages {
        stage('Clone GitHub Repository Master Branch') {
            steps {
                git branch: 'main', url : 'https://github.com/MLOps-Demo/production-optimization.git'
            }
        }
        stage ('Docker_Build') {
            steps {
                sh'''
                # FIRST WE START THE DOCKER DAEMON
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

                # Build the image
                docker build -t skshreyas714/production-optimization-model:0.11 -f model/Dockerfile model/
                docker push skshreyas714/production-optimization:0.11
                '''
            }
        }
    }
}
