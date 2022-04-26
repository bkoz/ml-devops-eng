# ML DevOps Engineering 
## Coursework

### Clean code

#### Check your code for cleanliness.
```
pylint <source-file>
```

Source files can not begin with a number.

#### After acheiving a high score with `pylint` run `autopep8` to format.
```
autopep8 --in-place --aggressive --aggressive <source-file>.py
```