import django
django.setup()
import uuid
import subprocess
from .models import Submissions

def create_code_file(code , languages):
    file_name = str(uuid.uuid4()) + " . " + languages
    with open ("miniproject/code/" + file_name , "w") as f:
        f.write(code)
    return file_name


def execute_file (file_name , languages,submission_id):
    submission = Submissions.objects.get(pk=submission_id)
    if languages == "py":
    #python xyz.py
        result = subprocess.run(["python", "miniproject/code/" + file_name] , stdout = subprocess.PIPE)
        if result.returncode != 0:
            submission.status ='E'
            submission.save()
            return    #for compilation error , the return code is 1

        submission.output = result.stdout.decode("utf-8")
        print(submission.output)
        submission.status = 'S'
        submission.save()







