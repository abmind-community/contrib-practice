# Task 05 - Resolve merge conflict through rebasing

Rebasing rewrites the history of your branch so that it appears as if your changes were made on top of the latest `main`. It keeps your history linear but rewrites commit hashes. This exercise builds on the 04-merge-conflict task and shows how to resolve the same situation with `git rebase`.

### Steps

1. **Repeat the setup from Task 04.**

   Follow Steps 1 - 4 in `tasks/04-merge-conflict.md` (create `update-story-rebase`, edit line 2, open a PR in your fork, then make a conflicting edit on `main`). Stop once `main` has the competing change and your pull request shows the “This branch has conflicts” warning.

2. **Rebase onto the updated `main` instead of merging.**

   ```bash
   git checkout update-story-rebase
   git fetch origin
   git rebase origin/main
   ```

   Git flags line 2 as conflicted. Open `tasks/story.txt` locally to view the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

   Note: Rebasing keeps history linear and easier to read. But it rewrites commits, so any collaborators on this branch would need to coordinate before you push.

3. **Resolve the conflict.**

   Combine the two versions of line 2. **Do not simply delete the other contributor’s
   change** — make sure your resolution preserves both ideas or otherwise integrates them. Remove the conflict markers when you’re done. Then stage and commit the resolved file:

   ```bash
   git add tasks/story.txt
   git rebase --continue
   ```

4. **Force-push safely.**

   Because the commit hashes changed, you must update the remote branch with `--force-with-lease`:

   ```bash
   git push --force-with-lease origin update-story-rebase
   ```

   Force pushes can overwrite remote work if someone else pushed to the same branch; `--force-with-lease` helps guard against that by refusing to overwrite unexpected commits.

5. **Explain the outcome on your pull request.**

   Refresh the PR to confirm the conflict warning is gone and leave a comment describing how you reconciled the edits.

Understanding both merge and rebase conflicts will help you keep your branches clean and avoid noisy merge commits. Mesa maintainers often recommend rebasing to keep a linear history.
