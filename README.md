<h1 align="center" >SWIGGY-Analytics</h1>
                                              
🔘 **Introduction**

In the ever-evolving food delivery landscape, understanding the dynamics of popular platforms like **swiggy.com** is crucial for making informed decisions. By employing web scraping techniques to gather data on restaurant ratings, cuisine, and pricing, valuable insights and recommendations can be generated. This analysis not only aids in evaluating the viability of opening a remote kitchen in Bangalore but also offers broader industry insights, including area-wise distribution of restaurants, affordable and upscale options for various cuisines, and the prevalence of different culinary offerings.

🔘 **Aim of the study**

The aim of this study is to analyze data collected from swiggy.com, a food delivery platform, using web scraping techniques. The objective is to generate insights and recommendations for opening a remote kitchen in Bangalore, as well as provide broader industry insights such as area-wise restaurant distribution and affordable and upscale options for various cuisines.

🔘 **Data Source**

The data source used for this analysis is SWIGGY, a popular food delivery platform, specifically focusing on the Bangalore region. The data was collected by scraping the relevant information from the SWIGGY website using the Beautiful Soup library. The scraping process was carried out using Jupyter Notebook, a widely used programming environment for data analysis and exploration. The collected data includes details such as restaurant IDs, names, links, prices for two people, ratings, cuisines, dishes, and their corresponding prices.

🔘 **Data Description**

Before conducting the analysis, the data was scraped from **swiggy.com** using the **Beautiful Soup** library. The scraped data was then processed and saved into CSV files using the **Pandas** library, creating separate dataframes for restaurants and dishes. These dataframes provide the foundation for further analysis and insights into the restaurant and cuisine landscape on the food delivery platform.

<img src="https://i.ibb.co/Yb5FgnT/Swiggy-Scrapping-1.png" alt="Swiggy-Scrapping-1" border="0"><br>
<img src="https://i.ibb.co/mDspsNG/Swiggy-Scrapping-2.png" alt="Swiggy-Scrapping-2" border="0"><br>
<img src="https://i.ibb.co/X233D0g/Swiggy-Scrapping-3.png" alt="Swiggy-Scrapping-3" border="0">

The first CSV contains data on restaurants, including columns such as restaurant ID, restaurant name, restaurant link, price for two people, ratings, and the cuisines they serve. This table provides an overview of the restaurants available on the food delivery platform.

The second CSV contains information on dishes offered by the restaurants. It includes columns such as restaurant ID, restaurant name, dishes, cuisines, and the price of each dish. This table provides detailed information about the specific dishes offered by each restaurant.


🔘 **Methodolgy**

The methodology for creating a dashboard based on the provided CSV data can involve the following steps:

1. Data Collection: Extract the data from the CSV files and load it into a suitable data analysis tool or programming language.

2. Data Cleaning and Transformation: Clean the data by handling missing values, removing duplicates, and transforming it into a suitable format for analysis. Perform any necessary data preprocessing tasks.

3. Data Analysis: Utilize descriptive and exploratory data analysis techniques to uncover patterns, trends, and insights within the data. Calculate summary statistics, visualize data distributions, and explore relationships between variables.

4. Dashboard Development: Develop a dashboard using a suitable visualization tool such as Tableau, Power BI, or Python libraries like Plotly or Dash. Design the dashboard to effectively communicate the key insights and recommendations derived from the data analysis, utilizing appropriate charts, graphs, and interactive elements.

🔘 **Dashboard**<br>

<img src="https://i.ibb.co/6n8MdVT/Swiggy-Analytics-dashboard.png" alt="Swiggy-Analytics-dashboard" border="0"><br>
This dashboard provides a comprehensive overview of the food delivery platform's data. It showcases the top 5 locations with the highest count of restaurants, allowing users to identify popular areas. Additionally, it highlights the top 5 restaurants for each type of cuisine, aiding in the exploration of diverse culinary options. The treemap visualization illustrates the distribution of restaurants, while the location-wise breakdown of restaurants with reviews exceeding 1000 offers insights into highly reviewed areas.

🔘 **Visualizations**<br>

<img src="https://i.ibb.co/4Z1Hdkd/Location-wise-number-of-restaurant-where-ratinf-is-greater-than-1000.png" alt="Location-wise-number-of-restaurant-where-ratinf-is-greater-than-1000" border="0">
<p>Indiranagr restaurants top in sum of rating count followed by other locations..</p>
<img src="https://i.ibb.co/QHpdF3G/Top-5-number-of-restaurant-for-each-type-of-cuisine.png" alt="Top-5-number-of-restaurant-for-each-type-of-cuisine" border="0">
<p>Beverages are the most orderd followed by Desserts, Snacks, South Indian & Chineses respectively.</p>
<img src="https://i.ibb.co/zfbJxhz/Location-wise-distribution-of-Restaurant.png" alt="Location-wise-distribution-of-Restaurant" border="0">
<p>Most restaurants are listed in Indiranagar followed by Layout, Koromangala, Jayanagar, Basvanagudi respectively.</p>

🔘 **Findings**

1. Beverages, Desserts, Indian & Biryani cuisine has the greatest number of restaurants
2. Clients can keep dishes related to this cuisine so that more consumers will get attracted to their restaurant
3. Most popular restaurant by ratings: Malabar Bay
4. Adugodi, Basavana Gudi, Basaveshwara Nagar - These areas have more number of restaurants, we can assume that more consumers are from these areas
5. Indira Nagar, Koramangala, Basaveshwara Nagar has a greater number of expensive restaurants based on average price. 


🔘 **Summary**

The analysis conducted on the data from SWIGGY.com aims to provide valuable insights for making informed decisions about opening a remote kitchen in Bangalore. By examining the dataset, key information regarding the distribution of restaurants across different areas, the affordability of restaurants for various cuisines, and the quantity of restaurants available for each cuisine will be obtained. These insights are vital for assessing the viability of a remote kitchen and offer valuable industry insights for the broader food delivery sector.

🔘 **Challenges Faced**

During the analysis, I may have faced challenges including data quality issues, website structure complexities, managing large data volumes, legal and ethical considerations, and interpreting the data for meaningful insights. Ensuring the accuracy and completeness of the scraped data while handling dynamic website elements can be demanding. Additionally, complying with legal and ethical boundaries, optimizing code, and addressing changing website structures require careful attention. Analyzing and interpreting the data, as well as maintaining technical expertise, are crucial for overcoming these challenges and deriving valuable insights from the project.
