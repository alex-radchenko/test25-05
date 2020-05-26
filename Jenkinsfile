node {

    stage("Checkout repo"){
        git branch: 'master',
        url: 'https://github.com/alex-radchenko/test25-05.git'
    }
    stage("Install deps"){
        sh 'pip3 install pipenv'
    }
    stage("Test"){
        sh 'pipenv run tests -sv'
    }

}