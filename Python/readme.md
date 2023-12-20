# Access function code details
[Different __code__ functions](https://youtu.be/7lmCu8wz8ro?list=PLFjq8z-aGyQ4Y3mSWGBptr7SArEsfdWQA&t=2842)

# Contextmanager
Context manager: is a peace of code that pairs setup and teardown actions so the teardown action is always called after the setup action.

a Generator is some form of syntax that allows us to do things like enforce sequencing and interleaving of actions.
[Context managers](https://youtu.be/7lmCu8wz8ro?list=PLFjq8z-aGyQ4Y3mSWGBptr7SArEsfdWQA&t=5761)

# Random tips:

To force functions in python to use keyargument you can add `*` as first argument:

```python
def test(*,arg1, arg2):
    return arg1 + arg2

print(test(arg1=1, arg2=3))

```