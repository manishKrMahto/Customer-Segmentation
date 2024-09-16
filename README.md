# Customer Segmentation Dashboard 🚀

This project is an end-to-end analysis and customer segmentation system using exploratory data analysis (EDA) and K-Means clustering. The **Streamlit** app offers a dynamic dashboard for visualizing customer purchasing behavior.

## 🔑 Key Features

1. **Interactive Filters**: 
   - Filter customers by **Country**, **Month**, and **Day** for targeted analysis.
2. **Data Insights**:
   - **Amount Spent** and **Purchase Frequency** visualized across clusters.
3. **Clustering**:
   - Customers are grouped into distinct clusters using **K-Means** based on their purchasing behavior.
   
## 🧠 Model Building

- **Feature Scaling**: Standardized **AmountSpent** and **Purchase Frequency** using `StandardScaler`.
- **K-Means Clustering**: Determined the optimal number of clusters by analyzing **WCSS** (Within-Cluster Sum of Squares) and selecting **n_clusters = 5**.
- **Segmentation**: Customers are segmented into 5 clusters, with **0.0** representing high frequency buyers and **1.0** representing high spenders.

## 📊 Visual Insights

- **Before Clustering**: Scatter plot of **AmountSpent** vs **Frequency** to understand raw data.
- **After Clustering**: Visualized distinct clusters using color-coded scatter and strip plots.


## ⚙️ Tech Stack

- **Streamlit**: For interactive dashboard creation.
- **Seaborn & Matplotlib**: For detailed visualizations.
- **Pickle**: For loading preprocessed data.
- **K-Means (Sklearn)**: To segment customers into clusters.
- **StandardScaler**: For feature scaling.

## 🏗️ Future Enhancements

- Apply machine learning models for further customer behavior prediction.
- Introduce advanced filtering, prediction, and recommendations.

## 🛠️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/manishKrMahto/Customer-Segmentation
   cd Customer-Segmentation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```