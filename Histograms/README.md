## The provided code generates histograms to visualize the distribution of numerical data in a dataset using Python libraries like Pandas and Seaborn. It performs the following tasks:



- Imports necessary libraries such as Pandas, Matplotlib, and Seaborn.
- Reads a CSV file containing data into a Pandas DataFrame for analysis.
- Divides the columns into two types: numerical and categorical.
- Prints lists of numerical and categorical columns.
- Creates histograms for each numerical column using Seaborn's `sns.histplot()` function.
- Saves the histograms as image files in an 'output' directory.
- Closes each plot after saving to prepare for the next one.

---
### Histogram Descriptions

#### Distribution of Account Length
![Account Length Histogram](images/account_length_distribution.png)

Description: This histogram displays the distribution of account lengths in the dataset. The x-axis represents account length, while the y-axis represents frequency. The data appears to be somewhat uniformly distributed across different account lengths.

#### Distribution of Area Code
![Area Code Histogram](images/area_code_distribution.png)

Description: This histogram illustrates the distribution of area codes in the dataset. The x-axis represents area codes, while the y-axis represents frequency. It shows the distribution of customers across different area codes.

#### Distribution of Number of Voicemail Messages
![Number of Voicemail Messages Histogram](images/voicemail_messages_distribution.png)

Description: This histogram shows the distribution of the number of voicemail messages for customers. The x-axis represents the number of voicemail messages, while the y-axis represents frequency. It provides insights into how many voicemail messages customers typically receive.

#### Distribution of Total Day Minutes
![Total Day Minutes Histogram](images/total_day_minutes_distribution.png)

Description: This histogram depicts the distribution of total day minutes used by customers. The x-axis represents the total day minutes, while the y-axis represents frequency. It helps analyze the distribution of daytime call durations.

#### Distribution of Total Day Calls
![Total Day Calls Histogram](images/total_day_calls_distribution.png)

Description: This histogram visualizes the distribution of total day calls made by customers. The x-axis represents the total day calls, while the y-axis represents frequency. It provides insights into the number of daytime calls.

#### Distribution of Total Day Charge
![Total Day Charge Histogram](images/total_day_charge_distribution.png)

Description: This histogram displays the distribution of total day charges incurred by customers. The x-axis represents the total day charges, while the y-axis represents frequency. It helps analyze the distribution of daytime call charges.

#### Distribution of Total Evening Minutes
![Total Evening Minutes Histogram](images/total_evening_minutes_distribution.png)

Description: This histogram shows the distribution of total evening minutes used by customers. The x-axis represents the total evening minutes, while the y-axis represents frequency. It provides insights into evening call durations.

#### Distribution of Total Evening Calls
![Total Evening Calls Histogram](images/total_evening_calls_distribution.png)

Description: This histogram illustrates the distribution of total evening calls made by customers. The x-axis represents the total evening calls, while the y-axis represents frequency. It helps analyze the distribution of evening call activity.

#### Distribution of Total Evening Charge
![Total Evening Charge Histogram](images/total_evening_charge_distribution.png)

Description: This histogram visualizes the distribution of total evening charges incurred by customers. The x-axis represents the total evening charges, while the y-axis represents frequency. It helps analyze the distribution of evening call charges.

#### Distribution of Total Night Minutes
![Total Night Minutes Histogram](images/total_night_minutes_distribution.png)

Description: This histogram depicts the distribution of total night minutes used by customers. The x-axis represents the total night minutes, while the y-axis represents frequency. It provides insights into nighttime call durations.

#### Distribution of Total Night Calls
![Total Night Calls Histogram](images/total_night_calls_distribution.png)

Description: This histogram displays the distribution of total night calls made by customers. The x-axis represents the total night calls, while the y-axis represents frequency. It helps analyze the distribution of nighttime call activity.

#### Distribution of Total Night Charge
![Total Night Charge Histogram](images/total_night_charge_distribution.png)

Description: This histogram shows the distribution of total night charges incurred by customers. The x-axis represents the total night charges, while the y-axis represents frequency. It helps analyze the distribution of nighttime call charges.

#### Distribution of Total International Minutes
![Total International Minutes Histogram](images/total_international_minutes_distribution.png)

Description: This histogram illustrates the distribution of total international minutes used by customers. The x-axis represents the total international minutes, while the y-axis represents frequency. It provides insights into international call durations.

#### Distribution of Total International Calls
![Total International Calls Histogram](images/total_international_calls_distribution.png)

Description: This histogram visualizes the distribution of total international calls made by customers. The x-axis represents the total international calls, while the y-axis represents frequency. It helps analyze international call activity.

#### Distribution of Total International Charge
![Total International Charge Histogram](images/total_international_charge_distribution.png)

Description: This histogram displays the distribution of total international charges incurred by customers. The x-axis represents the total international charges, while the y-axis represents frequency. It helps analyze international call charges.

#### Distribution of Customer Service Calls
![Customer Service Calls Histogram](images/customer_service_calls_distribution.png)

Description: This histogram shows the distribution of customer service calls made by customers. The x-axis represents the number of customer service calls, while the y-axis represents frequency. It provides insights into customer service interaction frequency.

#### Distribution of Non-International Total Calls
![Non-International Total Calls Histogram](images/non_international_total_calls_distribution.png)

Description: This histogram depicts the distribution of non-international total calls made by customers. The x-axis represents the non-international total calls, while the y-axis represents frequency. It helps analyze call activity excluding international calls.

#### Distribution of Non-International Total Revenue
![Non-International Total Revenue Histogram](images/non_international_total_revenue_distribution.png)

Description: This histogram illustrates the distribution of non-international total revenue generated by customers. The x-axis represents the non-international total revenue, while the y-axis represents frequency. It provides insights into revenue generated from non-international calls.

#### Distribution of Non-International Total Minutes
![Non-International Total Minutes Histogram](images/non_international_total_minutes_distribution.png)

Description: This histogram visualizes the distribution of non-international total minutes used by customers. The x-axis represents the non-international total minutes, while the y-axis represents frequency. It helps analyze call durations excluding international calls.

#### Distribution of Total Calls
![Total Calls Histogram](images/total_calls_distribution.png)

Description: This histogram displays the distribution of total calls made by customers, including both international and non-international calls. The x-axis represents the total calls, while the y-axis represents frequency. It provides insights into overall call activity.

#### Distribution of Total Revenue
![Total Revenue Histogram](images/total_revenue_distribution.png)

Description: This histogram illustrates the distribution of total revenue generated by customers, including both international and non-international calls. The x-axis represents the total revenue, while the y-axis represents frequency. It helps analyze overall revenue.

#### Distribution of Total Minutes
![Total Minutes Histogram](images/total_minutes_distribution.png)

Description: This histogram visualizes the distribution of total minutes used by customers, including both international and non-international calls. The x-axis represents the total minutes, while the y-axis represents frequency. It provides insights into overall call durations.

# You can add more descriptions for other columns as needed...
