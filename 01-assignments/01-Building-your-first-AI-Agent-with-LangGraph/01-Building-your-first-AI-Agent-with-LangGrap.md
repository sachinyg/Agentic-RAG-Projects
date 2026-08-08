PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> New-Item 01-Building-your-first-AI-Agent-with-LangGrap.md -ItemType File                                                                                           


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                                                 
----                 -------------         ------ ----                                                                                                                                                                                                                                 
-a----        08-08-2026     18:00              0 01-Building-your-first-AI-Agent-with-LangGrap.md                                                                                                                                                                                     


PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph>

(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> deactivate
PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> python -m venv .venv                                                                                                                                               
PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> .\.venv\Scripts\Activate.ps1
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> python -c "import sys; print(sys.executable)"
C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph\.venv\Scripts\python.exe
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> code .
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> python -m pip install python-dotenv
Collecting python-dotenv
  Using cached python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
Using cached python_dotenv-1.2.2-py3-none-any.whl (22 kB)
Installing collected packages: python-dotenv
Successfully installed python-dotenv-1.2.2

[notice] A new release of pip is available: 24.0 -> 26.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in c:\dev\agentic-rag-projects\01-assignments\01-building-your-first-ai-agent-with-langgraph\.venv\lib\site-packages (24.0)
Collecting pip
  Downloading pip-26.2.1-py3-none-any.whl.metadata (4.6 kB)
Downloading pip-26.2.1-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 11.5 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.0
    Uninstalling pip-24.0:
      Successfully uninstalled pip-24.0
Successfully installed pip-26.2.1
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> 
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> 
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> python -m pip freeze > requirements.txt
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> mkdir notebooks


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                                                 
----                 -------------         ------ ----                                                                                                                                                                                                                                 
d-----        08-08-2026     20:43                notebooks                                                                                                                                                                                                                            


(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> mkdir src


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                                                 
----                 -------------         ------ ----                                                                                                                                                                                                                                 
d-----        08-08-2026     20:43                src                                                                                                                                                                                                                                  


(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> mkdir data


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                                                 
----                 -------------         ------ ----                                                                                                                                                                                                                                 
d-----        08-08-2026     20:43                data                                                                                                                                                                                                                                 


(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> dir


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                                                 
----                 -------------         ------ ----                                                                                                                                                                                                                                 
d-----        08-08-2026     20:33                .venv                                                                                                                                                                                                                                
d-----        08-08-2026     20:43                data                                                                                                                                                                                                                                 
d-----        08-08-2026     20:43                notebooks                                                                                                                                                                                                                            
d-----        08-08-2026     20:43                src                                                                                                                                                                                                                                  
-a----        08-08-2026     18:01           1317 01-Building-your-first-AI-Agent-with-LangGrap.md                                                                                                                                                                                     
-a----        08-08-2026     20:38             46 requirements.txt                                                                                                                                                                                                                     


(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> Get-ChildItem .\notebooks


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph\notebooks


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                                                 
----                 -------------         ------ ----                                                                                                                                                                                                                                 
-a----        15-04-2026     15:16          21146 Building Stateful Applications.ipynb                                                                                                                                                                                                 
-a----        15-04-2026     15:16          54965 Building_a_Research_Assistant_in_LangGraph.ipynb                                                                                                                                                                                     
-a----        15-04-2026     15:16          74238 Simple_RAG_Agent_with_LangGraph.ipynb                                                                                                                                                                                                


(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph>


notebooks\
    ↓ experimentation / learning

src\
    ↓ reusable Python code

tests\
    ↓ automated testing

data\
    ↓ documents used by RAG

.env
    ↓ credentials



(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> git status --untracked-files=all
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        01-Building-your-first-AI-Agent-with-LangGrap.md
        notebooks/Building Stateful Applications.ipynb
        notebooks/Building_a_Research_Assistant_in_LangGraph.ipynb
        notebooks/Simple_RAG_Agent_with_LangGraph.ipynb
        requirements.txt

nothing added to commit but untracked files present (use "git add" to track)
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> 


2. Install VS Code Jupyter extension

In VS Code press:

Ctrl + Shift + X

Search for:

Jupyter

Install the extension published by:

Microsoft

You should already have the Microsoft Python extension as well in VS Code.

3. Install ipykernel inside this .venv

This is the important part.

With (.venv) active, run:

python -m pip install ipykernel

I also recommend upgrading pip first if you haven't done so:

python -m pip install --upgrade pip

Then:

python -m pip install ipykernel

Verify:

python -m pip show ipykernel

The Location: should point somewhere underneath your project .venv.

(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> python --version
Python 3.11.9
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> python -c "import sys; print(sys.executable)"
C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph\.venv\Scripts\python.exe
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> python -m pip install --upgrade pip
Requirement already satisfied: pip in .\.venv\Lib\site-packages (26.2.1)
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> python -m pip install ipykernel
Collecting ipykernel
  Downloading ipykernel-7.3.0-py3-none-any.whl.metadata (4.5 kB)
Collecting comm>=0.1.1 (from ipykernel)
  Downloading comm-0.2.3-py3-none-any.whl.metadata (3.7 kB)
Collecting debugpy>=1.6.5 (from ipykernel)
  Downloading debugpy-1.8.21-cp311-cp311-win_amd64.whl.metadata (1.5 kB)
Collecting ipython>=7.23.1 (from ipykernel)
  Downloading ipython-9.16.1-py3-none-any.whl.metadata (4.6 kB)
Collecting jupyter-client>=8.9.0 (from ipykernel)
  Downloading jupyter_client-8.9.1-py3-none-any.whl.metadata (8.5 kB)
Collecting jupyter-core!=6.0.*,>=5.1 (from ipykernel)
  Downloading jupyter_core-5.9.1-py3-none-any.whl.metadata (1.5 kB)
Collecting matplotlib-inline>=0.1 (from ipykernel)
  Downloading matplotlib_inline-0.2.2-py3-none-any.whl.metadata (2.4 kB)
Collecting nest-asyncio2>=1.7.0 (from ipykernel)
  Downloading nest_asyncio2-1.7.2-py3-none-any.whl.metadata (6.3 kB)
Collecting packaging>=22 (from ipykernel)
  Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting psutil>=5.7 (from ipykernel)
  Downloading psutil-7.2.2-cp37-abi3-win_amd64.whl.metadata (22 kB)
Collecting pyzmq>=25 (from ipykernel)
  Downloading pyzmq-27.1.0-cp311-cp311-win_amd64.whl.metadata (6.0 kB)
Collecting tornado>=6.4.1 (from ipykernel)
  Downloading tornado-6.5.8-cp39-abi3-win_amd64.whl.metadata (2.9 kB)
Collecting traitlets>=5.4.0 (from ipykernel)
  Downloading traitlets-5.16.1-py3-none-any.whl.metadata (10 kB)
Collecting colorama>=0.4.4 (from ipython>=7.23.1->ipykernel)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting ipython-pygments-lexers>=1.0.0 (from ipython>=7.23.1->ipykernel)
  Downloading ipython_pygments_lexers-1.1.1-py3-none-any.whl.metadata (1.1 kB)
Collecting jedi>=0.18.2 (from ipython>=7.23.1->ipykernel)
  Downloading jedi-0.20.0-py2.py3-none-any.whl.metadata (23 kB)
Collecting prompt_toolkit<3.1.0,>=3.0.41 (from ipython>=7.23.1->ipykernel)
  Downloading prompt_toolkit-3.0.53-py3-none-any.whl.metadata (6.4 kB)
Collecting pygments>=2.14.0 (from ipython>=7.23.1->ipykernel)
  Downloading pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
Collecting stack_data>=0.6.0 (from ipython>=7.23.1->ipykernel)
  Downloading stack_data-0.6.3-py3-none-any.whl.metadata (18 kB)
Collecting typing_extensions>=4.6 (from ipython>=7.23.1->ipykernel)
  Using cached typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Collecting wcwidth>=0.1.4 (from prompt_toolkit<3.1.0,>=3.0.41->ipython>=7.23.1->ipykernel)
  Downloading wcwidth-0.8.2-py3-none-any.whl.metadata (43 kB)
Collecting parso<0.9.0,>=0.8.6 (from jedi>=0.18.2->ipython>=7.23.1->ipykernel)
  Downloading parso-0.8.7-py2.py3-none-any.whl.metadata (8.2 kB)
Collecting python-dateutil>=2.8.2 (from jupyter-client>=8.9.0->ipykernel)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting platformdirs>=2.5 (from jupyter-core!=6.0.*,>=5.1->ipykernel)
  Downloading platformdirs-4.11.1-py3-none-any.whl.metadata (5.5 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->jupyter-client>=8.9.0->ipykernel)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting executing>=1.2.0 (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel)
  Downloading executing-2.2.1-py2.py3-none-any.whl.metadata (8.9 kB)
Collecting asttokens>=2.1.0 (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel)
  Downloading asttokens-3.0.2-py3-none-any.whl.metadata (5.7 kB)
Collecting pure-eval (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel)
  Downloading pure_eval-0.2.3-py3-none-any.whl.metadata (6.3 kB)
Downloading ipykernel-7.3.0-py3-none-any.whl (120 kB)
Downloading comm-0.2.3-py3-none-any.whl (7.3 kB)
Downloading debugpy-1.8.21-cp311-cp311-win_amd64.whl (5.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.3/5.3 MB 17.8 MB/s  0:00:00
Downloading ipython-9.16.1-py3-none-any.whl (625 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 626.0/626.0 kB 24.3 MB/s  0:00:00
Downloading prompt_toolkit-3.0.53-py3-none-any.whl (392 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading ipython_pygments_lexers-1.1.1-py3-none-any.whl (8.1 kB)
Downloading jedi-0.20.0-py2.py3-none-any.whl (4.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 MB 19.7 MB/s  0:00:00
Downloading parso-0.8.7-py2.py3-none-any.whl (107 kB)
Downloading jupyter_client-8.9.1-py3-none-any.whl (109 kB)
Downloading jupyter_core-5.9.1-py3-none-any.whl (29 kB)
Downloading matplotlib_inline-0.2.2-py3-none-any.whl (9.5 kB)
Downloading nest_asyncio2-1.7.2-py3-none-any.whl (7.8 kB)
Downloading packaging-26.3-py3-none-any.whl (129 kB)
Downloading platformdirs-4.11.1-py3-none-any.whl (23 kB)
Downloading psutil-7.2.2-cp37-abi3-win_amd64.whl (137 kB)
Downloading pygments-2.20.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 20.6 MB/s  0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading pyzmq-27.1.0-cp311-cp311-win_amd64.whl (633 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 633.4/633.4 kB 24.8 MB/s  0:00:00
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading stack_data-0.6.3-py3-none-any.whl (24 kB)
Downloading asttokens-3.0.2-py3-none-any.whl (28 kB)
Downloading executing-2.2.1-py2.py3-none-any.whl (28 kB)
Downloading tornado-6.5.8-cp39-abi3-win_amd64.whl (452 kB)
Downloading traitlets-5.16.1-py3-none-any.whl (86 kB)
Using cached typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Downloading wcwidth-0.8.2-py3-none-any.whl (323 kB)
Downloading pure_eval-0.2.3-py3-none-any.whl (11 kB)
Installing collected packages: pure-eval, wcwidth, typing_extensions, traitlets, tornado, six, pyzmq, pygments, psutil, platformdirs, parso, packaging, nest-asyncio2, executing, debugpy, comm, colorama, asttokens, stack_data, python-dateutil, prompt_toolkit, matplotlib-inline, jupyter-core, jedi, ipython-pygments-lexers, jupyter-client, ipython, ipykernel
Successfully installed asttokens-3.0.2 colorama-0.4.6 comm-0.2.3 debugpy-1.8.21 executing-2.2.1 ipykernel-7.3.0 ipython-9.16.1 ipython-pygments-lexers-1.1.1 jedi-0.20.0 jupyter-client-8.9.1 jupyter-core-5.9.1 matplotlib-inline-0.2.2 nest-asyncio2-1.7.2 packaging-26.3 parso-0.8.7 platformdirs-4.11.1 prompt_toolkit-3.0.53 psutil-7.2.2 pure-eval-0.2.3 pygments-2.20.0 python-dateutil-2.9.0.post0 pyzmq-27.1.0 six-1.17.0 stack_data-0.6.3 tornado-6.5.8 traitlets-5.16.1 typing_extensions-4.16.0 wcwidth-0.8.2
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> python -m pip show ipykernel
Name: ipykernel
Version: 7.3.0
Summary: IPython Kernel for Jupyter
Home-page: https://ipython.org
Author: 
Author-email: IPython Development Team <ipython-dev@scipy.org>
License-Expression: BSD-3-Clause
Location: C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph\.venv\Lib\site-packages
Requires: comm, debugpy, ipython, jupyter-client, jupyter-core, matplotlib-inline, nest-asyncio2, packaging, psutil, pyzmq, tornado, traitlets
Required-by: 
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> 

4. Register the environment as a Jupyter kernel

Technically VS Code can often discover .venv automatically, but I recommend registering it explicitly because we'll have many environments later.

Run:

python -m ipykernel install --user --name agentic-rag-langgraph --display-name "Python 3.12 - Agentic RAG LangGraph"

Assuming your .venv uses Python 3.12.

This gives the kernel a human-friendly name:

Python 3.12 - Agentic RAG LangGraph

Much easier than choosing between a forest of nearly identical Python 3.x.x entries later. 🌲🐍

(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> python -m ipykernel install --user --name agentic-rag-langgraph --display-name "Python 3.11.9 - Agentic RAG LangGraph"
Installed kernelspec agentic-rag-langgraph in C:\Users\Sachin Y Gaydhani\AppData\Roaming\jupyter\kernels\agentic-rag-langgraph
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> New-Item .env -ItemType File


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                              
----                 -------------         ------ ----                                                                                                                                                                                                              
-a----        08-08-2026     21:17              0 .env                                                                                                                                                                                                              


(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> New-Item .env.example -ItemType File


    Directory: C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph


Mode                 LastWriteTime         Length Name                                                                                                                                                                                                              
----                 -------------         ------ ----                                                                                                                                                                                                              
-a----        08-08-2026     21:17              0 .env.example                                                                                                                                                                                                      


(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> git check-ignore -v .env
.gitignore:185:.env     .env
(.venv) PS C:\Dev\Agentic-RAG-Projects\01-assignments\01-Building-your-first-AI-Agent-with-LangGraph> 