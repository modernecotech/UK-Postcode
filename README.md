The test example as instructed on the page below was carried out:
https://gist.github.com/edhiley/5da612c93e31c7e60355


Instructions for use. 

1- install Python 3.5 or above
2- unzip the files which should include the following:
	-part1.py     		python file for exercise 1
	-part2.py			python file for exercise 2
	-part3.py			python file for exercise 3
	-test_postcode.py	python code for unit tests
	-README.md			this file including instructions for use
	-ANALYSIS.md		Analysis of the exercise and improvements

3- how to run the examples: 

open a command prompt / terminal in the same folder where the files are
located.

NOTE: if you also have python 2 installed on the system please use the command 
python3 to run the examples below.

run the unit test: 
python -m unittest test_postcode.py
(the unit test tests the examples included on the github page for validation)
if you need higher verbosity for the test output please use:
python -m unittest -v test_postcode.py



run part1: 
python part1.py WC1A 2AA 
(it can be run with different postcodes of your choosing to test the regex)

run part2: 
python part2.py "import_data_csv.gz" 
(of course other gziped csv files can be used) a "failed_validation.csv" file
generated when this finishes containing the failed postcodes).


run part3: 
python part3.py "import_data_csv.gz"
(this one will generate both a "succeeded validation.csv" and "failed_validation.csv" 
files). The files are naturally sorted. 