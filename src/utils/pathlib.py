from pathlib import Path 

conf = Path() 

# for i in conf.glob(' '): 
#     print( i)
# # print(conf) 

# if conf.exists(): 
#     print(f"yess !!! {conf}") 
# else : 
#     print("no such file in current directory") 


from databricks.sdk import WorkspaceClient 


w = WorkspaceClient()

# files = w.dbutils.fs.ls("/Workspace/Users")
# count = 0
# li = {}
# for f in range(0, len(files)) : 
#     count += 1
#     li[f] = files[f].path

# print(count) 
# print(li)