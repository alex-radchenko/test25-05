node {

    stage("Checkout repo"){
        git branch: 'master',
        url: 'https://github.com/alex-radchenko/test25-05.git'
    }
    stage("Install deps"){
        sh 'pipenv install'
        sh 'pipenv --version'
    }
    stage("Test"){
        sh 'pytest test.py -sv --alluredir=allure_result'
    }

}



