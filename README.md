# This is wx sample labtest 
![alt image](https://github.com/weixiang67/sample_labtest/blob/main/cat.png?raw=true)

# Git Notes

## 1. Image Syntax
1. To add images the syntax is:
   ![]()

---

## 2. Remote Commands
1. Git remote add origin <link>
2. Git remote -v
3. Git remote set-url origin <link>
4. Git push --set-upstream origin master

---

## 3. Basic Git Commands
1. Git add
2. Git commit -m "message"
3. Git push
4. Git restore --staged <file>   # to unstage
5. Git diff   # to check changes

---

## 4. Branch
1. Git branch   # check which branch you are on
2. Git branch bug-fix1   # create new branch (no spaces)
3. Git checkout bug-fix1   # switch to bug-fix1
4. Git branch   # now you will see two branches
5. After finishing edits:
   - Git add
   - Git commit -m "message"
6. Git checkout master   # back to main branch
7. Git merge bug-fix1    # merge the branch

---

## 5. Image Upload Workflow
1. Upload files to Git
2. Git pull origin master
3. Edit the code
4. Git add
5. Git commit -m "added image"
6. Git push -u origin master

---

## 6. Tags
1. Git tag -a v1.0 -m "initial version v1.0"
2. Git push origin v1.0

---

## 7. Submodules
1. Git submodule add <link>
2. Git status
3. Git add
4. Git commit -m "added submodule"
5. Git push -u origin
