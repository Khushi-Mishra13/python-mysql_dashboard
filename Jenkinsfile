pipeline{
	agent any
	stages{
		stage('To Checkout SCM'){
			steps{
				checkout scm
				}
			}
		stage('Create .env') {
                        steps {
                                sh '''
                                cat > .env <<EOF
				MYSQL_HOST=mysql
				MYSQL_USER=user
				MYSQL_PASSWORD=password
				MYSQL_DATABASE=dashboard
				EOF
                	'''
            }
        }
		stage('Stop running containers'){
			steps{
				sh'docker compose down'
				}
			}
		stage('To Build Docker Image'){
			steps{
				sh'docker compose build '
				}
			}
		stage('To Run The Image'){
			steps{
				sh'docker compose up -d'
					}
				}
			
		}
}
