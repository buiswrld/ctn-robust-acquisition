This is data explored from the [Breast Cancer Wisconsin (Diagnostic)](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) data
### Report
There are no missing values in this data. The `Diagnosis` column has been annotated based on predicting field 2, diagnosis: B = benign, M = malignant
	- sets are linearly separable using all 30 input features
	- best predictive accuracy obtained using one separating plane
		in the 3-D space of Worst Area, Worst Smoothness and
		Mean Texture.  Estimated accuracy 97.5% using repeated
		10-fold crossvalidations.  Classifier has correctly
		diagnosed 176 consecutive new patients as of November
		1995. <br>
Each feature has 3 values - mean, standard error in measurment (se), and the worst measurement.<br>
The data summary is as below:
| feature                 | count | mean       | std        | min      | 25%      | 50%      | 75%      | max     | cv       | missing |
|:------------------------|------:|-----------:|-----------:|---------:|---------:|---------:|---------:|--------:|---------:|--------:|
| radius_mean             | 569 | 14.127292  | 3.524049   | 6.981    | 11.7     | 13.37    | 15.78    | 28.11   | 0.249450 | 0 |
| texture_mean            | 569 | 19.289649  | 4.301036   | 9.71     | 16.17    | 18.84    | 21.8     | 39.28   | 0.222971 | 0 |
| perimeter_mean          | 569 | 91.969033  | 24.298981  | 43.79    | 75.17    | 86.24    | 104.1    | 188.5   | 0.264208 | 0 |
| area_mean               | 569 | 654.889104 | 351.914129 | 143.5    | 420.3    | 551.1    | 782.7    | 2501    | 0.537364 | 0 |
| smoothness_mean         | 569 | 0.096360   | 0.014064   | 0.05263  | 0.08637  | 0.09587  | 0.1053   | 0.1634  | 0.145954 | 0 |
| compactness_mean        | 569 | 0.104341   | 0.052813   | 0.01938  | 0.06492  | 0.09263  | 0.1304   | 0.3454  | 0.506155 | 0 |
| concavity_mean          | 569 | 0.088799   | 0.079720   | 0        | 0.02956  | 0.06154  | 0.1307   | 0.4268  | 0.897753 | 0 |
| concave_points_mean     | 569 | 0.048919   | 0.038803   | 0        | 0.02031  | 0.0335   | 0.074    | 0.2012  | 0.793204 | 0 |
| symmetry_mean           | 569 | 0.181162   | 0.027414   | 0.106    | 0.1619   | 0.1792   | 0.1957   | 0.304   | 0.151325 | 0 |
| fractal_dimension_mean  | 569 | 0.062798   | 0.007060   | 0.04996  | 0.0577   | 0.06154  | 0.06612  | 0.09744 | 0.112430 | 0 |
| radius_se               | 569 | 0.405172   | 0.277313   | 0.1115   | 0.2324   | 0.3242   | 0.4789   | 2.873   | 0.684432 | 0 |
| texture_se              | 569 | 1.216853   | 0.551648   | 0.3602   | 0.8339   | 1.108    | 1.474    | 4.885   | 0.453340 | 0 |
| perimeter_se            | 569 | 2.866059   | 2.021855   | 0.757    | 1.606    | 2.287    | 3.357    | 21.98   | 0.705448 | 0 |
| area_se                 | 569 | 40.337079  | 45.491006  | 6.802    | 17.85    | 24.53    | 45.19    | 542.2   | 1.127771 | 0 |
| smoothness_se           | 569 | 0.007041   | 0.003003   | 0.001713 | 0.005169 | 0.00638  | 0.008146 | 0.03113 | 0.426435 | 0 |
| compactness_se          | 569 | 0.025478   | 0.017908   | 0.002252 | 0.01308  | 0.02045  | 0.03245  | 0.1354  | 0.702884 | 0 |
| concavity_se            | 569 | 0.031894   | 0.030186   | 0        | 0.01509  | 0.02589  | 0.04205  | 0.396   | 0.946458 | 0 |
| concave_points_se       | 569 | 0.011796   | 0.006170   | 0        | 0.007638 | 0.01093  | 0.01471  | 0.05279 | 0.523077 | 0 |
| symmetry_se             | 569 | 0.020542   | 0.008266   | 0.007882 | 0.01516  | 0.01873  | 0.02348  | 0.07895 | 0.402407 | 0 |
| fractal_dimension_se    | 569 | 0.003795   | 0.002646   | 0.000895 | 0.002248 | 0.003187 | 0.004558 | 0.02984 | 0.697270 | 0 |
| radius_worst            | 569 | 16.269190  | 4.833242   | 7.93     | 13.01    | 14.97    | 18.79    | 36.04   | 0.297079 | 0 |
| texture_worst           | 569 | 25.677223  | 6.146258   | 12.02    | 21.08    | 25.41    | 29.72    | 49.54   | 0.239366 | 0 |
| perimeter_worst         | 569 | 107.261213 | 33.602542  | 50.41    | 84.11    | 97.66    | 125.4    | 251.2   | 0.313278 | 0 |
| area_worst              | 569 | 880.583128 | 569.356993 | 185.2    | 515.3    | 686.5    | 1084     | 4254    | 0.646568 | 0 |
| smoothness_worst        | 569 | 0.132369   | 0.022832   | 0.07117  | 0.1166   | 0.1313   | 0.146    | 0.2226  | 0.172491 | 0 |
| compactness_worst       | 569 | 0.254265   | 0.157336   | 0.02729  | 0.1472   | 0.2119   | 0.3391   | 1.058   | 0.618789 | 0 |
| concavity_worst         | 569 | 0.272188   | 0.208624   | 0        | 0.1145   | 0.2267   | 0.3829   | 1.252   | 0.766470 | 0 |
| concave_points_worst    | 569 | 0.114606   | 0.065732   | 0        | 0.06493  | 0.09993  | 0.1614   | 0.291   | 0.573549 | 0 |
| symmetry_worst          | 569 | 0.290076   | 0.061867   | 0.1565   | 0.2504   | 0.2822   | 0.3179   | 0.6638  | 0.213281 | 0 |
| fractal_dimension_worst | 569 | 0.083946   | 0.018061   | 0.05504  | 0.07146  | 0.08004  | 0.09208  | 0.2075  | 0.215154 | 0 |

