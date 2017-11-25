""" Find and read zip file """

import boto3

s = boto3.resource("s3")
mb = s.Bucket("5934-build")

for obj in mb.objects.all():
    print obj.key
    mb.download_file(obj.key, obj.key)
