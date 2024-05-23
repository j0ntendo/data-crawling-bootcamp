# Data Crawling Bootcamp

This repository contains a collection of Python scripts developed during a data crawling bootcamp. The scripts use various libraries including `selenium`, `webdriver_manager`, `pandas`, and `BeautifulSoup` to scrape data from different websites such as Naver Shopping, Instagram, Naver News, Google Play Store, and YouTube.

## Prerequisites

Before running any scripts, ensure you have the necessary libraries installed. You can install them using the following commands:

```bash
pip install selenium
pip install webdriver_manager
pip install pandas
pip install beautifulsoup4
```

## Scripts Overview

### 1. Chrome.py

This script scrapes product data from Naver Shopping.

- **URL:** [Naver Shopping](https://search.shopping.naver.com/)
- **Data Scraped:** Product names, prices, and categories.
- **Output:** `애견용품.csv`

#### How to Run

```bash
python chrome.py
```

### 2. Instagram.py

This script scrapes Instagram comments for a specified hashtag.

- **URL:** [Instagram](https://www.instagram.com/)
- **Data Scraped:** Comments on posts with a specific hashtag.
- **Output:** `insta.csv`

#### How to Run

```bash
python instagram.py
```

### 3. Naver_news.py

This script scrapes news articles from Naver News based on a search query.

- **URL:** [Naver News](https://search.naver.com/)
- **Data Scraped:** Article titles, links, and descriptions.
- **Output:** `test.csv`

#### How to Run

```bash
python naver_news.py
```

### 4. Playstore.py

This script scrapes reviews and ratings from a specified app on the Google Play Store.

- **URL:** [Google Play Store](https://play.google.com/)
- **Data Scraped:** Review text and star ratings.
- **Output:** `bae_review.csv`

#### How to Run

```bash
python playstore.py
```

### 5. Youtube.py

This script scrapes video titles and view counts from YouTube based on a search query.

- **URL:** [YouTube](https://www.youtube.com/)
- **Data Scraped:** Video titles and view counts.
- **Output:** `연세대학교.csv`

#### How to Run

```bash
python youtube.py
```

