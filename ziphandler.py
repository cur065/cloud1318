""" Find and read zip file """

import StringIO
import zipfile
import boto3
import mimetypes

s = boto3.resource("s3")
mb = s.Bucket("5934-build")

mySite_zip = StringIO.StringIO()
mb.download_fileobj("MySite.zip", mySite_zip)

with zipfile.ZipFile(mySite_zip) as myzip:
    for nm in myzip.namelist():
        nmObj = myzip.open(nm)
        # Do we really need ExtraArgs & mimetype?
        mb.upload_fileobj(nmObj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
        # mb.Object(nm).Acl().put(ACL='public-read')
