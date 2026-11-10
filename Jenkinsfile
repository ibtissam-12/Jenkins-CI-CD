pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('github-token')
        VENV_DIR = ".venv"
        HOST = "0.0.0.0"
        PORT = "5000"
        APP_MODULE = "app:app"  
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ibtissam-12/Jenkins-CI-CD.git',
                    credentialsId: 'github-token'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat """
                python -m venv ${VENV_DIR}
                call ${VENV_DIR}\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

    stage('Run Tests') {
    steps {
        bat """
        call ${VENV_DIR}\\Scripts\\activate
        python -m pytest test_app.py -v
        """
    }
}

        stage('Deploy (Local with Gunicorn)') {
            steps {
                echo 'Starting Flask app locally using Gunicorn...'
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                start /B gunicorn --bind ${HOST}:${PORT} ${APP_MODULE} > gunicorn.log 2>&1
                echo ✅ Gunicorn started on http://${HOST}:${PORT}
                """
            }
        }
    }
}

         
