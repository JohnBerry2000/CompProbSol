# Problem 5
## Outcomes
- Import a large data file using multiple MATLAB functions
- Export processed data to multiple file formats

## Problem 
Importing and processing data is an important skill to master, especially if you find yourself in the industry dubbed "Big Data". Today, you will be processing data from `GlobalTempbyYear.txt` (format of which is location at https://www.metoffice.gov.uk/hadobs/hadcrut4/data/current/series_format.html) and `GlobalCarbonBudget2018.xlsx` (which has extensive documentation in the file). These files contain global temperature averages and carbon emission data respectively. Both are rich datasets that we will return to, but right now we want a small slice of data from each file. Writing a script in `Python` and `MATLAB`:
 
1. Import the data from the *Historic Budget* sheet in the `GlobalCarbonBudget2018.xlsx` and the first two columns (year and average global temperature) from `GlobalTempbyYear.txt`. (Note the first year in `GlobalTempbyYear.txt` is 1850. )
1. Calculate the **cumulative sum** of the columns labeled `fossil fuel and industry` and `land-use change emissions` in `GlobalCarbonBudget2018.xlsx` through the years starting with the year 1850. This cumulative sum of carbon emissions should still have values for each year. For instance, the value for 1860 should be the sum of all carbon emissions from 1850 to 1860 (you may want to look at the function `cumsum` in MATLAB and its counterpart in `numpy`)
1. Produce 2 graphs: One plotting the global temperature and the cumulative sum of carbon emissions vs the year **on the same plot using two y axes** and one plotting global temperature vs the cumulative sum of carbon emissions.  
1. Save these three columns of data to a `.mat` file
