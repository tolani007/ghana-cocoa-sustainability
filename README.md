# ghana-cocoa-sustainability
What Ghana’s Cocoa Farmers Can Teach Silicon Valley About Sustainability: A data science investigation into cocoa yield, climate impact, and sustainable profitability.
# 🍫 Ghana Cocoa Sustainability Project

> I analyzed crop and climate data and uncovered a $20M mistake. Here’s how Ghana’s cocoa farmers beat the odds — in 3 charts.

## 📌 Goal
Use open-source climate and yield data to explore how Ghanaian cocoa farming can inspire sustainable agri-tech practices.

## 🗂️ Project Status
✅ Data collection done  
⏳ Cleaning + visualization in progress  
🚧 Cocoa profit simulator in development  
## 📦 Usage

This project uses `clean_merge.py` to prepare a merged dataset of cocoa yield, rainfall, and temperature (1961–2023) for Ghana.

### ▶️ To run the cleaning script:

Make sure you have Python and pandas installed.

```bash
pip install pandas

## 📁 Repo Structure (coming soon)
- `/data` - CSVs from FAOSTAT and World Bank  
- `/scripts` - Python cleaning + merging  
- `/notebooks` - Exploratory notebooks  
- `/streamlit_app` - Cocoa Profit Estimator
```

## 📈 Sneak Peek
Coming soon: Cocoa Yield vs. Rainfall (1961–2023) 📉


### 🧼 Scripts
- `clean_merge.py` — combines rainfall, temperature, and yield datasets (1961–2023)

  ## 📊 Exploratory Data Analysis (EDA)

All exploratory work and climate-yield trends are inside [`notebooks/eda.ipynb`](notebooks/eda.ipynb).  
This includes:

- Yield growth trends
- Scatter plots of climate vs yield
- Correlation matrix with key insights

📈 Cocoa Yield in Ghana (1961–2023)

![image](https://github.com/user-attachments/assets/b299db07-1d76-4caf-a8b3-4a4b17f9a329)


This chart shows how Ghana’s cocoa yield has evolved.
Notice the sharp rise post-2010 — could hint at better farming tech, improved seedlings, or policy changes.

Like a striker finding form, Ghana’s cocoa yields began scoring steadily after years of fluctuations.

Between 1986 and 1992, Ghana's cocoa yield experienced an upward trend due to several key factors:​

Economic Reforms and Producer Incentives: In 1983, Ghana implemented the Economic Recovery Program (ERP), which aimed to revitalize the economy, with a significant focus on agriculture. A crucial component of this program was increasing the producer prices for cocoa farmers, thereby enhancing their income and providing greater incentives to boost production. ​

My source url: https://en.wikipedia.org/wiki/Agriculture_in_Ghana?utm_source=chatgpt.com

Cocoa Rehabilitation Projects: The government launched initiatives to rehabilitate the cocoa sector, including compensating farmers for removing trees infected with the swollen shoot virus and encouraging the planting of new, higher-yielding varieties developed by the Cocoa Research Institute of Ghana. These efforts led to substantial rehabilitation and increased productivity. ​

My source url: https://researchonline.lshtm.ac.uk/id/eprint/4669424/7/Kolavalli-Vigneri-2011-Cocoa-in-ghana-shaping-the.pdf?utm_source=chatgpt.com

Infrastructure Improvements: Investments were made to repair and enhance transportation and distribution infrastructure, facilitating more efficient movement of cocoa beans from farms to markets. This development reduced post-harvest losses and improved market access for farmers. ​

My source url: https://en.wikipedia.org/wiki/Agriculture_in_Ghana?utm_source=chatgpt.com

Market Liberalization: In 1992, the Ghana Cocoa Board (Cocobod) shifted responsibility for domestic cocoa procurement to privately licensed companies, known as Licensed Buying Companies (LBCs). This move introduced competition into the internal marketing system, leading to more efficient purchasing and better prices for farmers. ​

My source url: https://researchonline.lshtm.ac.uk/id/eprint/4669424/7/Kolavalli-Vigneri-2011-Cocoa-in-ghana-shaping-the.pdf?utm_source=chatgpt.com

These combined efforts created a more favorable environment for cocoa production, leading to the observed increase in yields during this period.

​In the early 2000s, Ghana experienced a significant increase in cocoa yields, driven by several key factors:​

Cocoa Sector Reforms and Increased Farmer Incentives:

Higher Producer Prices: The government progressively raised the producer price of cocoa, aiming to return a higher percentage of the Free On Board (FOB) price to farmers. This policy sought to provide greater motivation for farmers to expand cocoa farming.

My source url: https://unctad.org/meetings/en/Presentation/SUC_MYEM2013_21032013_Ebenezer%20Tei%20Quartey.pdf?utm_source=chatgpt.com

Prompt Payment to Farmers: The introduction of Licensed Buying Companies (LBCs) in the internal marketing system led to increased competition, which in turn ensured prompt cash payments to farmers. ​

My source url: https://odi.org/documents/1305/592.pdf?utm_source=chatgpt.com

Mass Spraying and Disease Control Programs:

Mass Spraying Exercise (2001): The government initiated a nationwide mass spraying program to combat cocoa pests, particularly capsids, and diseases like black pod. This initiative significantly reduced crop losses and improved yields.​My source url: https://www.modernghana.com/news/273336/the-national-cocoa-diseases-and-pests-control-achievements.html?utm_source=chatgpt.com

Enhanced Fertilizer and Input Accessibility:

The government reintroduced fertilizer subsidy programs in the early 2000s to address declining soil fertility and stagnating production. These subsidies made fertilizers more affordable and accessible to smallholder cocoa farmers, leading to increased yields. ​

My source url: https://core.ac.uk/download/pdf/234661792.pdf?utm_source=chatgpt.com

Improved Cocoa Variety and Agronomic Practices:

The Cocoa Research Institute of Ghana (CRIG) developed and disseminated high-yielding, disease-resistant cocoa varieties. These new varieties matured earlier and were more resilient to prevalent diseases, contributing to higher productivity. ​

My source url: https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Ghana+Cocoa+Situation+Report_Accra_Ghana_10-06-2000.pdf&utm_source=chatgpt.com

Farmers received training and extension services on modern agronomic practices, including proper spacing, pruning, and pest management, which enhanced farm productivity. ​

My source url: https://www.researchgate.net/publication/281711886_The_new_Ghana_cocoa_boom_in_the_2000s_from_forest_clearing_to_Green_revolution?utm_source=chatgpt.com

Improved Infrastructure and Market Access:

Investments were made to rehabilitate and improve rural infrastructure, such as roads and storage facilities. These improvements facilitated more efficient transportation of cocoa beans to markets, reducing post-harvest losses and ensuring better prices for farmers. ​

Strong International Demand and Stable Export Environment:

The early 2000s saw an upward trend in world cocoa prices, which, combined with domestic policy reforms, created a favorable environment for cocoa exports. This stability and profitability in the export market further motivated farmers to invest in cocoa production. ​

These combined strategies led to significant productivity gains and drove the upward trend observed in Ghana’s cocoa yield during the early 2000s.



