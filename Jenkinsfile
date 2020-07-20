node {

    stage("Checkout repo") {
        git branch: 'master',
        url: 'https://github.com/alex-radchenko/test25-05.git'
    }

    stage("test") {
        sh '/usr/local/bin/pipenv run /usr/local/bin/pytest -v --tb=line test.py -k test_site_login_chrome -sv --alluredir=allure_result'
    }
    stage("report") {
        script {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure_result']]
                ])
        }
    }
}