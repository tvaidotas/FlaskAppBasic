# flaskappbasic-forked
QA Tutorial in Forking
Make sure you're logged into your GitHub account

Go to any public repository available. This one for example.

To fork the repository, click on Fork (in the top-right of the page):

This will create a copy of the repository under your account.
You will then be redirected to your account's version of the repository

Click on the green Code button, and copy the SSH URL


Open a Git Bash terminal in the location you want to clone your project into

Run the command git clone [URL], but replace [URL] with the repository URL you copied in the previous step

Change directory to the project you just cloned

Run the following command, to confirm that you have cloned the correct repository: git remote -v.

You should get a similar output for fetch and push, but the URL will be pointing to your repository


Updating forked repository from original
Now you will set up your local project to receive updates from the original repository. This is required, so that when
the owner of the original repository adds new functionality, bug fixes etc., you will be able to get these changes as well.

Open your Bash terminal, in the root directory of your project. You should be able to see that you're on the main branch.

Next, you want to execute git remote -v to make sure that the upstream to the original repository is not set up yet.


In your browser, go to the original git repository and copy the repository URL.

You can do this by clicking on the green Code button and copying the SSH URL:


Execute the following command in your Bash terminal, but replace the [URL] with the one you just copied: git remote add upstream [URL]

Next, you want to check that this has worked, which you can do by executing the git remote -v command.

The output should look similar to this:


Now you will pull the changes from the original repository into yours, which you can do by executing the git fetch upstream command in your Git Bash terminal.

The output will depend on whether there are new changes or not:


You will want to update the main branch, so we will merge the upstream/main into the local origin/main.

You can do this by executing the git merge upstream/[name_of_main_branch command.

Example command: git merge upstream/main

Keep in mind that there may be merge conflicts that you will need to resolve.

If you have resolved the merge conflicts, or if there were none, you should push to update your origin/main (or origin/master) branch.

