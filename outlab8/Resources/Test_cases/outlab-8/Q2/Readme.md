## Running test_grader

Make sure that before running `test_grader.py` on `grader.py`, change `Lab5Exception` or `Lab8Exception` to `Exception` at every place in your file. You can use following commands:

`sed -i "s/Lab5Exception/Exception/g" grader.py`

`sed -i "s/Lab8Exception/Exception/g" grader.py`

Also remove the `import statement` of Exception.

While evaluation, we have taken care of such adjustments. After making these adjustments, run `test_grader.py`