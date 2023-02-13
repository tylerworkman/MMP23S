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

Same as before (P 2f)
    $ vim test.txt
    $ git add test.txt
    $ git commit -m"created test.txt"
  
Problem 2G: I don't get an error, though my best guess is that's because I committed the changes to test2 before switching branches  
  
Merge to main (Problem 2H)
    $ git checkout main
    $ git merge test1
