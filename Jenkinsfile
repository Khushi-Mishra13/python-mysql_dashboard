pipeline {
  agent any
  stages {
    stage('To Checkout SCM') {
      steps {
        checkout scm
      }
    }
    stage('Create .env') {
      steps {
        sh '''
        	cat > .env << EOF
        	MYSQL_HOST = mysql
        	MYSQL_USER = user
        	MYSQL_PASSWORD = password
        	MYSQL_DATABASE = dashboard
EOF
    	'''
      }
    }
    stage('To Build Docker Image') {
      steps {
        sh 'docker build -t ghcr.io/khushi-mishra13/python-mysql_dashboard:latest .'
      }
    }
    stage('Trivy Scan Image') {
      steps {
         sh '''
         #trivy image --severity HIGH,CRITICAL ghcr.io/khushi-mishra13/python-mysql_dashboard:latest
       '''
      }
    }
    stage('push it to ghcr') {
      steps {
        withCredentials([
          usernamePassword(
            credentialsId: 'github-token-id',
            usernameVariable: 'username',
            passwordVariable: 'password'
          )
        ]) {
          sh '''
          echo "$password" | docker login ghcr.io -u "$username" --password-stdin
          docker push ghcr.io/khushi-mishra13/python-mysql_dashboard:latest
          '''
        }

      }
    }

    stage('deploy on vm') {
      steps {
        sshagent(credentials: ['khushi-vm']) {
          withCredentials([
            usernamePassword(
              credentialsId: 'github-token-id',
              usernameVariable: 'username',
              passwordVariable: 'password'
            )
          ]) {
            sh '''
            ssh -o StrictHostKeyChecking=no -p 5125 khushi@192.168.7.102 << EOF
            echo "$password" | docker login ghcr.io -u "$username" --password-stdin

            cd ~/dashboard &&
            docker compose down &&
            docker compose pull &&
            docker compose up -d --remove-orphans
            #docker pull ghcr.io/khushi-mishra13/python-mysql_dashboard:latest
            #docker run -d -p 8082:5000 ghcr.io/khushi-mishra13/python-mysql_dashboard:latest
EOF
              '''
          }
        }
      }
    }
  }

}
