node {

    stage("Checkout repo"){
        git branch: 'master',
        url: 'https://github.com/alex-radchenko/test25-05.git'
    }
    stage("install"){
        sh 'pip3 install pytest'
    }
    stage("test"){
        sh 'pytest test.py -sv --alluredir=allure_result'
    }
}




