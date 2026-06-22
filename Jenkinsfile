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
                powershell '''
                    $ErrorActionPreference = "Stop"

                    $vswhere = Join-Path ${env:ProgramFiles(x86)} "Microsoft Visual Studio\\Installer\\vswhere.exe"
                    if (-not (Test-Path $vswhere)) {
                        throw "Could not find vswhere.exe at $vswhere. Install Visual Studio Build Tools."
                    }

                    $vsDevCmd = & $vswhere -latest -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -find "Common7\\Tools\\VsDevCmd.bat"
                    if (-not $vsDevCmd) {
                        throw "Could not find Visual Studio Build Tools C++ environment. Install the Desktop development with C++ workload."
                    }

                    Write-Host "Using Visual Studio environment: $vsDevCmd"
                    cmd.exe /s /c "call `"$vsDevCmd`" -arch=amd64 && python scripts\\build.py --configuration Release"
                    if ($LASTEXITCODE -ne 0) {
                        exit $LASTEXITCODE
                    }
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
