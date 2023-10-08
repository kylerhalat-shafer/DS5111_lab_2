# DS5111_lab_2
What did you have to do for the make to work? --> sudo apt update 

Similarly for python3 -m venv env, what did you have to do? (How likely are you to have guessed that without their clear error message?) --> I had to download miniconda a different time which enabled it to work this time. I remember the messages being very clear on what to do and not to do, plus looking online.

Both the pip install on the requirements.txt, and the call to run bin/clockdeco_param.py should be activating the virtual environment first. In other words, there are two bash commands separated by a ;, the first of which activates. Why can't we just do that on a separate line? In other words, why do we have to do that in one line and separate the commands with a ; --> They need to run at the same time because 
If you activate the virtual environment in one command and then try to run a command in the next line of the Makefile recipe, that next command won't recognize the activated environment because it'll be running in a separate shell that isn't aware of the changes made in the previous command.

As it is, both the env and tests jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job run? What would happen if you accidentaly had a file called run in your directory? What can we do to fix this? --> If such a file  or a directory exists and doesn't have any dependencies that are newer than it, then make will consider the target up to date and won't execute the associated recipe.

The code provided to you for the test file starts with two lines, seemingly to append something to sys.path. What is the purpose of these lines? --> The purpose of these lines is to add a directory to the Python import path, which determines where the Python interpreter looks for modules to import.
