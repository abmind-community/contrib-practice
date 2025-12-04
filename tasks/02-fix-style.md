# Task 02 - Fix code style issues

Mesa uses the [Ruff](https://docs.astral.sh/ruff/) linter/formatter and [pre‑commit](https://pre-commit.com/) hooks to ensure a consistent code style. This task will show you how to use these tools to automatically fix style problems.

### Steps

1. **Create a new branch.**

   From your local `main` branch, create a branch named `fix-style` or similar:

   ```bash
   git checkout -b fix-style
   ```

2. **Install dependencies.**

   These tasks use a few developer tools. You can install them in a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -e ".[dev]"
   pre-commit install
   ```

   Installing pre‑commit sets up a Git hook that will run Ruff and other checks automatically when you commit.

3. **Run Ruff.**

   The `src/math_utils.py` file in this folder intentionally violates several style rules (missing spaces, inconsistent indentation, unused variables, etc.). Run Ruff on the file to see the problems:

   ```bash
   ruff check src/math_utils.py
   ```

   You can automatically apply many fixes with:

   ```bash
   ruff check src/math_utils.py --fix
   ```

   > Note: When you run `pre-commit run --all-files`, Ruff will be run automatically as part of the pre-commit hooks defined in the `.pre-commit-config.yaml` file.

4. **Apply remaining fixes manually.**

   Ruff might not fix everything automatically. Review the file and fix any remaining issues manually. Pay attention to:

   - Spacing around operators and after commas.
   - Consistent indentation.
   - Removing unused variables or imports.
   - Naming conventions (`snake_case` for functions and variables).

5. **Commit your changes.**

   Stage and commit the fixed file. Use a descriptive commit message, for example:

   ```bash
   git add src/math_utils.py
   git commit -m "fix style issues in math_utils.py (#<issue-number>)"
   ```

6. **Push and open a pull request.**

   Push your branch to your fork and open a pull request referencing this task. A reviewer (or you pretending to be one) will check that your changes pass the Ruff linter and match Mesa’s style.

   > **Do not close this pull request when you are done. In the next task you will build on this same branch and update the same pull request to practise making additional commits in response to review comments.**

This exercise demonstrates how pre‑commit and Ruff are used to enforce code quality in Mesa. Always run `pre-commit run --all-files` before pushing code to catch formatting issues early.
