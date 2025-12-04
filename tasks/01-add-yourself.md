# Task 01 - Add yourself to the contributors list

In this task you will practise the basic workflow of creating a branch,
editing a file, committing your changes, and opening a pull request. These
are the same steps you will follow when contributing to Mesa.

### Steps

1. **Create an issue (optional but recommended).**

   On the upstream GitHub repository (`abmind-community/contrib-practice`), open a new issue titled “Add `<your username>` to contributors list” describing that you are working on this task. In the Mesa project we create issues for all work; this step helps keep a record of what you’re doing.

2. **Create a new branch.**

   In your local clone, create and switch to a new branch with a descriptive name. For example:

   ```bash
   git checkout -b add-<your-github-username>
   ```

3. **Edit `CONTRIBUTORS.md`.**

   Open the `CONTRIBUTORS.md` file in the repository root and add a Markdown list item with your GitHub username. Follow the format shown in the example in the file. Do not remove or edit any existing entries.

4. **Commit your changes.**

   Stage the file and commit with a meaningful message. A good commit message summarises the change in the first line and, if needed, includes additional context in the following paragraphs. If you created an issue in step 1, reference it in the commit message using the syntax `(#<issue-number>)`.

   ```bash
   git add CONTRIBUTORS.md
   git commit -m "add <your-name> to contributors list (#<issue-number>)"
   ```

5. **Push and open a pull request.**

   Push your branch to your fork:

   ```bash
   git push -u origin add-<your-github-username>
   ```

   The `-u` option in `git push -u origin <branch>` sets the upstream tracking relationship for your local branch to the remote branch you are pushing to. This means future `git pull` and `git push` commands (without extra arguments) will automatically apply to this branch and its remote counterpart, making it easier to sync changes.

   Then go to the upstream repository on GitHub (`abmind-community/contrib-practice`) and click “Compare & pull request”. Make sure your base branch is `main` and your compare branch is your new branch.

   In the pull request description, mention that you are completing Task 01 and (if applicable) reference the issue number you created in step 1.


6. **Respond to review.**

   A mentor may leave comments on your pull request. Make any requested changes by committing to the same branch. When everything looks good, your PR will be merged and you can move on to the next task.

This workflow - opening an issue, working on a feature in a branch, committing with clear messages, and opening a PR - is the same process used when contributing to Mesa.