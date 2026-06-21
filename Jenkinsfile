pipeline {
    agent {
        label 'windows-cpp'
    }

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '20'))
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Show Build Machine Tools') {
            steps {
                bat '''
                    echo Computer: %COMPUTERNAME%
                    echo Workspace: %WORKSPACE%
                    git --version
                    python --version
                    cmake --version
                    ninja --version
                '''
            }
        }

        stage('Build Test Package') {
            steps {
                bat 'python scripts\\build.py --configuration Release'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'artifacts/**/*', allowEmptyArchive: true
        }
    }
}
