file=open(r"E:\桌面\研一\！\化镀仿真资料镍\化镀仿真资料\2.txt","w")

i=304
while i<=573:
    file.write(str(i))
    file.write(",")
    i+=2
file.close()