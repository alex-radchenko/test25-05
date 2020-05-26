node {

    stage("Checkout repo"){
        git branch: 'master',
        url: 'https://github.com/alex-radchenko/test25-05.git'
    }
    stage("VV"){
        sh 'pipenv install'
    }

}