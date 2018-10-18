### For this weeks homework, I worked with myself for assignment 1 when reviewing my partners null hypothesis. For assignment two, I worked with primarily with Duke. I also helped manrique with his. For assignment 3, I worked with Manrique and Amber. Everyone was very helpful. For assignment 4 i ran out of time. 

|  **Statistical Analyses**     | **IV(s)**         | **IV type(s)** | **DV(s)**       | **DV Types**  | **Control Var.** |**Q to be answered**|**H0**      | **alpha** |**Link to paper**|
| ------------- |:-------------:| ----------:|------------:|----------:|-------------:|---------------:|-------:|------:|------------:|
| Logistic regression |# of individuals (community size)| Continuous |Absence or presence of critical scalar stress levels|dichotomous| Hutterties of North America(control group|What is the relationship btw. community size + scalar stress levels in archaelogical communites when size can be estimated? Is there a theshhold of community size that there is a higher propability of a critical scalar stress levels?|test group(s) scalar stress level threshold <= control group scalar stress level threshold| 0.05|https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0091510#s4 |
ANCOVA	| 1, Ranks of values | ordinal | 1, did Self Affirmation or no| categorical | 1, age | continuous (could also be categorical) | 	Do participants in self-affirmation rak  value significantly higher than control group | Ranks test groups <= Ranks control group | 0.05 | [Self-Affirmation Improves Problem-Solving under Stress](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0062593) |
MANCOVA  |difference in parameters between control and patient groups|real number|Respiratory rate, Heart Rate Variability, Tidal Volume, HF high frequency, LF low freq., minute ventilation, blood oxygen saturation level|continuous|sickness indicator|categorical|are there differences for respiratory parameters (breathing rate, rapid shallow breathing index, minute volume, ratio of inspiration and exhalation, RMMSDResp, LFResp, MFResp, HFResp, VHF1Resp, tidal volume, RMMSDTV, LFTV, HFTV) between all three groups?|$$H_0: parameter_{control} = parameter_{patient}$$|0.001|[The Phrenic Component of Acute Schizophrenia – A Name and Its Physiological Reality](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0033459)
Spearman’s rank correlation  |self-reported wealth|continuous|primary livelihood, ethnicity, self-reported wealth ranking, acres of land (used for crops and/or grazing), sanitation facilities, education level of both parents, primary expenditures, frequency of requests for assistance (financial or otherwise) to family members and/or others in the past year, and whether family lives within the District or beyond.|continuous and categorical (e.g. education level)|mobile phone ownership|indicator variable (categorical)|self-reported wealth was significantly, positively correlated with other indicators of wealth|$$H_0: \rho = 0 $$ | p \sim 0.013 | [Mobile Phones and Mental Well-Being: Initial Evidence Suggesting the Importance of Staying Connected to Family in Rural, Remote Communities in Uganda](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0169819)
||||||||


# Logistic Regresssion Figures

![figure4_opitmalprob](https://user-images.githubusercontent.com/41444592/47115682-51a61400-d22d-11e8-9a38-aa720bb3ce87.png)
"Figure 4. Optimal cutoff on Logistic Regression probabilities.

Plot of sensitivity (percentage of correctly classified cases of critical scalar stress) and specificity (percentage of correctly classified cases of not critical scalar stress) versus community size. Reference line: intersection point at which there is a balance between sensitivity and specificity; it corresponds to the optimal cutoff on logistic regression probabilities (community size 127 = p 0.50). See also Table 2.

https://doi.org/10.1371/journal.pone.0091510.g004 "

![figure5_logregmod](https://user-images.githubusercontent.com/41444592/47115685-536fd780-d22d-11e8-806b-07b66c1777a5.png)
"Figure 5. Logistic Regression model.

A) Best fitting logistic curve (plus 95% confidence band) for the critical level of scalar stress as derived from Olsen’s Hutterite fissioning data. Vertical axis: probability of experiencing not critical/critical scalar stress; horizontal axis: community size in terms of sheer number of individuals. Lower probabilities of experiencing a critical level of scalar stress are associated with smaller community sizes and higher probabilities with larger community sizes. B) Scalar stress (sensu Johnson) chart plus critical threshold as derived by the logistic regression model. Black line: scalar stress as function of number of individuals; it is equal to (n2−n)/2, where n is the number of interacting subjects. Vertical lines: in green, group size threshold at which the probability of critical scalar stress begins to change from low to high (i.e., p = 0.50; mid-point: 126.9; 95% confidence interval: 121.9–131.9); in red, group size threshold at which the probability of critical scalar stress reaches its maximum (i.e., p = 0.99; mid-point: 158.2; 95% confidence interval: 146.6–169.8). See also Table 3. The gradient in the shaded area is meant to visually represent the increase in probability between the two thresholds."


# Other Statistical Test Figures (Ancova, Mancova, Spearman's rank)
  
Include the main plot of the paper (the plot that summarized the result)

![respiration_parameters](https://user-images.githubusercontent.com/41444592/47116279-2d4b3700-d22f-11e8-9ab6-e1103919eb10.png)
Figure 1. Parameters of respiratory analysis of controls, patients and relatives are presented.
The pattern of significantly altered values of patients in comparison to controls is represented in A–F. The increased breathing rate of patients is presented in A. As shown in B, the inspiratory-to-expiratory time ratio is increased in patients indicating a reduction of the exhalation time. Patients breathe shallowly as indicated in C. Most pronounced are increased frequency bands of respiration as indicated in D–F. Boxes indicate data between the 25th and 75th percentile with the horizontal bar reflecting the median (□ = mean; - = 1st and 99th percentile; x = minimum and maximum of data). Significant differences of Bonferoni corrected pair-wise comparisons are indicated: * p<.05; ** p<.01; *** p<.001
![mobile_phone_and_mental_wellbeing](https://user-images.githubusercontent.com/41444592/47116281-2fad9100-d22f-11e8-8c1d-1ee8dc09a554.png)
Table 2. Results for multiple linear regression model predicting mental well-being.
