pipeline{
    agent any
    environment{
        Dev_IP="13.233.19.188"  // update with development server ip
        QA_IP="13.233.19.188"   // update with QA server ip
    }
    stages{
        stage("Download code"){
           steps{
                git branch: 'main', url: 'https://github.com/harshitadwivedi1199/TO-DO-List.git'
           }
        }
        stage("Build docker image"){
            steps{
               
                sh " docker build -t harc1199/to-do-list:${BUILD_TAG} ."
            }
        }
        
        stage("Push docker image"){
            steps{
                sh "whoami"
                withCredentials([string(credentialsId: 'DOCKER_HUB_PASSWD', variable: 'DOCKER_HUB_CRED_PASSWD')]) {
                    sh "docker login -u harc1199 -p $DOCKER_HUB_CRED_PASSWD"
                    sh "docker push harc1199/to-do-list:${BUILD_TAG} "
                    
                }
            }
        }
        
         stage("Deploy in Dev"){
             steps{
                 sshagent(['DEV_QA_PROD_ENV']) {
                     sh "ssh -o StrictHostKeyChecking=no ec2-user@${Dev_IP} sudo docker rm -f  myweb"
                     sh "ssh ec2-user@${Dev_IP} sudo docker run -d -p 5000:5000 --name myweb harc1199/to-do-list:${BUILD_TAG}"
    
                 }
             }
         }
        // stage("Deploy in QA"){
        //     steps{
        //         sshagent(['DEV_QA_PROD_ENV']) {
        //             sh "ssh -o StrictHostKeyChecking=no ec2-user@${QA_IP} sudo docker rm -f  myweb"
        //             sh "ssh ec2-user@${QA_IP} sudo docker run -d -p 80:80 --name myweb harc1199/Task-manager-project:${BUILD_TAG}"
    
        //         }
        //     }
        // }
        // stage("Testing QA"){
        //     steps{
        //         sshagent(['DEV_QA_PROD_ENV']) {
        //             sh "curl --silent http://${QA_IP}/"
        //         }
        //     }
        // }
        stage("Manual Approval"){
            steps{
                input(message: "Do you want to continue ?? ")
            }
        }
        stage("Deploy in prod"){
            steps{
                withAWS(credentials: 'aws_cred', region: 'ap-south-1') {
                  script {
                    sh ('aws eks update-kubeconfig --name mycluster  --region ap-south-1')
                    BUILD_TAG="${BUILD_TAG}"
                    sh "envsubst < deployment-svc.yaml | kubectl apply -f deployment.yaml"
                    sh "kubectl apply -f svc.yaml"
                    sh "kubectl get pods"
                    sh "kubectl get deployment"
                    sh "kubectl get svc"
                    }            
  }
            }
        
    }
}
}

