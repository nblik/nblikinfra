import base64 


contents = open("temp.txt").read().splitlines()

out = open("tempnew.txt","w")
for x in contents:
    obj = x.split(":")
    a = obj[0]
    b = base64.b64encode(obj[1].encode()).decode()
    out.write(a+": "+b)
    out.write("\n")
out.close()