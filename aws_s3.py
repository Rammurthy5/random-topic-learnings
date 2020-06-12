# For full doc: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.create_bucket

import boto3

accessKey = <xxx>
secretKey = <yyyy>

client = boto3.client('s3', aws_access_key_id=accessKey, aws_secret_access_key=secretKey)

s3 = boto3.resource('s3', aws_access_key_id=accessKey, aws_secret_access_key=secretKey)

buckets = client.list_buckets()

for b in buckets['Buckets']:
    print(b['Name'], b['CreationDate'])
assert buckets['ResponseMetadata']['HTTPStatusCode'] == 200, "Failed"
print("Bucket status code verified: 200")

import sys
# sys.exit(0)

object_acl = s3.ObjectAcl('saibaba05', 'a.docx')

print(object_acl.load())

# list the objects in a particular bucket
bucketobj = s3.Bucket("saibaba05")  # bucket name
for i in bucketobj.objects.all():
    print(i.key)

# Creating a new bucket on aws using Python SDK.
import traceback
from botocore.exceptions import ClientError

try:
    pyBuck = client.create_bucket(Bucket="pythonbucketrammurty", ACL="public-read")

    assert pyBuck['ResponseMetadata']['HTTPStatusCode'] == 200, "Failed"

except ClientError as e:
    print(e)


# uploading objects to S3

uploadResp = client.upload_file("pdfReadWrite.py", "pythonbucketrammurty", "pyobj")

print(uploadResp)

# delete obj from a bucket

# delete bucket

delBuck = client.delete_bucket(Bucket="pythonbucketrammurty")
