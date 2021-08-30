import uuid

def random_string(string_length):
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")

    return random[0:string_length]

loop = True
while loop:
    length = int(input("Enter String Length or '0' to exit : "))
    if(length <= 0):
        break
    print(random_string(length))