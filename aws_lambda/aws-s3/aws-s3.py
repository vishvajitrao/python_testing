import boto3

# Access key ID:- AKIAWROR2W2SSHVIA2MD
# Secret access key:- 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


# Create high level object oriented client
s3 = boto3.resource(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id='AKIAWROR2W2SSHVIA2MD',
    aws_secret_access_key='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'

)

# getting all the s3 buckets
# for i in s3.buckets.all():
#     print(i)


# access bucket by name
response = s3.Bucket("testing-vishvajit")
print(response)
# name
print(response.name)
# Creation date
print(response.creation_date)
# access acl
print(response.Acl().grants)

# bucket name
print(response.Acl().bucket_name)


# getting all objects of the specific bucket
# for i in s3.Bucket('testing-vishvajit').objects.all():
#     print(i.bucket_name, i.key)


# By using boto3 client - Create low level functional cleint

# s3 = boto3.client('s3', region_name='ap-south-1', aws_access_key_id='AKIAWROR2W2SSHVIA2MD', aws_secret_access_key='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')


# Bucket Owner:- 3dc45e98370f8233476c1bf698fbf84a0500736e1c98b463034b58f8138a54c0
# List buckets
# print(s3.list_buckets())

# Get object
# obj = s3.get_object(Bucket='testing-vishvajit', Key="work_packages_v2.1.xlsx")
# print(obj['Body'].read())

# delete object
# obj = s3.delete_object(Bucket='testing-vishvajit', Key="work_packages_v2.1.xlsx")
# print(obj)

# generate download url
# url = s3.generate_presigned_url(ClientMethod="get_object", Params={"Bucket": "testing-vishvajit", "Key": "work_packages_v2.1.xlsx"})
#
# print(url)


# get bucket location
# loc = s3.get_bucket_location(Bucket="testing-vishvajit")
# print(loc)


# Create bucket
#response = s3.create_bucket(ACL='public-read-write',Bucket='testing-vishvajit1',CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'},)

#print(response)

# get object tagging
# response = s3.get_object_tagging(Bucket='testing-vishvajit',Key = "Skyline.jpg")
# print(response)

# Returns the website configuration for a bucket.
# response = s3.get_bucket_website(Bucket='testing-vishvajit')
# print(response)

# Returns the access contole of the s3 bucket.
# response = s3.get_object_acl(Bucket='testing-vishvajit', Key = "Skyline.jpg")
# print(response)

















