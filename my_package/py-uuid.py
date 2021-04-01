import uuid

#make unique time based on host address and current itme
id = uuid.uuid1()
print(id)

# Result:- f3a446e6-7276-11eb-8c1e-e96d9981a7f3
# f3a446e6:- time_low
# 7276:- time_mid
# 11eb:- “time_high_and_version
# 8c1e:- clock_seq_and_reserved_And_clock_seq_low
# e96d9981a7f3:- Node

#generate unique id using clock sequence and mac id
print(uuid.uuid1(clock_seq=4115, node=0xe96d9981a7f3))

#get node id
print(uuid.getnode())


#generate random uuid using uuid4
print("Generate random unique id using uuid4:- ", uuid.uuid4())


#generate name based unique id using uuid3 and uuid5.
print('Unique id using uuid3:- ', uuid.uuid3(uuid.NAMESPACE_DNS, 'google.com'))
print('Unique id using uuid5:- ', uuid.uuid5(uuid.NAMESPACE_DNS, 'google.com'))


nameSpaces = [uuid.NAMESPACE_DNS, uuid.NAMESPACE_URL, uuid.NAMESPACE_OID, uuid.NAMESPACE_X500]
hostName = 'google.com'
print("Generate uuid using namespace")

for namespace in nameSpaces:
    print('uuid 3 is', uuid.uuid3(namespace, hostName))
    print('uuid 5 is', uuid.uuid5(namespace, hostName))
    print()



print('----------------')
# Extract uuid 
UUID = uuid.uuid1()

print("UUID is ", UUID)
print("UUID Type is ",type(UUID))
print('UUID.bytes   :', UUID.bytes)
print('UUID.bytes_le :', UUID.bytes_le)
print('UUID.hex     :', UUID.hex)
print('UUID.int     :', UUID.int)
print('UUID.urn     :', UUID.urn)
print('UUID.variant :', UUID.variant)
print('UUID.version :', UUID.version)
print('UUID.fields  :', UUID.fields)
print("Prining each field seperately")
print('UUID.time_low            : ', UUID.time_low)
print('UUID.time_mid            : ', UUID.time_mid)
print('UUID.time_hi_version     : ', UUID.time_hi_version)
print('UUID.clock_seq_hi_variant: ', UUID.clock_seq_hi_variant)
print('UUID.clock_seq_low       : ', UUID.clock_seq_low)
print('UUID.node                : ', UUID.node)
print('UUID.time                : ', UUID.time)
print('UUID.clock_seq           : ', UUID.clock_seq)
print('UUID.SafeUUID           : ', UUID.is_safe)