pipeline {
    agent {
        node {
            label 'testing'
        }
    }

    stages {
        stage('Prepare') {
            steps {
                checkout([$class: 'GitSCM',
                branches: [[name: "origin\master"]],
                doGenerateSubmoduleConfigurations: false,
                submoduleCfg: [],
                userRemoteConfigs: [[
                    url: 'https://github.com/MLOps-Demo/production-optimization.git']]
                ])
            }
        }
        stage ('Docker_Build') {
            steps {
                \\ Build the docker image
                sh'''
                    # Build the image
                    docker build -t skshreyas714/production-optimization-model:0.11 -f model/Dockerfile model/
                    docker push skshreyas714/production-optimization:0.11
                '''
            }
        }
    }
}