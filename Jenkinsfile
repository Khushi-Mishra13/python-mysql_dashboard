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
				docker compose exec -T mysql mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} -e "
                        CREATE TABLE IF NOT EXISTS users (
                            Roll_No INT,
                            Name VARCHAR(60),
                            Subjects VARCHAR(50)
                        );

                        INSERT INTO users (Roll_No, Name, Subjects)
                        VALUES (4, 'thy', 'c++');
                    "
				'''
					}
				}
			
		}
}
