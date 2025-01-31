# UnboundLocalError in Python
This repository demonstrates a common yet easily overlooked error in Python: the `UnboundLocalError`.  The error arises when a local variable is accessed before it has been assigned a value within its scope. This often occurs within `try-except` blocks where an exception prevents the variable from being initialized.

## The Bug
The `bug.py` file contains a function that attempts to handle division by zero and type errors. However, if an exception is raised, the variable `result` is never assigned, leading to an `UnboundLocalError` when the program tries to access it outside the `try` block.

## The Solution
The solution (`bugSolution.py`) addresses this issue by assigning a default value to `result` before the `try` block, ensuring it's always defined regardless of whether an exception occurs.