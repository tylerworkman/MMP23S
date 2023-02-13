Tyler Workman


Create both branches (test1 and test2) per Problem 2a

'''bash
$ git branch test1
$ git branch test2
'''

Now create/edit test.txt in test1 branch (Problem 2b and 2c)

'''bash
$ git checkout test1
Switched to branch 'test1'
$cd hw/VCS
$vim test.txt
'''

The above code creates the test.txt file, and all we need to do is paste our text in and exit with :wq to save and quit the vim editor

Now commit to new branch (Problem 2d)

'''bash
$ git add test.txt
$ git commit -m"created test.txt"
'''
