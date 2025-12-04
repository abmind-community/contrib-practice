# Task 04 - Resolve merge conflict

Merge conflicts happen when two branches change the same lines differently. This exercise walks you through resolving a conflict in `tasks/story.txt`.

### Steps

1. **Create a feature branch.**

   From the `main` branch, create and check out a new branch named `update-story`:

   ```bash
   git checkout main
   git checkout -b update-story
   ```

2. **Modify the story.**

   In this folder you'll find `story.txt`. It contains a short story with numbered lines. Edit the line beginning with `2:` to say something different, and save the file.

3. **Commit and open a pull request in your fork.**

   Stage and commit your change, push the branch to your fork, and open a pull request *within your own repository* (e.g. from `update-story` into your `main` branch). **Do not open a PR against the upstream `abmind-community/contrib-practice` repository.** In the PR description,
   note that you’re practising Task 04 - merge conflicts.

   ```bash
   git add tasks/story.txt
   git commit -m "update line 2 of story.txt"
   git push -u origin update-story
   # open a PR from `update-story` into `main` in *your* fork (not upstream `github.com/abmind-community/contrib-practice`)
   ```

4. **Pretend to be someone else.**

   To simulate another contributor, switch back to `main`, edit the same line in `story.txt` in a *different* way, commit and push. This represents someone else making changes while your pull request is open.

   ```bash
   git checkout main
   # Edit the file again with a different change...
   git add tasks/story.txt
   git commit -m "change line 2 of story.txt differently"
   git push
   ```

   Once `main` is updated, open your pull request in GitHub: it should now show a “This branch has conflicts” warning that prevents merging until you resolve the issue.

5. **Merge `main` into your branch and inspect the conflict so you can unblock the PR.**

   ```bash
   git checkout update-story
   git fetch origin
   git merge origin/main
   ```

   Git flags line 2 as conflicted. Open `tasks/story.txt` locally to view the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

6. **Resolve the conflict.**

   Combine the two versions of line 2. **Do not simply delete the other contributor’s
   change** — make sure your resolution preserves both ideas or otherwise integrates them. Remove the conflict markers when you’re done. Then stage and commit the resolved file:

   ```bash
   git add tasks/story.txt
   git commit -m "resolve merge conflict in story.txt"
   ```

7. **Push and explain.**

   Push your feature branch to your fork again. The pull request you opened in step 3 will automatically update and should now show that the conflict is resolved. Leave a comment explaining how you resolved the conflict and why you kept both changes.


This exercise simulates the common scenario where someone else modifies a file on `main` while your pull request is open. In real contributions you will often need to keep your branch in sync with upstream changes and resolve conflicts without discarding anyone else’s work.
