node {

    stage("Checkout repo"){
        git branch: 'master',
        url: 'https://github.com/alex-radchenko/test25-05.git'
    }
    stage("test"){
        sh 'pip install pytest'
    }
    stage("test"){
        sh 'pytest test.py -sv --alluredir=allure_result'
    }
}




