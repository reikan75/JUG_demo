pipeline{
    agent any
    environment{
        GIT_CREDENTIALS = credentials('github_token')
        VENV_PATH = 'venv'
    }
    
    stages{
        stage("Build"){
            steps{
                sh "python3 -m venv ${VENV_PATH}"
                sh "source ${VENV_PATH}/bin/activate"
                sh "pip3 install -r requirements.txt"
            }
        }
        stage("Unit Test"){
            steps{
                sh "source ${VENV_PATH}/bin/activate"
                sh "python3 -m coverage run -m unittest tests/test_calculator.py"
                sh "python3 -m coverage xml"
            }  
        }
        stage("Sonar Scan"){
            steps{
                sh "/usr/local/Cellar/sonar-scanner/5.0.1.3006/bin/sonar-scanner"
            }  
        }
    }
    post {
        always {
            // Clean up workspace
            deleteDir()
        }
    }
}