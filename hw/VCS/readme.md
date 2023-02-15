Tyler Workman


Create both branches (test1 and test2) per Problem 2a

    $ git branch test1
    $ git branch test2

Now create/edit test.txt in test1 branch (Problem 2b and 2c)

    $ git checkout test1
    Switched to branch 'test1'
    $cd hw/VCS
    $vim test.txt

The above code creates the test.txt file, and all we need to do is paste our text in and exit with :wq to save and quit the vim editor
  
Now commit to new branch (Problem 2d)

    $ git add test.txt
    $ git commit -m"created test.txt"

Enter test2 and search for test.txt (P 2e)

    $ git checkout test2
    $ ls
test.txt does not appear, as it was a file specifically created in the test1 branch, which is a different development path than test2  

Same as before (P 2f) <br />
   
    $ vim test.txt
    $ git add test.txt
    $ git commit -m"created test.txt"
  
Problem 2G: I don't get an error, though my best guess is that's because I committed the changes to test2 before switching branches  
  
Merge to main (Problem 2H) <br />
  
    $ git checkout main
    $ git merge test1
  
Content of main? (P 2I) <br />
    
    readme.md test.txt
  
What error if trying to merge test2? (2J) <br />
    
    CONFLICT (add/add): Merge conflict in hw/VCS/test.txt
    Auto-merging hw/VCS/test.txt
    Automatic merge failed; fix conflicts and then commit the result.
  
What error if checking out into test2? (2K) <br />
    
    hw/VCS/test.txt: needs merge
    error: you need to resolve your current index first
  
What is the source of the error, according to git status? (2L) <br />
The error appears to be caused by the fact that both merging branches are attempting to add a file with the same name, and so the system doesn't know which to resolve first.  
  
What error do you get for trying to delete test1 branch? (2O) <br />
    
    error: The branch 'test1' is not fully merged.
    If you are sure you want to delete it, run 'git branch -D test1'.
  
What message do you get after switching to your main branch instead? What branches are left? (2P) <br />
    
    Deleted branch test1 (was 42c2a87).
    *main
    test2
  
Why wasn't there an error message when deleting from the main branch? (2Q) <br />
  Because the error preventing it from occurring on test2 was because the two branches hadn't been merged yet. The main branch had already  
merged with test1 and test2, so that error did not exist.
  
What error do you get if you try to delete the test2 branch while inside of test2? (2R) <br />
    
    error: Cannot delete branch 'test2' checked out at '/Users/tlw8878/Jupyter Notebooks/MMP23S'
  
List the branches after deleting test2 from main branch (2S) <br />
    
    *main
  
