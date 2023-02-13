Q1: Name the three generations of VCS. Briefly describe how each paradigm works and a problem that it resolves in the previous generation. 
---
    A1: Local VCS, Centralized VCS, and Distributed VCS. Local VCS is the bare-bones system, where a single user keeps track of development versions on their local system. Centralized VCS is where multiple users access a single central server, which has the advantage over Local VCS in that Centralized can allow for easier collaboration with multiple developers. Distributed VCS is a system where (in addition to a central server), each collaborator has a full copy of the version they pulled from. This has the advantage over Centralized in that it allows users to edit without a connection to the central server **and** it (by its very nature) creates backups on multiple independent pieces of hardware.  
  
Q2: Which VCS generation does git belong to?
---
A2: Git is a prime example of Distributed VCS  
  
Q3: Which of the following Git commands can add all the new and modified-existing files to the staging area?
---
A3:  
    (A) git add -A  
    (D) git add --all  
    (F) git add .  
(I was unsure of the exact nature of the question, but its possible that (G) and/or (I) are correct depending on whether the commands override one another)  
  
Q4:Which of the following Git commands both stages and commits only modified and deleted files but NOT the new files added to the repository since the last commit.  
---
A4: (B) will, though if a string message is appended to (C), that one will as well  
  
Q5: Write down the Git command that lists all Git commands for you  
---
A5: git help
  
  
Q6: Write down the Git command that lists all branches for you.  
---
A6: git branch  
  
Q7: Write down the Git command that creates and checks out a new branch named dev from the current branch.  
---
A7: git checkout -b dev  
  
Q8: Follow Instructions  
---
A8:  

    $ git init temp
    Initialized empty Git repository in /Users/tlw8878/Jupyter Notebooks/temp/temp/.git/
    $ vim README.md
    Tyler Workman
    :wq
    $ git checkout -b dev
    $ vim README.md
    :wq
    $ git add .
    $ git push --all
    $ git checkout master
    $ git merge dev
    $ git branch
    *master
    dev  
  
Q9: Write down the Git command that lists all commits made to the project.  
---
A9: git log
