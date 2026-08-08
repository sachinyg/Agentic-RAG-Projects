1. ✅ Python checked
2. ⬜ Install Git
3. ⬜ Configure Git identity
4. ⬜ Sign VS Code into GitHub
5. ⬜ Confirm GitHub security / 2FA
6. ⬜ Create PRIVATE GitHub repository
7. ⬜ Create C:\Dev\Agentic-RAG-Analytics-Vidhya
8. ⬜ Create our folder structure
9. ⬜ Create .gitignore
10. ⬜ Initialize/connect Git
11. ⬜ Create first Python virtual environment
12. ⬜ Test .env

=================================================================================================

Your setup will eventually look like this:

Windows
│
├── Python 3.11.9
│   └── C:\Users\Sachin Y Gaydhani\
│       AppData\Local\Python\pythoncore-3.11-64\
│
├── Git for Windows
│
└── C:\Dev\
    └── Agentic-RAG-Analytics-Vidhya\
        │
        ├── .git\
        ├── .gitignore
        │
        ├── 00-course-notes\
        ├── 01-assignments\
        ├── 02-mini-projects\
        ├── 03-real-world-projects\
        ├── 04-experiments\
        ├── 05-shared-resources\
        └── 90-scratch\

=================================================================================================
Individual projects will then get environments such as:
02-mini-projects\
└── basic-rag\
    ├── .venv\
    ├── .env
    ├── .env.example
    ├── requirements.txt
    └── src\

=================================================================================================

The .venv will use your installed Python 3.11.9, but its packages will remain isolated from other projects.

=================================================================================================

PS C:\Users\Sachin Y Gaydhani> python --version
Python 3.11.9
PS C:\Users\Sachin Y Gaydhani> python -c "import sys; print(sys.executable)"
C:\Users\Sachin Y Gaydhani\AppData\Local\Python\pythoncore-3.11-64\python.exe
PS C:\Users\Sachin Y Gaydhani> py list
Python install manager was successfully updated to 26.3.

Additional shebang configuration is now available. Please see
https://docs.python.org/using/windows#shebang-lines for more information.

Tag           Name           Managed By  Version  Alias                                
3.11[-64]  *  Python 3.11.9  PythonCore  3.11.9   python3[-64].exe, python3.11[-64].exe
PS C:\Users\Sachin Y Gaydhani> git --version
git : The term 'git' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the 
path is correct and try again.
At line:1 char:1
+ git --version
+ ~~~
    + CategoryInfo          : ObjectNotFound: (git:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS C:\Users\Sachin Y Gaydhani> git config --global --list
git : The term 'git' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the 
path is correct and try again.
At line:1 char:1
+ git config --global --list
+ ~~~
    + CategoryInfo          : ObjectNotFound: (git:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 

=================================================================================================
 Python 3.11.9
 C:\Users\Sachin Y Gaydhani\AppData\Local\Python\pythoncore-3.11-64\python.exe
=================================================================================================

=================================================================================================
 winget install --id Git.Git -e --source winget
=================================================================================================

 This is the command currently recommended by the official Git for Windows site. The current Git for Windows release is 2.55.0 as of July 14, 2026.

Then close VS Code completely and reopen it. This matters because VS Code needs to pick up the updated Windows

Then open a fresh terminal and run:

=================================================================================================
git --version
=================================================================================================

PS C:\Users\Sachin Y Gaydhani> winget install --id Git.Git -e --source winget
Found Git [Git.Git] Version 2.55.0.3
This application is licensed to you by its owner.
Microsoft is not responsible for, nor does it grant any licenses to, third-party packages.
Downloading https://github.com/git-for-windows/git/releases/download/v2.55.0.windows.3/Git-2.55.0.3-64-bit.exe
  ██████████████████████████████  62.3 MB / 62.3 MB
Successfully verified installer hash
Starting package install...
The installer will request to run as administrator. Expect a prompt.
Successfully installed
PS C:\Users\Sachin Y Gaydhani> 

==================================================================================================
If you do not close VS Code and Reopen you might get

PS C:\Users\Sachin Y Gaydhani> git --version
git : The term 'git' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the 
path is correct and try again.
At line:1 char:1
+ git --version
+ ~~~
    + CategoryInfo          : ObjectNotFound: (git:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS C:\Users\Sachin Y Gaydhani> 
==================================================================================================

PS C:\Users\Sachin Y Gaydhani> git --version
git version 2.55.0.windows.3
PS C:\Users\Sachin Y Gaydhani> git config --global user.name "sachinyg"
PS C:\Users\Sachin Y Gaydhani> git config --global user.email "69243284+sachinyg@users.noreply.github.com"
PS C:\Users\Sachin Y Gaydhani> git config --global --list
user.name=sachinyg
user.email=69243284+sachinyg@users.noreply.github.com
PS C:\Users\Sachin Y Gaydhani> git config --global user.name "sachinyg"
PS C:\Users\Sachin Y Gaydhani> git config --global --list              
user.name=sachinyg
user.email=69243284+sachinyg@users.noreply.github.com
PS C:\Users\Sachin Y Gaydhani> 

==================================================================================================

We can also install Microsoft's GitHub Pull Requests and Issues extension later, although it isn't required merely to push and pull code.

git config --global user.email 69243284+sachinyg@users.noreply.github.com

==================================================================================================

PS C:\Users\Sachin Y Gaydhani> git config --global --get user.name       
sachinyg
PS C:\Users\Sachin Y Gaydhani> git config --global --get user.email
69243284+sachinyg@users.noreply.github.com
PS C:\Users\Sachin Y Gaydhani> 
==================================================================================================

Step 1: Sign VS Code into GitHub

In VS Code, install Microsoft's GitHub Pull Requests extension if you don't already have it.
Sign in
---------------------------------------------------------------------------------------------------
Step 2: Create the private GitHub repository
Agentic-RAG-Projects

==================================================================================================
First Assignment - Create Virtual Environment
==================================================================================================

PS C:\Dev\Agentic-RAG-Projects> git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
PS C:\Dev\Agentic-RAG-Projects> mkdir 00-course-notes


    Directory: C:\Dev\Agentic-RAG-Projects


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                         
----                 -------------         ------ ----                                                                                                                                                                                                         
d-----        08-08-2026     13:38                00-course-notes                                                                                                                                                                                              


PS C:\Dev\Agentic-RAG-Projects> mkdir 01-assignments


    Directory: C:\Dev\Agentic-RAG-Projects


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                         
----                 -------------         ------ ----                                                                                                                                                                                                         
d-----        08-08-2026     13:39                01-assignments                                                                                                                                                                                               


PS C:\Dev\Agentic-RAG-Projects> mkdir 02-mini-projects


    Directory: C:\Dev\Agentic-RAG-Projects


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                         
----                 -------------         ------ ----                                                                                                                                                                                                         
d-----        08-08-2026     13:39                02-mini-projects                                                                                                                                                                                             


PS C:\Dev\Agentic-RAG-Projects> mkdir 03-real-world-projects


    Directory: C:\Dev\Agentic-RAG-Projects


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                         
----                 -------------         ------ ----                                                                                                                                                                                                         
d-----        08-08-2026     13:39                03-real-world-projects                                                                                                                                                                                       


PS C:\Dev\Agentic-RAG-Projects> mkdir 04-experiments


    Directory: C:\Dev\Agentic-RAG-Projects


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                         
----                 -------------         ------ ----                                                                                                                                                                                                         
d-----        08-08-2026     13:39                04-experiments                                                                                                                                                                                               


PS C:\Dev\Agentic-RAG-Projects> mkdir 05-shared-resources


    Directory: C:\Dev\Agentic-RAG-Projects


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                         
----                 -------------         ------ ----                                                                                                                                                                                                         
d-----        08-08-2026     13:39                05-shared-resources                                                                                                                                                                                          


PS C:\Dev\Agentic-RAG-Projects> mkdir 90-scratch


    Directory: C:\Dev\Agentic-RAG-Projects


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                         
----                 -------------         ------ ----                                                                                                                                                                                                         
d-----        08-08-2026     13:39                90-scratch                                                                                                                                                                                                   


PS C:\Dev\Agentic-RAG-Projects> dir


    Directory: C:\Dev\Agentic-RAG-Projects


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                         
----                 -------------         ------ ----                                                                                                                                                                                                         
d-----        08-08-2026     13:38                00-course-notes                                                                                                                                                                                              
d-----        08-08-2026     13:39                01-assignments                                                                                                                                                                                               
d-----        08-08-2026     13:39                02-mini-projects                                                                                                                                                                                             
d-----        08-08-2026     13:39                03-real-world-projects                                                                                                                                                                                       
d-----        08-08-2026     13:39                04-experiments                                                                                                                                                                                               
d-----        08-08-2026     13:39                05-shared-resources                                                                                                                                                                                          
d-----        08-08-2026     13:39                90-scratch                                                                                                                                                                                                   
-a----        08-08-2026     13:21           5183 .gitignore                                                                                                                                                                                                   
-a----        08-08-2026     13:21             96 README.md                                                                                                                                                                                                    


PS C:\Dev\Agentic-RAG-Projects> mkdir 01-assignments\00-environment-setup


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                         
----                 -------------         ------ ----                                                                                                                                                                                                         
d-----        08-08-2026     13:41                00-environment-setup                                                                                                                                                                                         


PS C:\Dev\Agentic-RAG-Projects> cd 01-assignments\00-environment-setup
PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> mkdir src


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                         
----                 -------------         ------ ----                                                                                                                                                                                                         
d-----        08-08-2026     13:41                src                                                                                                                                                                                                          


PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> python -m venv .venv
PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> dir


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                         
----                 -------------         ------ ----                                                                                                                                                                                                         
d-----        08-08-2026     13:41                .venv                                                                                                                                                                                                        
d-----        08-08-2026     13:41                src                                                                                                                                                                                                          


PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> .\.venv\Scripts\Activate.ps1
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> python --version
Python 3.11.9
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> python -c "import sys; print(sys.executable)"
C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup\.venv\Scripts\python.exe
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup>


Conceptually:

Windows Python 3.11.9
        │
        └── creates
             │
             ▼
00-environment-setup\.venv
             │
             ├── its own Python
             └── its own packages


Step -  Tell VS Code to use this interpreter

Press:

Ctrl + Shift + P

Search:

Python: Select Interpreter

Select the interpreter containing:

00-environment-setup\.venv\Scripts\python.exe

Then press:

Ctrl + Shift + P

and search for:

Python: Select Interpreter

not Python Environments:.

Choose:

Enter interpreter path...

then browse to:

C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup\.venv\Scripts\python.exe
==========================================================================================

1. Install python-dotenv

Run:

python -m pip install python-dotenv

Then verify:

python -m pip show python-dotenv

(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> python -m pip install python-dotenv
Collecting python-dotenv
  Using cached python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
Using cached python_dotenv-1.2.2-py3-none-any.whl (22 kB)
Installing collected packages: python-dotenv
Successfully installed python-dotenv-1.2.2

[notice] A new release of pip is available: 24.0 -> 26.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> python -m pip show python-dotenv
Name: python-dotenv
Version: 1.2.2
Summary: Read key-value pairs from a .env file and set them as environment variables
Home-page: 
Author: 
Author-email: Saurabh Kumar <me+github@saurabh-kumar.com>
License: BSD-3-Clause
Location: C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup\.venv\Lib\site-packages
Requires: 
Required-by: 
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> 

2. Create requirements.txt
Run:

python -m pip freeze > requirements.txt

Check it:

Get-Content requirements.txt

You should see something like:

python-dotenv==...

.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> python -m pip freeze > requirements.txt
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> Get-Content requirements.txt
python-dotenv==1.2.2
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> 

3. Create .env

From the current folder:

New-Item .env -ItemType File

Open .env in VS Code and put:

COURSE_NAME=Agentic RAG
PROJECT_OWNER=sachinyg
ENVIRONMENT=development

No actual API keys yet.

==================================================================================================
Futur Projects
Agentic-RAG-Projects
│
├── 01-assignments
│   ├── 00-environment-setup
│   │   ├── .env
│   │   └── .venv
│   │
│   └── future-assignment
│       ├── .env
│       └── .venv
│
├── 02-mini-projects
│   └── some-rag-project
│       ├── .env
│       └── .venv
│
└── 03-real-world-projects
    └── some-agentic-rag-app
        ├── .env
        └── .venv



=========================================================================================================

(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> New-Item .env -ItemType File


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                                                                  
----                 -------------         ------ ----                                                                                                                                                                                                                                                  
-a----        08-08-2026     14:04              0 .env                                                                                                                                                                                                                                                  


(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> dir


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                                                                  
----                 -------------         ------ ----                                                                                                                                                                                                                                                  
d-----        08-08-2026     13:41                .venv                                                                                                                                                                                                                                                 
d-----        08-08-2026     13:41                src                                                                                                                                                                                                                                                   
-a----        08-08-2026     14:12             72 .env                                                                                                                                                                                                                                                  
-a----        08-08-2026     14:02             46 requirements.txt                                                                                                                                                                                                                                      


(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> New-Item src -ItemType Directory -Force


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                                                                  
----                 -------------         ------ ----                                                                                                                                                                                                                                                  
d-----        08-08-2026     13:41                src                                                                                                                                                                                                                                                   


(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> New-Item .\src\test_env.py -ItemType File


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup\src


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                                                                  
----                 -------------         ------ ----                                                                                                                                                                                                                                                  
-a----        08-08-2026     14:13              0 test_env.py                                                                                                                                                                                                                                           


(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> python .\src\test_env.py
Course      : Agentic RAG
Owner       : sachinyg
Environment : development
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> 

===========================================================================================================

6. Most important security check 🔐

Before putting any real API key into .env, run:

git check-ignore -v .env
git check-ignore -v .venv

Both should report that they are being ignored by your root .gitignore.

Then:

git status

You should not see .env or .venv listed for commit.

(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> python .\src\test_env.py
Course      : Agentic RAG
Owner       : sachinyg
Environment : development
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> git check-ignore -v .env
.gitignore:183:.env     .env
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> git check-ignore -v .venv
.gitignore:185:.venv    .venv
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../

nothing added to commit but untracked files present (use "git add" to track)
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> git add
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
hint: Disable this message with "git config set advice.addEmptyPathspec false"
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup> cd ..

(.venv) PS C:\Dev\Agentic-RAG-Projects> git status --untracked-files=all
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        01-assignments/00-environment-setup/requirements.txt
        01-assignments/00-environment-setup/src/test_env.py

===================================================================================================================
(.venv) PS C:\Dev\Agentic-RAG-Projects> git status --untracked-files=all
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        01-assignments/00-environment-setup/requirements.txt
        01-assignments/00-environment-setup/src/test_env.py

nothing added to commit but untracked files present (use "git add" to track)
(.venv) PS C:\Dev\Agentic-RAG-Projects> 
(.venv) PS C:\Dev\Agentic-RAG-Projects> 
(.venv) PS C:\Dev\Agentic-RAG-Projects> 
(.venv) PS C:\Dev\Agentic-RAG-Projects> 
(.venv) PS C:\Dev\Agentic-RAG-Projects> 
(.venv) PS C:\Dev\Agentic-RAG-Projects> Get-ChildItem -Force .\01-assignments\00-environment-setup


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                                                                  
----                 -------------         ------ ----                                                                                                                                                                                                                                                  
d-----        08-08-2026     13:41                .venv                                                                                                                                                                                                                                                 
d-----        08-08-2026     14:13                src                                                                                                                                                                                                                                                   
-a----        08-08-2026     14:12             72 .env                                                                                                                                                                                                                                                  
-a----        08-08-2026     14:02             46 requirements.txt                                                                                                                                                                                                                                      


(.venv) PS C:\Dev\Agentic-RAG-Projects> git check-ignore -v .\01-assignments\00-environment-setup\.env
.gitignore:183:.env     ".\\01-assignments\\00-environment-setup\\.env"
(.venv) PS C:\Dev\Agentic-RAG-Projects> git check-ignore -v .\01-assignments\00-environment-setup\.env
.gitignore:183:.env     ".\\01-assignments\\00-environment-setup\\.env"
(.venv) PS C:\Dev\Agentic-RAG-Projects> git check-ignore -v .\01-assignments\00-environment-setup\.venv
.gitignore:185:.venv    ".\\01-assignments\\00-environment-setup\\.venv"
(.venv) PS C:\Dev\Agentic-RAG-Projects> git check-ignore -v .\01-assignments\00-environment-setup\.env.example
.gitignore:4:!.env.example      ".\\01-assignments\\00-environment-setup\\.env.example"
(.venv) PS C:\Dev\Agentic-RAG-Projects> New-Item .\01-assignments\00-environment-setup\.env.example -ItemType File


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\00-environment-setup


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                                                                  
----                 -------------         ------ ----                                                                                                                                                                                                                                                  
-a----        08-08-2026     14:24              0 .env.example                                                                                                                                                                                                                                          


(.venv) PS C:\Dev\Agentic-RAG-Projects> git status --untracked-files=all
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        01-assignments/00-environment-setup/.env.example
        01-assignments/00-environment-setup/requirements.txt
        01-assignments/00-environment-setup/src/test_env.py

nothing added to commit but untracked files present (use "git add" to track)
(.venv) PS C:\Dev\Agentic-RAG-Projects> git status --untracked-files=all                                          
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        01-assignments/00-environment-setup/.env.example
        01-assignments/00-environment-setup/Agentic_RAG_Environment_Creation_Development.md
        01-assignments/00-environment-setup/requirements.txt
        01-assignments/00-environment-setup/src/test_env.py

nothing added to commit but untracked files present (use "git add" to track)
(.venv) PS C:\Dev\Agentic-RAG-Projects> 
(.venv) PS C:\Dev\Agentic-RAG-Projects> 
(.venv) PS C:\Dev\Agentic-RAG-Projects> git check-ignore -v .\01-assignments\00-environment-setup\.env
.gitignore:183:.env     ".\\01-assignments\\00-environment-setup\\.env"
(.venv) PS C:\Dev\Agentic-RAG-Projects> git check-ignore -v .\01-assignments\00-environment-setup\.venv
.gitignore:185:.venv    ".\\01-assignments\\00-environment-setup\\.venv"
(.venv) PS C:\Dev\Agentic-RAG-Projects> git check-ignore -v .\01-assignments\00-environment-setup\.env.example
.gitignore:4:!.env.example      ".\\01-assignments\\00-environment-setup\\.env.example"
(.venv) PS C:\Dev\Agentic-RAG-Projects> 

=================================================================================

(.venv) PS C:\Dev\Agentic-RAG-Projects> git diff -- .gitignore
(.venv) PS C:\Dev\Agentic-RAG-Projects> git diff -- .gitignore
diff --git a/.gitignore b/.gitignore
index 0e2318b..7ff62f9 100644
--- a/.gitignore
+++ b/.gitignore
@@ -3,6 +3,8 @@
 .env.*
 !.env.example
 
+#env.example will not be ignored
+
 # Python virtual environments
 .venv/
 **/.venv/
(.venv) PS C:\Dev\Agentic-RAG-Projects> 

================================================================================
(.venv) PS C:\Dev\Agentic-RAG-Projects> git status --short
 M .gitignore
?? 01-assignments/
(.venv) PS C:\Dev\Agentic-RAG-Projects> 

================================================================================

(.venv) PS C:\Dev\Agentic-RAG-Projects> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        01-assignments/

no changes added to commit (use "git add" and/or "git commit -a")
(.venv) PS C:\Dev\Agentic-RAG-Projects> git add .
(.venv) PS C:\Dev\Agentic-RAG-Projects> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   .gitignore
        new file:   01-assignments/00-environment-setup/.env.example
        new file:   01-assignments/00-environment-setup/Agentic_RAG_Environment_Creation_Development.md
        new file:   01-assignments/00-environment-setup/requirements.txt
        new file:   01-assignments/00-environment-setup/src/test_env.py

(.venv) PS C:\Dev\Agentic-RAG-Projects> git commit -m "Set up Python environment and dotenv configuration"
[main 8933404] Set up Python environment and dotenv configuration
 5 files changed, 682 insertions(+)
 create mode 100644 01-assignments/00-environment-setup/.env.example
 create mode 100644 01-assignments/00-environment-setup/Agentic_RAG_Environment_Creation_Development.md
 create mode 100644 01-assignments/00-environment-setup/requirements.txt
 create mode 100644 01-assignments/00-environment-setup/src/test_env.py
(.venv) PS C:\Dev\Agentic-RAG-Projects> git push
info: please complete authentication in your browser...
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 16 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (10/10), 5.20 KiB | 1.73 MiB/s, done.
Total 10 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/sachinyg/Agentic-RAG-Projects.git
   98efb2b..8933404  main -> main
(.venv) PS C:\Dev\Agentic-RAG-Projects> 