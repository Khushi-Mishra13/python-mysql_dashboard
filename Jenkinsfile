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
