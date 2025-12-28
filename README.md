# Contribution Practice

Welcome to the contribution practice repository! This repository is designed to help you get comfortable with the workflow used when [contributing to the Mesa](https://github.com/projectmesa/mesa/blob/main/CONTRIBUTING.md) project. It contains a series of self‑contained tasks that mirror the steps you will follow when submitting a real pull request to Mesa.

## Why this repository?

The Mesa team asks contributors to follow a specific process: create a ticket, fork the repository, work on a feature or bug fix in a separate branch, run linters and tests, write clear commit messages, and open a pull request for review. Working through the tasks in this repository will give you hands‑on experience with that workflow without the complexity of Mesa’s codebase.

If you prefer a visual overview first, you can also read the slides before diving into the tasks:

> [📄 **Contribution Workflow (slides)**](https://github.com/abmind-community/course-2025/blob/main/lecture_02/part_1_contribution_workflow.pdf)

## Getting started

1. **Fork this repository.**

   Use the "Fork" button on GitHub to create your own copy under your account.

2. **Clone your fork.**

   On your machine run:

   ```bash
   git clone https://github.com/<your‑username>/contrib-practice.git
   cd contrib-practice
   ```

   Setting your default pull behaviour to rebase is recommended to avoid merge commits when keeping your branch up to date:

   ```bash
   git config pull.rebase true
   ```

   > **Note:** You do *not* need to install any developer dependencies (like Ruff, pre-commit, etc.) until you reach Task 02. Installing them early can sometimes cause style checks to run before you have learned how to fix them, which may lead to confusing errors during Task 01. Just clone the repository and start with the first task.

3. **Read the tasks.**

   Each task is located in the `tasks/` directory and contains step‑by‑step instructions. Tasks are numbered and build on one another, so it is helpful to complete them in order.

## Commit messages and branches

When working on a task:

- **Create a new branch** based off of `main`. Use a descriptive name. For example, `add-yourname` for Task 01, `fix-style` for Tasks 02-03, or `update-story` for Task 04. Tasks 02 and 03 share the same branch because you will update an existing pull request.
- **Write clear commit messages** that describe *what* you changed and *why*.
  For example:

  ```
  add alice to CONTRIBUTORS.md (#1)

  This adds my GitHub username and name to the contributors file, completing task 1.
  ```

  The first line should be short (around 50 characters) and include a ticket reference if you created one. Optionally use subsequent lines to explain additional context.
- **Push your branch** to your fork and **open a pull request**.
  * For Tasks 01-03, open the pull request against this upstream `abmind-community/contrib-practice` repository so that your instructors can review your work.
  * For Tasks 04 and 05 (the conflict exercises), open the pull request **within your own repository** (e.g. from your feature branch into your `main`). This allows you to practise resolving conflicts without affecting the upstream repository.

Following these practices now will prepare you to contribute to Mesa later.

## Pull request policy

To keep this repository clean and focused for new cohorts:

-	Task 01 PR (adding yourself to CONTRIBUTORS.md) is the only PR that will be merged into this upstream repository.
-	Tasks 02 and 03 PRs are for practice and review (including updating an existing PR). They will be closed without merging after some time.
-	Tasks 04 and 05 PRs (merge conflict) should be opened within your own fork (feature branch -> your fork’s main). Do not open these PRs against the upstream repository.

## Tasks overview

A quick summary of the available tasks:

| Task | Description |
| ---- | ----------- |
| [**01‑add‑yourself**](https://github.com/abmind-community/contrib-practice/blob/main/tasks/01-add-yourself.md) | Add your name to the `CONTRIBUTORS.md` file, practising the branch/fork/PR workflow. |
| [**02‑fix‑style**](https://github.com/abmind-community/contrib-practice/blob/main/tasks/02-fix-style.md) | Use `ruff` and pre‑commit to fix style issues in a Python file.  Leave your pull request open for the next task. |
| [**03‑add‑tests**](https://github.com/abmind-community/contrib-practice/blob/main/tasks/03-add-tests.md) | Write unit tests for a small module and update your existing pull request instead of creating a new one. |
| [**04‑merge‑conflict**](https://github.com/abmind-community/contrib-practice/blob/main/tasks/04-merge-conflict.md) | Create and resolve a merge conflict by editing the same line on two branches **in your own repository**. Do not open a pull request against this upstream repository for this task. |
| [**05‑merge‑conflict‑rebase**](https://github.com/abmind-community/contrib-practice/blob/main/tasks/05-merge-conflict-rebase.md) | Repeat the Task 04 setup but practise resolving the conflict with `git rebase`, including handling rewritten history with a safe force push. |

After completing these exercises you should feel comfortable with the contribution workflow and ready to start making contributions to Mesa itself. If you get stuck or have questions, please reach out in our discussion threads.

Happy contributing!
