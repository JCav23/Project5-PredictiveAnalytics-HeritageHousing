# ![Heritage Housing Logo](assets/img/house.png)

## Heritage Housing Issues

Welcome to Heritage Housing, a predictive analytics app designed and developed after being requested by a client to investigate a method of predicting house prices in Ames, Iowa. The app consists of a Machine Learning UI Dashboard created with Streamlit. The various pages explore the business requirements set out by the client including a study of the various data labels & how they correlate against the house sale price. It was created using various Python libraries for machine learning, data analysis and daata visualisation. 

Along side the dashboard there are multiple Jupyter notebooks outlining all the steps taken during the project from initial data exploration, the correlation study required under the buisness case, and entire workflow for developing a convential machine learning Regression model including data cleaning, feature engineering, modelling, and evaluation.
 
The project was built to address a full business case as led by the client, answering several buisness requirements agreed upon with them. This informative README, the UI dashboard and Jupyter notebooks created during the analysis all discuss how and why conclusions were drawn, and the methods used to achieve them, in varying level of details to cater to audiences with any level of technical knowledge.

The live site can be found [HERE](https://heritage-housing-prices-d6811e354989.herokuapp.com/)

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Business Requirements

As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.
* 3 - The client requires a UI dashboard to view the results of our study

## Project Hypothesis

*Hypothesis One*
- It is considered that the Lot area of the property would correlate positvely with the sale price.
- Conclusion: Correct 

*Hypothesis Two*
- It is considered that the overall condition of the property would positively correlate with the sale price.
- Conclusion: Correct

*Hypothesis Three*
-  It is considered that houses with a similar square footing but higher overall quality of materials and finish and a higher overall condition would have a higher sales price.
- Conclusion: Correct

*Hypothesis Four*
-  It is considered that those houses in a similar condition but with a higher number of bedrooms above grade, would have a higher sales price
- Conclusion: Unconfirmed

*Hypothesis Five*
- It is considered that houses of a similar size and number of bedrooms would have a higher sale price the more recently they were built.
- Conclusion: Unconfirmed

### Hypothesis Validation

#### Correlation Analysis
For hypotheses one and two, the easiest way to validate these will be through the correlation study carried out as part of addressing the first part of our business requirement. By using the Pearson & Spearman methods to calculate correlation levels for the features within our dataset and by generating heatmaps for the results we will be able to clearly confirm for each hypothesis whether the specified features are correlated or not as we assume.

#### Correlation Conclusion
Hypotheses One & Two were both confirmed as correct during our correlation study, details of which can be found in the dashboard or the jupyter notebooks. Plots were generated to display the features considered in our hypotheses against the Sale Price, which showed a positive correlation.

#### Regression Analysis 
Our next three hypotheses will require the finshed and optimized ML model to perform a regression analysis for the selected features. We can then specify the features we wish to keep the same and which we want to vary in order to test our hypotheses to confirm our deny our assumptions. 

#### Regression Conclusion
Our model was able to confirm Hypothesis three as correct, by varying the labels we wished to investigate in this case quality and condition, we were able to confirm that houses with a higher quality and condition have a higher sale price. 

Unfortunately we were unable to confirm hypotheses four and five. While we varied the features we aimed to investigate, our model is not powerful enough to be able to accurately predict the resulting difference in sale price. The features in question in this case number of bedrooms and year the houses were built in, did not prove to have enough importance when fitting and training the model to predict a change in sale price. Future iteration of the project should be led to strengthen the performance of the model, by futher optimizing hyperparameters with more current versions of the ML Libraries and by collecting more data to work with. 

## Rationalizing Machine Learning Tasks based on Business Requirements

*Business Requirement 1*

As a client I would like to view the outcome of the correlation study so that I can better understand how the different features of the data affect the target of the machine learning regression; `SalePrice`. There should be multiple visualisations displaying the features plot againt sale price so I can easily view the results graphically and draw conclusions quickly and efficiently.

*Business Requirement 2*

As a client I would like to be able to accurately predict the sale price for the inherited houses using a machine learning model to perform regression analysis to predict a fixed number based on the features of a house. I would also like to be able to pass new data in to be able to make any new predictions for houses in the future. 

*Business Requirement 3*

As a client I would like an an interactive dashboard to be able to access and view all results of the project, including data visualisations, machine learning pipeline steps, regression results and performance. The dashboard should contain sufficient explanation for all results if not already obviously apparant.

## ML Business Case

* Heritage Housing's primary goal is to develop a ML model that can acurately predict Sale Price from the housing records of the area. While the client understands the property market in her own residential area, using these insights may lead to inaccurate predictions for the houses she has inherited.
* The ML model will be trained on the publicly available dataset for housing records in Ames, Iowa containing attribute information for each house, and the models output will be the predicted sale price based on these features.
* The customer requires an interactive dashboard to view the data, plots, and model performance metrics. The dashboard should also allow for inputing records to predict housing prices for any additional houses in the area.
* There are no ethical or privacy concerns when it comes to using the data as it is a publicly available dataset. 
* The model success will be determined by the accuracy of its predictions using regression when predicting sale price which will be determined by the R<sup>2</sup> score of the regressor. 
* Validation of the models performance carried out by training and validating the model on our data that we have split into seperate train and test sets and determining the models ability to generalise for any data without underfitting or overfitting. 
* The project's success metric will be an R2 score of 0.75 or higher on both the train and test sets. 

### Crisp-DM
The workflow used throughout the project development complies with the cross-industry standard process for data mining or Crisp-DM. which is an open standard process model widely used within data analytics and data mining. It outlines the 6 stages used to provide a reliable and repeatable process within data science projects. These 6 steps are what help define our workflow and include Business Understanding, Data Understanding, Data Preparation, Modelling, Evaluation, Deployment

![Crisp-DM](https://miro.medium.com/v2/resize:fit:640/format:webp/1*sicHaDLyHRGuJm9eZTaHNw.png)

**Buisness Understanding**

The project goal was to produce a conventional machine learning regression model to successful predict housing prices based on records from the area. This is so the client who had inherited 4 house would be able to accurately predict their sale value. 

**Data Understanding**

The dataset was a publicly available dataset from Kaggle, an online platform for the data science and machine learning practitioner community. The data described various features of ~1400 houses in Ames, Iowa such as the number of bedrooms above ground, quality and condition of the houses, garage and basement details, and size of the building and property extents.

**Data Preperation**

The data was preprocess and cleaned to handle any features with missing values, encode categorical features, handle outlying values, and scale features appropriately, all to improve performance of the ML model. The data was then split into train and sets to train and validate the models performance.

**Modelling**

The business requirements showed that the model needed to perform a regression analysis to predict the sale price. The `ExtraTreesRegressor`; extended random decision forest model was chosen through cross validation searchs completed by SciKit Learn's `GridSearchCV` module. Hyperparameter optimization was then carried out to assess the optimal configuration of the model. A second pipeline was developed implementing Principle Componant Analysis, however this was shown to not perform as well. 

**Evaluation**

The main success metrics used to validate the models performance were the R<sup>2</sup> score for the regressor, and the Mean Absolute Error. The R<sup>2</sup> score threshold to determine a succesful model was outlined by the client and set as `0.75`, which our model exceeded.

**Deployment** 

The model was intergrated into a Streamlit dashboard which allowed for user input to define data for new housing records to make further predictions. The dashboard also displayed the correlation study requested by the client under another business requirement, the prediction for the 4 inherited houses as requested in the buisness requirement, and the model performance metrics.

## Dashboard Design

* 


## Bugs

* Pingouin (fixed)
    * During the feature engineering step of the machine learning work flow, the statistical package Pingouin was installed as part of generating QQ plots during the numerical transformer investigation. However, after the package was installed it became apparent that the most recent version of the package clashed with other dependencies already installed in the project. This was shown when rerunning all cells within the notebook previously successful cell outputs would instead throw errors. The solution was to install an older version of Pingouin which would successfully function alongside other dependicies. However one final issue arose, in which that due to deprecated modules within SciPy that Pingouin scripts utilize, I had to adjust the internal `plotting.py` script from Pingouin, to successfully run my project as desired.

* FitFailedWarning - Criterion (Fixed)
    * During the GridSearchCV process of hyperparameter optimization, the output was returning a `FitFailedWarning`. When deciding upon hyperparameters to optimize I was using the most current version of the SciKit Learn documentation, which lists Criterion as having several acceptable values available. However this project was built on the premade template provided by CodeInstitute, that uses older versions of the project dependencies including SciKit Learn. So after checking the appropriate version of the documentation it became apparent that only `mse` (Mean Square Error) and `mae` (Mean Absolute Error) are acceptable values for the Criterion parameter in this projects version dependency. Investigation was held into possibly using `mae` within the hyperparameter optimization however after it became apparent it drastically increases computational time to unwieldly levels, I decided against including it in the optimization and other parameters were chosen instead.

## Deployment

### Heroku

* The App live link is: <https://heritage-housing-prices-d6811e354989.herokuapp.com/>
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

### Main Data Analysis and Machine Learning Libraries

* [NumPy](https://numpy.org/doc/stable/index.html) - Fundamental scientific computing library used for processing data and calculation. Is a major dependency for other libraries such as Pandas and Pingouin
* [Pandas](https://pandas.pydata.org/docs/index.html) - Python analytics library for handling data primarily in the pandas DataFrame structure
* [Pingouin](https://pingouin-stats.org/build/html/index.html#) - Statistical Python package used for data analysis and plot generation, written on NumPy & Pandas
* [Matplotlib](https://matplotlib.org/stable/) - Statistical analysis library for python also used for data visualisations
* [Seaborn](https://seaborn.pydata.org/index.html) - Data visualisation library for generating statistical graphs (Heatmaps, Jointplots)
* [Plotly](https://plotly.com/graphing-libraries/) - Data visualisation library for generating interactive graphs (3D scatter, Scatter Matrix).
* [Scikit Learn](https://scikit-learn.org/stable/) - Library for conventional machine learning model development
### Other technologies
[Streamlit](https://docs.streamlit.io/) - Library for building interactive dashboard app
[Heroku](https://devcenter.heroku.com/) - Used for hosting and deployment of the dashboard
[Git/GitHub](https://docs.github.com/en) - Version control, and repository storage

## Credits

### Content

* The CodeInstitute Walkthrough project (Churnometer) and the various course material for the various data analytic and machine learning packages were refered to continually throughout development of this project. 
* https://github.com/van-essa/heritage-housing-issues/tree/main - example reference project provided by mentor
* [Stack Overflow](https://stackoverflow.com/) - Dozens of different stack overflow pages were refered to during development & troubleshooting.
* Documentation for the various libraries linked above were all referenced during development of the project & troubleshooting.

### Media

* The image of a house used on the dashboard and the readme introduction was obtained from [ShutterStock](https://www.shutterstock.com/) as a stock image.
* The Crisp-DM diagram was used from medium and is linked directly from the article. 

#### Acknowledgements 
* Paige, my other half who has kept me motivated throughout a rollercoaster of a development 
