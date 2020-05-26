node {

    stage("Checkout repo"){
        git branch: 'master',
        url: 'https://github.com/alex-radchenko/test25-05.git'
    }
    stage("Install deps"){
        sh 'pip3 install pipenv'
        sh 'pip3 install pytest'
    }
    stage("Test"){
        sh 'cd tests'
        sh 'pytest test.py -sv --alluredir=allure_result'
    }

}



