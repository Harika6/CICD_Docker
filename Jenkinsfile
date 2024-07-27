pipeline {
    agent any
    environment {
        KUBECONFIG_CREDENTIALS = credentials('kubeconfig')
    }
    stages {
        stage('Deploy') {
            steps {
                script {
                    // Load kubeconfig from Jenkins credentials and set environment variable
                    withCredentials([string(credentialsId: 'kubeconfig', variable: 'KUBECONFIG_CONTENT')]) {
                        writeFile(file: 'kubeconfig', text: KUBECONFIG_CONTENT)
                        sh 'export KUBECONFIG=kubeconfig'
                        
                        // Apply Kubernetes manifests
                        sh 'kubectl apply -f deployment.yaml'
                        sh 'kubectl apply -f service.yaml'
                        sh 'kubectl apply -f ingress.yaml'
                    }
                }
            }
        }
    }
}
