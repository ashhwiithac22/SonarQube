pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ashhwiithac22/SonarQube.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('My Sonar Server') {
                    withCredentials([string(credentialsId: 'squ_3b5c5b11e105c8d63b448bfb5d047bcb5f12d61c', variable: 'SONAR_TOKEN')]) {
                        sh "/opt/sonar-scanner/bin/sonar-scanner -Dsonar.login=$SONAR_TOKEN"
                    }
                }
            }
        }

    }
}
