import uuid
import subprocess

def create_code_file(code , languages):
    file_name = str(uuid.uuid4()) + " . " + languages
    with open ("miniproject/code/" + file_name , "w") as f:
        f.write(code)
    return file_name


def execute_file (file_name , languages):
    try:
        if languages == "py":
        #python xyz.py
            result = subprocess.run(["python", "miniproject/code/" + file_name] , stdout = subprocess.PIPE)
            if result.returncode != 0:
                return    #for compilation error , the return code is 1
            return result.stdout.decode("utf-8")


    except subprocess.CalledProcessError as e:
        print("Error :" + e)
        return





