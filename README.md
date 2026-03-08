# Fraud_Detection_ML_capstone_project

Project Overview

This project presents a Machine Learning-based Fraud Detection System designed to identify fraudulent financial transactions.  
The system analyzes transaction-level features and predicts whether a transaction is legitimate or fraudulent.

The primary objective is to minimize false negatives (missed fraud cases) while handling highly imbalanced data effectively.


Business Problem

Financial institutions face significant losses due to fraudulent transactions.  
Traditional rule-based systems fail to capture complex interactions between features.

This project builds an intelligent ML system that:

- Detects fraudulent transactions
- Handles imbalanced datasets
- Reduces financial losses
- Supports real-world deployment



Dataset Information

- Dataset: `transaction_fraud.csv`
- Target Variable: `is_fraud`
    - 0 → Legitimate Transaction
    - 1 → Fraudulent Transaction
- Highly imbalanced dataset

Performed:
- Data inspection (`info`, `describe`)
- Duplicate & missing value checks
- Class distribution analysis


Data Preprocessing

- Feature & target separation
- Stratified Train-Test Split (70%-30%)
- OneHotEncoding for categorical variables
- Scaling of numerical features
- Implemented using `ColumnTransformer`
- Pipeline used to prevent data leakage


Models Implemented

1. Logistic Regression
2. Random Forest
3. XGBoost

Evaluation Metrics:
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC


Model Comparison 

| Model | Recall | F1 Score | ROC-AUC |
|--------|--------|----------|----------|
| Logistic Regression | 0.50 | 0.30 | 0.71 |
| Random Forest | 0.18 | 0.22 | - |
| XGBoost | 0.96 | 0.20 | 0.71 |

Final Model Selected: XGBoost
Reason:  
XGBoost achieved the highest Recall (0.96), which is critical in fraud detection since missing fraudulent transactions results in financial loss. Although accuracy was lower, minimizing false negatives was prioritized over overall accuracy.


Deployment

The model is deployed using 'Streamlit'.
The application allows users to input transaction features and receive real-time predictions for fraud detection.

Project links 
GitHub Repository:
https://github.com/ayushmanral10-crypto/Fraud_Detection_ML_capstone_project.git

Live Streamlit App Link:
https://frauddetectionmlcapstoneproject-nznayscn9kttgbsdeywyxq.streamlit.app/


Project Structure

Fraud_App/
│
├── app.py
├── fraud_model.pkl
├── requirements.txt
├── README.md


Future Improvements

- Hyperparameter tuning (GridSearchCV / RandomSearch)
- Real-time fraud detection API


Business Impact

- Reduced financial losses
- Improved fraud detection capability
- Enhanced customer trust
- Automated risk monitoring
- Scalable fraud prevention system


Author

Ayush Manral  
Capstone Project – 2026  


Conclusion

Successfully built and deployed a machine learning-based fraud detection system capable of handling imbalanced datasets and detecting high-risk fraudulent transactions using XGBoost.
