pipeline{
	agent any
	stages{
		stage('To Checkout SCM'){
			steps{
				checkout scm
				}
			}
		stage('To Build Docker Image'){
			steps{
				sh'docker build -t python-mysql-dashboard .'
				}
			}
		stage('To Run The Image'){
			steps{
				sh'docker run -p 4001:4001 python-mysql-dashboard'
					}
				}
			
		}
}
