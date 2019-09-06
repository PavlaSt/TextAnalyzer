# Text Analyzer
This is a task from Engeto's Python academy

## Task Description
Let's create a program that will perform the following tasks:

- Greet or welcome the user to the app
- Ask the user for entering username and password
  - Check whether the password and username entered are among those registered.
  - If you consider this task difficult, then just check, whether the username and password entered are among the registered, without taking care of pairing them together.
  - The registered username - password pairs:
<pre>
| USER |   PASSWORD  |
-----------------------
| bob  |     123     |
| ann  |    pass123  |
| mike | password123 |
| liz  |    pass123  |
</pre>


- Ask the user to select among the three texts stored in the variable TEXTS.
- Calculate the following statistics for the selected text:

  - number of words in total
  - number of words starting with capital letter
  - number of uppercase words
  - number of lowercase words
  - number of numeric-only words (e.g. 100, not 100N)
- Create a bar chart depicting the frequencies of word lengths in the text. For example:

<pre>
1 * 1
2 *********** 11
3 *************** 15
4 ********* 9
5 ********** 10
</pre>

(In the above chart, there is one word of length 1, 11 words of length 2, 15 words of length 3 etc.)

- Calculate the sum of all the numeric "words" in the given text. For example the sum for the string below would be 8500: *"that rises sharply some 1000 feet above
Twin Creek Valley to an elevation of more
than 7500 feet above sea level. The butte
is located just north of US 30N"*

**Your program could run as follows:**
<pre>
[engeto@localhost PythonLesson3]$ python task.py
----------------------------------------
Welcome to the app. Please log in:
USERNAME: bob
PASSWORD: 123
----------------------------------------
We have 3 texts to be analyzed.
Enter a number btw. 1 and 3 to select: 2
----------------------------------------
There are 62 words in the selected text.
There are 10 titlecase words
There are 0 uppercase words
There are 51 lowercase words
There are 1 numeric strings
----------------------------------------
 2 ******* 7
 3 ***************** 17
 4 ********* 9
 5 ********** 10
 6 ******* 7
 7 *** 3
 8 ** 2
 9 ***** 5
10 * 1
13 * 1
----------------------------------------
If we summed all the numbers in this text we would get: 300.0
----------------------------------------
</pre>
