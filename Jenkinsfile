pipeline{
	agent any{
		stages{
			stage('To Checkout SCM'){
				steps{
					checkout SCM
					}
				}
			stage('To Build Docker Image'){
				steps{
					sh'docker build -t pyhton-mysql-dashboard'
					}
				}
			stage('To Run The Image'){
				steps{
					sh'docker run -p 5000:8080 python-mysql-dashboard'
						}
					}
			}
		}
}
