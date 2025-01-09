import os
def function_with_closed_file(filename):
    try:
        with open(filename, 'w') as f:
            # ... some code that might raise an exception ...
            f.write('some data')
    except Exception as e:
        print(f"An error occurred: {e}")
        # Clean up if necessary. In this example, no explicit cleanup is needed as 'with' takes care of it.
        # os.remove(filename)  # If needed to remove partially created file

# Example usage
function_with_closed_file("my_file.txt")