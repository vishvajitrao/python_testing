# Statistics is the process of study and manipulating the data, gather, review, draw and conclusion the data.
from statistics import *
# 1. Mean:-The mean usually referred to as average.

data = [12, 20, 30, 12, 87]
result = mean(data=data)
print("The mean is:- ",result)

# 2. fmean:- Convert data to float and compute the mean

data = [12, 20, 30, 12, 87]
result = fmean(data=data)
print("The fmean is:- ",result)


# 3. Geometric mean:- The geometric mean is a type of number, the geometric mean multiple the whole number and then compute the root of he numbers.

data = [2, 3, 6]
result = geometric_mean(data=data)
print("The Geometric Mean is:- ", result)

# 4. The harmonic mean is a type of average.Harmonic mean calculated by the total numbers of observation divided by the sum of reciprocal of each item.

data = [40, 60]
result = harmonic_mean(data=data)
print("The Harmonic mean is:- ", result)


# 5. Median is a type of average which describe the where the centered data is located.

data = [13, 21, 21, 40, 48, 55, 72]
result = median(data=data)
print("The Median is:- ", result)

# 6. median_low

data = [13, 21, 21, 40, 48, 55, 72]
result = median_low(data=data)
print("The Median low is:- ",result)

# 6. median_high

data = [13, 21, 21, 40, 48, 55, 72]
result = median_high(data=data)
print("The Median high is:- ",result)

# 6. median_grouped

data = [13, 21, 21, 40, 48, 55, 72]
result = median_grouped(data=data)
print("The Median grouped is:- ",result)

# 7. Mode:- Mode is a type of average, which describe where he most of the data located.

data = [13, 55, 21, 55, 48, 55, 72]
result = mode(data=data)
print("The Mode is:- ", result)


# 7. multimode:- Multimode function return list of the most frequently occurring values in the sequence.

data = 'abcdaaccfff'
result = multimode(data=data)
print("The Multimode is:- ", result)


print("-------------------------------------------")


import boto3

_client = boto3.client("s3", region_name="us-east-1")
_url = _client.generate_presigned_url(
                ClientMethod="get_object", Params={"Bucket": "my-images-hub", "Key": "Skyline.jpg"}, ExpiresIn=604800
            )

print(_url)