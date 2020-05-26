node {

    stage("Checkout repo"){
        git branch: 'master',
        url: 'https://github.com/alex-radchenko/test25-05.git'
    }
    stage("Install deps"){
        sh 'pipenv install'
    }
    stage("Test"){
        sh 'pipenv run pytest test.py -sv --alluredir=allure_result'
    }

}



