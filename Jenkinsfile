node {

    stage("Checkout repo"){
        git branch: 'master',
        url: 'https://github.com/alex-radchenko/test25-05.git'
    }

    stage("test"){
        sh '/usr/local/bin/pipenv run /usr/local/bin/pytest test.py'
    }
}