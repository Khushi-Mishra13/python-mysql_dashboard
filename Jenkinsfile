pipeline{
	agent any
	stages{
		stage('To Checkout SCM'){
			steps{
				checkout scm
				}
			}
		stage('Get secrets from vault and create .env'){
			steps{
				withVault(
					configuration: [
						vaultUrl: 'http://localhost:8200',
						vaultCredentialId: 'vault-python-dashboard'
					],
					vaultSecrets: [
						[
							path: 'secret/data/python-dashboard',
							secretValues: [
								[envVar: 'MYSQL_HOST', vaultKey: 'MYSQL_HOST'],
								[envVar: 'MYSQL_USER', vaultKey: 'MYSQL_USER'],
								[envVar: 'MYSQL_PASSWORD', vaultKey: 'MYSQL_PASSWORD'],
								[envVar: 'MYSQL_DATABASE', vaultKey: 'MYSQL_DATABASE']
							]
						]
					]
				){
					sh '''
						cat > .env <<EOF
MYSQL_HOST=$MYSQL_HOST
MYSQL_USER=$MYSQL_USER
MYSQL_PASSWORD=$MYSQL_PASSWORD
MYSQL_DATABASE=$MYSQL_DATABASE
EOF
					'''
				}
			}
		}
		stage('Stop running containers'){
			steps{
				sh'docker compose down --remove-orphans'
				}
			}
		stage('To Build Docker Image'){
			steps{
				sh'docker compose build --no-cache'
				}
			}
		stage('To Run The Image'){
			steps{
				sh'''
				docker compose up -d --remove-orphans
				
				
				'''
					}
				}
			
		}
}
