# Book Recommendation System (Collaborative Filtering Based)

!(output.png)

## Overview
The **Book Recommendation System** utilizes collaborative filtering to provide personalized book recommendations based on user preferences. The system processes user interactions and recommends books that align with similar users' interests.

## Project Structure
```
📂 Book-Recommendation-System
├── 📂 data                # Folder containing dataset (to be unzipped here)
├── 📂 notebook            # Jupyter notebooks for data processing & model training
├── 📂 artifacts           # Stores trained models and processed data
├── app.py                 # Streamlit app for book recommendations
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```

## Setup Instructions

### 1. Install Dependencies
Ensure you have **Python 3.8+** installed. Install the required dependencies using:
```bash
pip install -r requirements.txt
```

### 2. Prepare the Dataset
- **Unzip the dataset** inside the `data` folder.
- Update the notebook to set the correct **data path** and **artifacts directory** before running.

### 3. Run the Jupyter Notebook
Navigate to the `notebook` directory and run the Jupyter Notebook to preprocess the data and train the model:
```bash
jupyter notebook
```
Make sure to set the correct **path** for fetching data and saving model artifacts.

### 4. Run the Streamlit App
Launch the Streamlit app using the following command:
```bash
streamlit run app.py
```
This will start a local web server where you can interact with the recommendation system.

## Features
- **Collaborative Filtering Algorithm**: Recommends books based on user interactions.
- **User-Friendly Interface**: Built using **Streamlit** for an interactive experience.
- **Model Training & Evaluation**: Preprocessed data and trained models are stored in the `artifacts` folder.

## Technologies Used
- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Jupyter Notebook**
- **Streamlit**

## Contribution
Feel free to contribute to the project by submitting issues or pull requests. Ensure to follow best coding practices and document any modifications.

## License
This project is licensed under the MIT License.

