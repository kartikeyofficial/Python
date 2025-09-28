def file_size(fname):
    import os
    statinfo = os.stat(fname)
    return statinfo.st_size
print("File Size In bytes Of a Plain File:",file_size("karthik.txt"))
