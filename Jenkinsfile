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
                    clang++ --version
                '''
            }
        }

        stage('Build Test Package') {
            steps {
                bat '''
                    for /f "usebackq tokens=*" %%i in (`"%ProgramFiles(x86)%\\Microsoft Visual Studio\\Installer\\vswhere.exe" -latest -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -find Common7\\Tools\\VsDevCmd.bat`) do set VSDEVCMD=%%i
                    if not defined VSDEVCMD (
                        echo Could not find Visual Studio Build Tools C++ environment.
                        echo Install Visual Studio Build Tools with the Desktop development with C++ workload.
                        exit /b 1
                    )
                    call "%VSDEVCMD%" -arch=amd64
                    python scripts\\build.py --configuration Release
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'artifacts/**/*', allowEmptyArchive: true
        }
    }
}
