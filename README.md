# 💼 Salary Prediction Scikit-Learn Model

A machine learning project that predicts employee monthly salaries based on professional and demographic factors using scikit-learn's Ridge Regression model.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Project Structure](#project-structure)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [License](#license)

## 🎯 Project Overview

This project builds a predictive machine learning model to estimate an employee's monthly salary based on key factors such as:
- Years of experience
- Education level
- Age
- Job level

The model uses **Ridge Regression** from scikit-learn, which is effective for regression problems and helps prevent overfitting through regularization.

## 📊 Dataset

**Source:** `employee_salary_dataset.csv`

**Dataset Size:** 50 employee records

**Key Columns:**
- `EmployeeID` - Unique identifier
- `Name` - Employee name
- `Department` - Department (Marketing, Operations, IT, Finance, HR, HR)
- `Experience_Years` - Years of professional experience
- `Education_Level` - Highest education (High School, Bachelor, Master, PhD)
- `Age` - Employee age (range: 22-57)
- `Gender` - Gender information
- `City` - Location (Delhi, Bangalore, Mumbai, Hyderabad, Chennai)
- `Monthly_Salary` - Target variable (range: $28,420 - $149,123)

**Data Statistics:**
- Average Experience: 9.9 years
- Average Age: 39.76 years
- Average Monthly Salary: $82,288.80

## ✨ Features

The model uses the following features for prediction:
1. **Experience_Years** (numeric) - Years of work experience
2. **Education_Level** (encoded) - 0=High School, 1=Bachelor, 2=Master, 3=PhD
3. **Age** (numeric) - Employee age

## 🚀 Installation

### Requirements
- Python 3.7+
- pandas
- numpy
- scikit-learn
- streamlit (for the web app)

### Setup

```bash
# Clone the repository
git clone https://github.com/Abu-Bakar-Farooq/Salary-Prediction-Scikit-Model.git
cd Salary-Prediction-Scikit-Model

# Install dependencies
pip install pandas numpy scikit-learn streamlit
