The mistake

the provided regex had a mistake in it whereby the AA99 
included a number before the exclusions. I had to thus make
a small change to the REGEX to make it function. 

==========================================================

Accuracy

In terms of postcode accuracy there are many exceptions
and its easy for "false positives" to pass through the 
regex provided. Trawling the internet I did find several 
slightly better REGEX examples (an example is in the comments 
at the bottom of part3) however none of them are able to 100% 
certify that a post code exists. 

In my view the best approach would be to incorporate the 
entire post office post code database in a NoSQL table for 
easy local verification in an operational system where accuracy
is critical.

===========================================================

Performance. 

Since this exercise was limited to the use of "built in" libraries
I could not make use of Pandas to speed up the file processing 
that library would provide the largest improvement in speed. 
However on my laptop the entire process "part3" took less than 
30 seconds in which time the GZIP file was opened, the CSV imported
Sorted and then filtered by regex into two separate files. 


============================================================

Testing

Simple TDD testing was done for the functions and functions
iterated. It was a simple example so functional testing was
basically just "part3". 

