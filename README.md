#  House Price Prediction using Machine Learning

An end-to-end Machine Learning project that predicts house prices based on various house features such as bedrooms, bathrooms, living area, lot size, floors, condition, year built, and more.

The project includes data preprocessing, model training, evaluation, model serialization, and a modern web application built using Streamlit.

---

##  Features

-  Data Cleaning and Preprocessing
-  House Price Prediction using Linear Regression
-  Model Evaluation using Mean Squared Error (MSE) and R² Score
-  Saved Trained Model (.pkl)
-  Interactive Web Application using Streamlit
-  Modern Blue & Black User Interface

---

##  Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

---

##  Project Structure

```
House_price_prediction
│
├── data
│   └── data.csv
│
├── model
│   └── house_price_model.pkl
│
├── .streamlit
│   └── config.toml
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Dataset Features

The model predicts house prices using the following features:

- Bedrooms
- Bathrooms
- Living Area (sqft)
- Lot Size (sqft)
- Floors
- Waterfront
- View
- Condition
- Above Ground Area
- Basement Area
- Year Built
- Year Renovated

---

##  Data Preprocessing

The following preprocessing steps were performed before training the model:

- Checked for missing values
- Removed 49 houses with a price equal to **0**
- Selected important numerical features
- Split the dataset into training and testing sets (80% / 20%)

---

## Machine Learning Model

This project uses **Linear Regression**, a supervised machine learning algorithm used for predicting continuous numerical values.

The model learns the relationship between the input features and house prices by fitting the best possible linear equation to the training data.

### Final Model

- Linear Regression

---

##  Model Performance

After removing houses with a price of **0**, the model performance improved significantly.

| Metric | Score |
|---------|--------|
| Mean Squared Error (MSE) | **59,413,057,706.78** |
| R² Score | **0.6006** |

---

##  Streamlit Web Application

The application allows users to:

- Enter house details
- Click **Predict House Price**
- Instantly receive the estimated house price
- View the prediction in a modern interactive interface

---

##  Installation

### Clone the repository

```bash
git clone https://github.com/your-username/House_price_prediction.git
```

### Navigate to the project folder

```bash
cd House_price_prediction
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📷 Application Screenshots

### Home Page

> Add a screenshot of the home page here.

Example:

```
screenshots/home.png
```

---

### Prediction Result

> Add a screenshot of the prediction result here.

Example:

```
screenshots/prediction.png
```

---

##  What I Learned

Through this project, I learned:

- Data preprocessing and cleaning
- Feature selection
- Train-Test Split
- Linear Regression
- Model Evaluation using MSE and R² Score
- Saving trained models using Joblib
- Building interactive web applications using Streamlit
- Creating an end-to-end Machine Learning project

---

##  Future Improvements

- Improve feature engineering
- Add more relevant features
- Perform Cross Validation
- Try Polynomial Regression
- Compare different regression algorithms
- Deploy the application on Streamlit Cloud
- Enhance the UI with charts and analytics

---

##  Author

**Prabhash Kotilingala**

B.Tech Computer Science Engineering Student

Passionate about:

-  Machine Learning
-  Artificial Intelligence
-  Data Science
-  Generative AI
-  Agentic AI

---

##  Support

If you found this project helpful, please consider giving it a  on GitHub.

It motivates me to build more Machine Learning and AI projects.