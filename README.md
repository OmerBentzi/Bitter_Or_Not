# Bitter_Or_Not
A machine learning project, dealing with a large amount of data and normalizing the data
1. Checking Are there any missing data? What can be done to complete or delete?
Answer: There are missing data in the above data file, it is possible to delete the data that comes from the same category due to several reasons:
A. Data containing text
B. Data containing empty cells (missing data)
third. Data containing text and numbers together
d. Data containing several numbers together in the same field.
It is possible to complete the figure that comes from the same category due to several reasons:
A. A row for which we know more than 50% of the data (we would like to preserve this column)
B. A column that contains more than 50% of its fields for us (we would like to preserve this column)

2. The target variable is ACTIVITY, turn it into a binary variable, meaning BITTER will receive the value 1.
 
3. Reducing the data file, checking whether there is data that can be deleted
o Columns containing text
o Columns containing empty cells (missing data)
o Columns containing text and numbers together
o Columns containing several numbers together in the same field.
o Columns containing only one value
o Columns containing more than 50% of the fields null value/fixed value
Answer:
Out of 310 features, only 66 features remain.
So a total of 244 attributes were deleted according to the conditions for deleting columns.


4. Are there unusual materials? Identification of unusual materials according to the accepted methods,
Delete the unusual materials, are there any?
o Checking the mean and standard deviation for each variable and for each row see how many unusual variables exist

Answer:
There are unusual materials, we used several methods to identify them:
Outliers detection - which requires obtaining the average and multiplying the standard deviation * 2, which will lead to the creation of some range (confidence interval), where we considered what is outside the confidence interval as an exception.

We deleted the unusual materials and with the help of the test we did we were able to reduce from 2075 rows to 2033, so that 42 rows were deleted in total that had more than 50% exceptions, but there are still exceptions that were deleted from the rows but in that row there were not more than 50% exceptions and thus the row was deleted.

5. Performing a correlation on the remaining variables, and checking which of the variables are correlative, meaning that there is a correlation of 0.8 or higher (in absolute value).
Answer:
First we defined a new variable corr_matrix and ran the corr() function on it, which takes the maximum of all the numbers and compares it to one and the minimum of all the numbers and compares it to 0, and thus by the probability between the minimum and the maximum, each number will receive a value between 0 and 1.
The code identifies pairs of variables with a Pearson correlation coefficient greater than or equal to 0.8.
The code drops one of the variables in each correlation pair from dataframe df. The dropped variable is not specified in the code, but it will be one of the variables with a high correlation coefficient.
We finally got it to have the same number of rows as the original data frame, but with fewer columns (21 columns).

6. To present the remaining variables with the help of histograms and boxplot.

7. Building a table showing descriptive statistics for each variable, according to the measurement scale of the variable, for example:

attached to the file
1. Excel sheet with the final data file that is ready to work.
2. Excel sheet with the final normalized data file.
