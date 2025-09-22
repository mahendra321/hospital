pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "medcare_app:latest"
    }

    stages {
        stage('Build') {
            steps {
                sh 'apt install python3.11-venv'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
                sh 'flake8 . || true'
                sh 'mypy . || true'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
