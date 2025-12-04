# Task 03 - Add unit tests

Writing tests ensures that your changes don’t break existing functionality
and allows you to verify that new code behaves as intended. Mesa uses
[`pytest`](https://docs.pytest.org/) with coverage reporting. This task
will guide you through writing tests for a small utility module.

In this folder you will find:

- `math_utils.py` - a simple module with arithmetic functions.
- `tests/test_math_utils.py` - a skeleton test file.

Your goal is to complete the tests and ensure they pass with coverage.

### Steps

1. **Stay on the same branch used in Task 02.**

   You should still be on the branch you created in the previous task (for example, `fix-style`). If you aren’t, switch back to it:

   ```bash
   # replace fix-style with whatever branch name you used in Task 02
   git checkout fix-style
   ```

   You will add your unit tests to this branch so that the existing pull request is updated, simulating the typical workflow where a reviewer asks for additional changes.

2. **Inspect the code.**

   Open `math_utils.py` and examine the functions `add` and `divide`. Note that `divide` returns `None` if division by zero is attempted.

3. **Write tests.**

   Open `tests/test_math_utils.py` and replace the `pass` statements with real assertions. For each function:

   - Test a few typical cases (e.g. positive numbers, negative numbers, zero).
   - Test edge cases where appropriate (e.g. dividing by zero should return `None`).
   - Use the built‑in `pytest.raises` context manager if you choose to change the function to raise an exception instead of returning `None`.

4. **Run the test suite.** Execute:

   ```bash
   pytest --cov=src tests/
   ```

   Ensure that all tests pass and that coverage is reported. If any tests fail, review your code and tests to identify the issue.

5. **Commit your changes to the same branch.**

   Once your tests pass, stage and commit both the test file and any changes you made to `math_utils.py`. Use a descriptive commit message, such as:

   ```bash
   git add tests/test_math_utils.py
   git commit -m "add unit tests for math_utils (#<issue-number>)"
   ```

6. **Push the updates to the same pull request.**

   Push your branch to your fork again. Since you used the same branch, GitHub will automatically update the existing pull request. Leave a comment on the pull request explaining that you’ve added tests and addressing any previous review comments.

Writing tests is a critical part of contributing to Mesa. All new features and bug fixes should include appropriate test coverage. In this exercise you practise updating an open pull request in response to feedback rather than opening a fresh one.