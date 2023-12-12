import os

os.system("aws s3 ls s3://adroll-b2b-data/user-attributes-offload-parquet/ | tee ~/testing/s3-delete.txt")

s3_prifix="s3://adroll-b2b-data/user-attributes-offload-parquet/"

ofile = open("output.txt", "w")
with open("s3-delete.txt", "r") as file:
    for line in file.readlines():
        # output = s3_prifix + str(line.split()[3]) + "\n"
        # ofile.write(output)
        tmp = line.split()
        if str(tmp[0]) == "PRE":
            output = s3_prifix + str(tmp[1]) + "\n"
            print(output)
            ofile.write(output)

ofile.close()

# os.system("cat ./testing/output.txt | xargs -L1 -P8 aws s3 rm --recursive")