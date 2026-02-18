pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/venkatapavan99/Python_auto.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                venv/bin/pip install --upgrade pip
                venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Automation Tests') {
            steps {
                sh '''
                PYTHONPATH=$WORKSPACE venv/bin/pytest \
                --html=report.html \
                --self-contained-html
                '''
            }
        }

        stage('Archive Test Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            }
        }
    }

    post {
        success {
            withCredentials([string(credentialsId: 'slack-webhook-url', variable: 'SLACK_URL')]) {
                sh '''
                curl -X POST -H 'Content-type: application/json' \
                --data '{"text":"✅ Printer Automation Build SUCCESS: '${BUILD_URL}'"}' \
                $SLACK_URL
                '''
            }
        }

        failure {
            withCredentials([string(credentialsId: 'slack-webhook-url', variable: 'SLACK_URL')]) {
                sh '''
                curl -X POST -H 'Content-type: application/json' \
                --data '{"text":"❌ Printer Automation Build FAILED: '${BUILD_URL}'"}' \
                $SLACK_URL
                '''
            }
        }
    }
}
