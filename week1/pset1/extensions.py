#1 ask user for file name
#2 classify them based on extensions
#3 if  no extensions or other than given ones output should be application/extension name
#4 if no extension then output should be application/octet-stream

user=input("Enter file name:")
user=user.strip().lower()

if user.endswith(".gif"):
    print("image/gif")
elif user.endswith(".jpg"):
    print("image/jpeg")
elif user.endswith(".jpeg"):
    print("image/jpeg")
elif user.endswith(".png"):
    print("image/png")
elif user.endswith(".txt"):
    print("text/plain")
elif user.endswith(".zip"):
    print("application/zip")
elif user.endswith(".pdf"):
    print("application/pdf")
else:
    print("application/octet-stream")
