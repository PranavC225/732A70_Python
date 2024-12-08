# 732A70_Python
## 732A70 - Introduction to Python course labs
### To create a environment using venv
- Goto the directory where you want the virtual environment
- ```python -m venv .732A70```
- to activate the environment on Windows: ```.\env\Scripts\activate```
- to ensure that the environment is used in the ipynb kernel
  - click on kernel on top right square in the notebook
  - select something like this ".732A70 (Python 3.x.xx)"
- in the notebook run the cell ```!where python``` and it should output
  - path_to_your_directory/.732A70/Scripts/python.exe

If everything is good, python environment is set and ready to use in notebook

### To use the repo
1. Open the folder where you want to clone the repository
2. Open terminal on that location and run these:
   1. ```git clone https://github.com/PranavC225/732A70_Python.git```
   2. ```git config user.name your_github_user_name```
   3. ```git config user.email your_email_id```
4. You are good to edit and modify the files

### Good to remember before making changes to files on a version control system such as github
1. ```git pull``` before any edits is a lifesaver to avoid merge conflicts 99% of the time
2. ```git checkout main``` to ensure you are on correct branch before making any edits
3. ```git status``` to check for any unstaged but modified files, will show how many files were modified, created in red
4. ```git add .``` to stage all the modified files/```git add file_name``` to stage a single file. Do a ```git status``` to check if the file/s were staged or not. If all is good then the changes would be shown in green
5. Try to commit small but frequent changes with messages:```git commit -m "This is my first commit"```
6. ```git push``` to FINALLY push all the commits at the same time
