

# Gemstone Price Prediction 

## Overview:
This project aims to predict gemstone prices based on various characteristics such as carat weight, cut quality, color grade, clarity grade, and dimensions. By leveraging machine learning algorithms, the goal is to provide accurate price estimates to assist buyers, sellers, and enthusiasts in making informed decisions about gemstone transactions.

## Data:
The dataset contains information about 50,000 gemstones, including their unique identifiers, carat weights, cut qualities, color grades, clarity grades, dimensions, and prices. Sourced from a Kaggle competition, the data ensures quality and suitability for predictive modeling tasks.

## Approach:
### Data Exploration: 
Thorough exploratory data analysis (EDA) was conducted to understand feature distributions, identify missing values, detect outliers, and assess correlations between variables.

### Data Preprocessing: 
Various preprocessing techniques were applied, including handling missing values, addressing skewness, standardizing feature scales, and encoding categorical variables.

### Model Selection: 
Multiple machine learning algorithms, such as linear regression, random forest regression, gradient boosting regression, XGBoost regression, and LightGBM regression, were experimented with to identify the best-performing model.

### Model Training and Evaluation: 
The selected model was trained on preprocessed data and evaluated using metrics like Root Mean Square Error (RMSE) on both training and validation sets. Hyperparameter tuning further optimized performance.

### Model Deployment: 
The final trained model was deployed using ModelBit, allowing users to interact with it via a web application or API for real-time gemstone price predictions.

## Results:
### Model Performance: 
The deployed model achieved a validation RMSE of 613.39 and a test RMSE of 598.37, indicating accurate gemstone price predictions.

### Web Application: 
Access the web application using the provided URL ([here](https://gemstoneprice-od8y.onrender.com/)) to input gemstone characteristics and receive price predictions interactively. The web application is hosted on Render, ensuring reliability and accessibility

### Flutter Application: 
Integrate the Gemstone Price Prediction model into our Flutter mobile application by leveraging the ModelBit API. This allows us to programmatically request gemstone price predictions using HTTP POST requests.

## Contributors:
[Hogwarts Team]

