import os
from dotenv import load_dotenv

load_dotenv()

course_name = os.getenv("COURSE_NAME")
project_owner = os.getenv("PROJECT_OWNER")
environment = os.getenv("ENVIRONMENT")

print(f"Course      : {course_name}")
print(f"Owner       : {project_owner}")
print(f"Environment : {environment}")