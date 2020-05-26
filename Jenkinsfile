node {

    stage("Checkout repo"){
        git branch: 'master',
        url: 'https://github.com/alex-radchenko/test25-05.git'
    }
    stage("install"){
        bash 'pip3 install pipenv'
        bash 'pip3 install pytest'
    }
    stage("test"){
        bash 'pytest test.py'
    }
}




