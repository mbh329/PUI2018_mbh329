# a.verify that their Null and alternative hypotheses are formulated correctly:


## Null Hypothesis 

### Customers are more likely to use Citibike during peak hours (7am - 9am, 5pm - 7pm) than subscribers during peak hours

## Alternative Hypothesis 

### Subscribers are more likely to use Citibike during peak hours (7am - 9am, 5pm - 7pm) than customers during peak hours 

### Comments:  This is an interesting idea but it could be more helpful to formulate a testable hypothesis and specify what exactly it means by more usage. One idea could be to specify the sample statistic that we are measuring here. E.g we could state that:
 
##### average trip duration of customers during peak hours is greater than subscribers 

#### OR

##### Average trips made by the customers is greater than subscribers during the peak hours. 

#### Furthermore, formulating corresponding equations will also improve clarity. 

#### Finally, we also need to specify the unit of observation , for example average daily, or monthly average so that we know how to claculate the statisic from the data. 



# b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

#### So apparently, we are interested in the counts of subscriber and customer rides in the peak hours. We have the required data to test this hypothesis. 

#### If we only wish to see peak hours in general and dont care about the trend we would aggreate over peak hour rather than over individual hours in the peak time, because we need just one sample statistic from each sample. So the aggregation counts of trips over hours is good for descriptive analytics. But we would not want to aggregate only over hours, since this will give us only one observation (sample size 1) of count for each hour and rider type. But we need a bigger sample for both rider types. For that we need to decide a uit of observation which we could define as a day. If we group by both day and hour and rider type, we will have two samples rather than just two values. Now we could calculate the average daily count for both samples and test the null hypothesis.

### Alternately if we want to conduct a proportion test, more useful statistic for each group would be the ratio of customer/(customer+subscriber) for any given hours rather than customer/(customer all day).

# c. chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.

### For comparing average daily counts for rider types two sample t test is a suitable test. A proprtions test is also a possibility if the data is organized accordingly. 

### If we take all the rides in peak hour and measure the proportion of customer and subscribers, we can do a one sample proportion test with null hypothesis being that proportion of customers is greater than or equal to 0.5.
