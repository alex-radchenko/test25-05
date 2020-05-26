node {

    stage("Checkout repo"){
        git branch: 'master',
        url: 'https://github.com/alex-radchenko/test25-05.git'
    }
    stage("install"){
        sh 'pip3 install pipenv'
        sh 'pipenv install'
    }

}




