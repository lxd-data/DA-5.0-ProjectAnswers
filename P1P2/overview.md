## Most of this is also covered in the [Notion Progress Tracker P1P2 Doc](https://www.notion.so/Progress-Tracker-0a07418e75fc4bf59bf33fe6c7bda36f).

### 1. Passing Next.Tech Checks:
    - I was able to pass all checks. The code that passed these checks is included
      in the P1P2 folder.
    - I will discuss the strictness of these checks more in the `RegEx` Section below.
### 2. Python Best Practices:
    - There was one scenario where I felt like we did not 'follow' Python best practices.
      This is when we call the `calc_mean()` function from within the `calc_stddev()` function.
    - I typically think it is best practice to pass a value from one function to another function
      as a `parameter` (this is an important concept for beginner python programmers to understand, and
      it also isolates functions from one another [making it easier to trace where functions are being 
      called from]).
    - Overall, after going through the entire lab, I don't think this is a problem worth solving now (at the 
      end of the day, this isn't a big issue. It is just something I wanted to point out)
### 3. RegEx Tests:
    - There were a few RegEx/Test Cases that are too lenient or working incorrectly:
        1. The RegEx for docstrings is not working throughout all checks. I was able to pass tasks with no 
           docstring or one and multi-line docstrings.
        2. In `task 4`, the RegEx for the variable `stats` does not work. I passed the task without a var 
           named `stats`.
        3. In `task 5`, we should add RegEx to check for the use of `while` and `.replace()`. I did not see
           any RegEx for this.
### 4. Miscellaneous:
    - The starter files are incorrect (tested from the `da@test.com` account). The starter file is `profit_margin.py`, but they should be `input.py` and `library.py`.