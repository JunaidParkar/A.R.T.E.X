# import markdown
# from markdown.extensions.fenced_code import FencedCodeExtension


data = """```python
# This code prints any data.

# Define a function to print data
def print_data(data):

  # Print the data
  print(data)

# Driver code
data = "Hello World!"
print_data(data)
```

This code will print the following output:

```
Hello World!
```"""

# html = markdown.markdown("hello world", extensions=[FencedCodeExtension()])
# print(html)

import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
text = """
```python
print('Hello, world')
```
"""
print(markdown.markdown(data, extensions=[FencedCodeExtension()]))