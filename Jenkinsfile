node {

    stage("Checkout repo"){
        git branch: 'master',
        url: 'https://github.com/alex-radchenko/test25-05.git'
    }
    stage("pipenv"){
        sh 'pip install pipenv'
    }
    stage("pipenv2"){
        sh 'pipenv install'
    }
    stage("test"){
        sh 'pipenv run pytest test.py -sv --alluredir=allure_result'
    }
}




