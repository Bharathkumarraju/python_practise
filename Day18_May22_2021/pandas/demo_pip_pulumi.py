import pulumi_gcp as pgcp

for i  in dir(pgcp):
    print(i)

print("---------------------------")

import pulumi_kubernetes as pk8s
for i in dir(pk8s):
    print(i)