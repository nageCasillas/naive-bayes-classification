# Naive Bayes Classifier: Analyzing Eating Times
A repository for exploring eating habits using a Naive Bayes Classifier on the tips dataset. This project focuses on identifying patterns in dining times (e.g., lunch vs. dinner) and analyzing how various factors like bill size, gender, and day of the week influence these patterns.

The project features a Streamlit app for interactive data exploration and classification.

## About

This project aims to determine when users are eating (e.g., lunch or dinner) based on features from the tips dataset. By applying a Naive Bayes classifier, it highlights probabilistic relationships between dining times and attributes like:

- Total Bill: How the bill amount correlates with meal times.
- Gender: Differences in dining patterns by gender.
- Day: Weekday vs. weekend tendencies.
- Time of Service: Lunch vs. dinner classification.

## Features
- Eating Time Prediction: Predict whether a dining event corresponds to lunch or dinner based on the given features.
- Data Exploration: Visualize key trends, such as average bill amounts and tip sizes across different times and demographics.
- Interactive Interface: Experiment with the model by uploading datasets, adjusting parameters, and viewing predictions in real-time.

## Getting Started

To get started with this project, follow these steps:

### Prerequisites

- Python 3.x
- pip package manager

### Installation
1. Clone the repository: 
    ```bash
    git clone https://github.com/nageCasillas/naive-bayes-classification.git
    cd naive-bayes-classification
    ```
2. Install the required packages:
   ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
4. Open your browser and go to http://localhost:8501 to start interacting with the app.

## Contribution
Contributions are welcome! If you would like to contribute, please:

1. Fork this repository.
2. Create a new branch (feature-branch-name).
3. Make changes and test them.
4. Create a pull request.


