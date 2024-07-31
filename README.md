# ![Heritage Housing Logo](assets/img/house.png)

## Heritage Housing Issues

Welcome to Heritage Housing, a predictive analytics app designed and developed after being requested by a client to investigate a method of predicting house prices in Ames, Iowa. The app consists of a Machine Learning UI Dashboard created with Streamlit. The various pages explore the business requirements set out by the client including a study of the various data labels & how they correlate against the house sale price. It was created using various Python libraries for machine learning, data analysis and daata visualization. 

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

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

## ML Business Case

* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)

## Bugs

* Pingouin
* FitFailedWarning - Criterion

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site



