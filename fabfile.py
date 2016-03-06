from fabric.api import local

def deploy():
    local('git pull origin develop')
    local('rm -rf wsgi/project')
    local('cp -r project wsgi/project')
