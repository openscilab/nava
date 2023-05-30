# Contribution			

Changes and improvements are more than welcome! ❤️ Feel free to fork and open a pull request.		


Please consider the following :


1. Fork it!
2. Create your feature branch (under `dev` branch)
3. Add your new features or fix detected bugs
4. Add standard `docstring` to your functions/methods according to the [standard format](#standard-docstring-format)
5. Add tests for your functions/methods (`test` folder)
6. Update `README.md` (if needed)
7. Pass all CI tests
8. Update `CHANGELOG.md`
	- Describe changes under `[Unreleased]` section
9.  Update `AUTHORS.md`
	- Add your name under `# Other Contributors #` section
10. Submit a pull request into `dev` (please complete the pull request template)


## Standard docstring format
Here, the `docstring` format mainly follows the PEP suggested structure. Note the following items
   - Start the `docstring` description with uppercase letter and end it with a dot
   - All other descriptions should be written in lowercase (unless exceptions)
   - Declare the abbreviations before using them

Example:

    def sum(x, y):
        """
        Calculate sum of two given input.

        :param x: first input to be summed
        :type x: int
        :param y: second input to be summed
        :type y: int
        :return: sum of x and y as int
        """
