# Sales Analysis and Optimizing Business Strategy with Power BI

## 🚀 Project Overview
This project leverages **data collection**, **SQL preprocessing**, and **Power BI** to deliver in-depth **sales analytics** and **performance optimization**. It includes web-scraped news data, sales trends, and insights into Power BI performance using the **Performance Analyzer**.

## 🎯 Objectives
1. **Data Integration**: Combine dataset-based and web-scraped data sources.
2. **Data Cleaning & Preprocessing**: Perform preprocessing directly in **SQL** for structured analysis.
3. **Sales Analysis**: Explore sales trends across categories, segments, regions.
4. **Power BI Performance Tuning**: Use **Performance Analyzer** to optimize report speed and responsiveness.
5. **Interactive Dashboards**: Build visually rich and interactive Power BI dashboards.
6. **Comprehensive Documentation**: Maintain clear documentation for every step of the process.

---

## 📁 Project Structure

### **1. `Collecting the Data/`**
- **Collected Data** from:
  - Historical **Sales Dataset**
  - **Web-scraped news articles** relevant to market trends
- Converted raw data into structured format using **Pandas**
- Uploaded structured data to **SQL database**

### **2. `Cleaning and Preprocessing/`**
- Conducted **data cleaning and transformation in SQL**.
- Removed missing values, standardized data types, and normalized features.
- Exported cleaned data for downstream analytics.

### **3. `Mining and Analysing/`**
- Built Power BI visualizations:
  - Sales by Region, Segment, Category
  - Trend over time (monthly, yearly)
  - Profit and Quantity distribution
  - Heatmaps and Tree Maps for profitability
- Power BI `.pbix` file is stored here.

### **4. `Collecting the Power BI Performance through Performance Analyzer/`**
- Used **Performance Analyzer** in Power BI to:
  - Log load time per visual
  - Optimize slow-performing visuals
  - Improve report responsiveness
- Logs and results stored here for reference.

### **5. `Documentation of the Project/`**
- Complete **project documentation**, including:
  - Data flow
  - Tools and technologies
  - Key visual insights
  - Screenshots of dashboards
  - Performance tuning strategies

---

## 🪠 Setup & Installation

### ✅ Prerequisites
- **Python 3.8+**
- **MySQL Server**
- **Power BI Desktop** ([Download here](https://powerbi.microsoft.com/en-us/desktop/))
- Python libraries:
  ```bash
  pip install pandas requests beautifulsoup4 mysql-connector-python
  ```

### 📦 Clone the Repository
```bash
git clone https://github.com/NukaNarendra/SalesAnalysisAndOptimisingPowerBI.git
cd SalesAnalysisAndOptimisingPowerBI
```

---

## 💡 How to Run the Project

### **Step 1: Collect the Data**
```bash
# Inside 'Collecting the Data' folder
python collect_data.py
```
- Uses `pandas`, `requests`, and `BeautifulSoup` to scrape news articles and merge them with sales dataset.
- Converts and uploads data to SQL.

---

### **Step 2: Clean and Preprocess in SQL**
- SQL scripts are executed manually or via Python.
- Cleaned data is saved in SQL and exported to CSV for analysis.

---

### **Step 3: Analyze in Power BI**
- Open `Mining and Analysing/SalesAnalysis.pbix` in Power BI Desktop.
- Click **Refresh** to load the latest cleaned data.
- Explore dashboards with interactive filters.

---

### **Step 4: Collect Power BI Performance Logs**
- Navigate to **View → Performance Analyzer** in Power BI.
- Start recording and export logs.
- Logs are stored in `Collecting the Power BI Performance through Performance Analyzer/`.

---

### **Step 5: Read Documentation**
- Go to `Documentation of the Project/` for:
  - Process flow diagrams
  - Screenshots of each dashboard section
  - Performance analysis notes
  - Model explanation and improvement steps

---

## 📊 Key Visuals in Power BI
- **Sales Overview**: Total Sales, Profit, Quantity
- **Time Series**: Monthly and Yearly breakdown
- **Profit Heatmap**: Region-wise performance
- **Top N Analysis**: Best-selling categories and products
- **Performance Analyzer Results**: Load times and optimizations

---

## ✅ Expected Deliverables
✔ Combined dataset and news insights.  
✔ Cleaned and processed data in SQL.  
✔ Power BI dashboards showing sales intelligence.  
✔ Performance optimization using Power BI analyzer.  
✔ Complete project documentation with visuals.

---

## 👥 Contributors
- Contributions are welcome!  
Feel free to open issues or pull requests to improve the data pipeline, dashboard, or documentation.

