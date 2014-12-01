from fabric.api import local

def sync_www():
    local('aws s3 sync www s3://joshcrompton.com/')
