# 🧠 Apriori Algorithm Project

This project implements the **Apriori Algorithm** in Python for mining frequent itemsets and generating association rules from transaction data. It features a custom implementation without relying on built-in data mining libraries.

The program accepts user-defined support and confidence thresholds to uncover frequent patterns and meaningful associations within a dataset.

---

## 📑 Table of Contents
- 🔍 [Features](#-features)  
- 🚀 [Getting-Started](#-getting-started)  
- ⚙️ [Usage](#-usage)  
- 🛠️ [Implementation-Details](#-implementation-details)  
- 📊 [Example-Output](#-example-output)  
- 📄 [License](#-license)

---

## 🔍 Features
- ✨ Accepts custom input for minimum support and confidence values  
- 📦 Processes transactional datasets to discover frequent itemsets  
- 🔗 Generates association rules from identified itemsets  
- ⏱️ Displays execution time to assess performance  

---

## 🚀 Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/apriori-algorithm.git
    cd apriori-algorithm
    ```

2. Run the script:
    ```bash
    python apriori.py
    ```

---

## ⚙️ Usage

When prompted, enter the minimum support and confidence thresholds (as decimals). The script will then analyze the dataset and output frequent itemsets and association rules.

Example:
```bash
Please enter minimum support: 0.2
Please enter minimum confidence: 0.5
