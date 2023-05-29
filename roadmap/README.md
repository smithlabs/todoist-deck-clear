# Project Roadmap

### Initial changes
-   turn it into a CLI instead of a few scripts. so refactor it so you have 1 `main()` and have each 'script' become a sub-command.
-   as mentioned, fix all the pip8 issues as needed.
-   remove the big `try/catch` blocks, try to keep those scoped small
-   replace `print` with a logger
-   add a setup.py to make it installable

### Testing framework
-   pass `api` as an argument to your functions, instead of `api_key` here: [https://github.com/smithlabs/todoist-deck-clear/blob/main/delete-tasks.py#L6](https://github.com/smithlabs/todoist-deck-clear/blob/main/delete-tasks.py#L6). This makes it easier to mock/test.
-   Unit tests: create a fake/mock `TodistAPI` with the methods your using.
-   Write some unit tests. Example: `test_delete_tasks()`. Create your `MockTodoistAPI` object at the beginning. Add some fake projects to your mock so that they will be returned by it when you call `api.get_projects()` on the mock. Similarly, add some fake tasks for the projects the fake is going to return. Finally, call `delete_tasks(fake_todoist, ["some-project"], False)` and verify the mock no longer has the tasks that should be deleted.

Hardest part is likely understanding and figuring out how to use a fake/mock and verify behavior of your code using it.

Python has builtin mocking support, so you can probably use that, but IMO, it can be a bit magical and i find it can be more useful to write your own, simple fakes/mocks to test when you are learning.

# Overview

**Feedback from a FAANG Engineer on my code**

>The lack of documentation and code comment is disappointing.  You really need to write documentation I don't even want to read this code and guess what's happening. @Sean Smith this is half assed attempt get some documentation in your code.

Ouch! 

![pain](https://i.imgur.com/zDSfPwK.png)


**My code sucks, where do I start?**

>“Code tells you how; Comments tell you why.” - Jeff Atwood

The documentation of projects have a simple progression:  
1.  No Documentation
2.  Some Documentation
3.  Complete Documentation
4.  Good Documentation
5.  Great Documentation

*If this is just for you 2 is good enough usually if working on a team 3-4 is where you want to be at. 5 usually happens when you have downtime (end of year freezes/code)

**Links to great documentation practices**
1. https://realpython.com/documenting-python-code/
2. https://google.github.io/styleguide/pyguide.html
3. [Example of well documented Go code!](https://github.com/golang/go/blob/master/src/io/io.go)

**All your functions should look like this**
```
 def connect_to_next_port(self, minimum: int) -> int:
    """Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.

    Raises:
      ConnectionError: If no available port is found.
    """
```

**Code review insights at FAANG**
Most hiring managers who review code usually just want to see the following :  

1.  Comment in code
2.  Proper style guide used
3.  Clear code that's easy to read and not cleaver

**Bonus points for documenting API calls**
Before
```
 projects = api.get_projects()
```

After
```
# API call: https://developer.todoist.com/rest/v2/#get-all-projects)
# Returns JSON-encoded array containing all user projects.
# A successful response has 200 OK status and application/json Content-Type.

projects = api.get_projects()
```

---
# Guidelines

The four essential rules:
1. Keep comments as close to the code being described as possible.
2. Don’t use complex formatting (such as tables or ASCII figures).
3. Don’t include redundant information. Assume the reader of the code has a basic understanding of programming principles and language syntax.
4. Design your code to comment itself. The easiest way to understand code is by reading it. When you design your code using clear, easy-to-understand concepts, the reader will be able to quickly conceptualize your intent.


> [!Important] 
> Remember that comments are designed for the reader, including yourself, to help guide them in understanding the purpose and design of the software.

Other important considerations:

**Type Hinting**: You can immediately tell that the function expects the input `name` to be of a type `str`, or [string](https://realpython.com/python-strings/). You can also tell that the expected output of the function will be of a type `str`, or string, as well.

```python
def hello_name(name: str) -> str:
    return(f"Hello {name}")
```

1. Use a type checker
2. https://mypy-lang.org/

1. `pip3 install mypy-lang`

**Docstrings**: These are built-in strings that, when configured correctly, can help your users and yourself with your project’s documentation. Along with docstrings, Python also has the built-in function `help()` that prints out the objects docstring to the console.

In all cases, the docstrings should use the triple-double quote (`"""`) string format. This should be done whether the docstring is multi-lined or not. At a bare minimum, a docstring should be a quick summary of whatever is it you’re describing and should be contained within a single line.

![python-tings-mon](https://i.imgur.com/0KPLgZp.png)

All docstrings should have the same max character length as comments (72 characters). Docstrings can be further broken up into three major categories:

-   **Class Docstrings:** Class and class methods
-   **Package and Module Docstrings:** Package, modules, and functions
-   **Script Docstrings:** Script and functions

You can load your own Python files into the interpreter and run `docs()` to see the functions within it.
```bash
# Load Python file from terminal
python -i file.py
```

In the Python interpreter show the current functions.
```python
dir()
```

**Char limit**: According to [PEP 8](http://pep8.org/#maximum-line-length), comments should have a maximum length of 72 characters. This is true even if your project changes the max line length to be greater than the recommended 80 characters.

**Code Description:** Comments can be used to explain the intent of specific sections of code:
```python
# Attempt a connection based on previous settings. If unsuccessful,
# prompt user for new settings.
```

**Algorithmic Description:** When algorithms are used, especially complicated ones, it can be useful to explain how the algorithm works or how it’s implemented within your code. It may also be appropriate to describe why a specific algorithm was selected over another.

**Code formatter**: Use a code formatter

1. Use [flake8](https://flake8.pycqa.org/en/latest/) initially for learning
2. Later on use this - https://github.com/psf/black has a neovim integration https://github.com/averms/black-nvim
