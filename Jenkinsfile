node {

    stage("Checkout repo"){
        git branch: 'master',
        url: 'https://github.com/alex-radchenko/test25-05.git'
    }
    stage("VV"){
        sh 'python3 -V'
        sh 'python -V'
    }
    stage("test"){
        sh '/usr/local/bin/pytest test.py'
    }
}