## Overview

HealthAnalyzer is a web application built with Streamlit that analyzes food items from images and provides insights into their nutritional content. It utilizes Google's Generative AI (Gemini Pro Vision API) to analyze images and extract information about food items present in them. Additionally, it fetches the latest health updates from the SERP API to keep users informed about current health trends and news.

## Features

- **Image Analysis**: Upload an image containing food items, and HealthAnalyzer will analyze it to identify the food items present.
- **Calorie Calculation**: HealthAnalyzer calculates the total calories of the food items detected in the image.
- **Nutritional Insights**: Get detailed insights into the nutritional content of each food item, including calorie intake.
- **Latest Health Updates**: Stay informed about the latest health updates and news fetched from the SERP API.

## How to Use

1. **Upload Image**: Choose an image containing food items.
2. **Click "Tell me the total calories"**: HealthAnalyzer will analyze the image and provide insights into the nutritional content.
3. **View Results**: The app will display the total calories of the food items detected in the image and provide additional nutritional insights.
4. **Explore Health Updates**: Scroll down to view the latest health updates fetched from the SERP API.

## Installation

1. Clone the repository:

```
git clone <link to your repository>
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Create a .env file and add your API keys:
```
GOOGLE_API_KEY=your_google_api_key
SERP_API_KEY=your_serp_api_key
```

4. Run the Streamlit app:
```
streamlit run main.py
```

## Technologies Used
- Python
- Google Gemini
- Streamlit
- Serp API

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

