
# Automated Google Form Quiz

## 💡 Motivation

My younger cousin is quite fidgety and often avoids practice. But one day, I gave him a quiz through a Google Form instead of paper — and the novelty actually got him to engage with it.

Seeing how well it worked, I wanted to create more such quizzes, but making them manually was tedious and time-consuming. So, I built this program to automate quiz creation. I hope this keeps him hooked for a little while longer.

## 📦 Overview

This is a Python script that generates Google Form quizzes using the Google Forms API. It reads questions from a CSV file, creates a form, sets correct answers, and returns links for sharing or editing.

## ⚙️ Features

- Read questions/answers from CSV
- Create Google Form quizzes programmatically
- Limit number of questions (e.g., 10 per quiz)
- Prevent reuse by removing used questions
- Command-line arguments using `argparse`

## 💻 Usage

Make sure you have `credentials.json` in your project folder and you've authenticated once.

Run the script like this ->

Example Input:

```bash
python main.py --csv Quiz.csv --count 15
```
Example output:
```bash
***Form created successfully***
Form ID: 1WuBQwIhMTP_p7m27l58Ui5hgvsu6ZPO0
Edit URL: https://docs.google.com/forms/dhfdBQxwIh_bjf7m2wvl58UlYhfjsdsYKIzxNu6ZPO0/edit
Public Quiz URL: https://docs.google.com/forms/d/1knlfdTPsYfgsfS_sdhd_ncjsghfZPO0/viewform
***All questions added successfully***
***Remaining questions saved to 'Quiz.csv'***
```
Now one can share the 'Public Quiz URL'.

## 📁 CSV Format

The script expects a CSV file with two columns: `question` and `answer`.

Each row represents one quiz question and its correct answer. Here's an example:

```csv
"question","answer"
"What is 256 + 256?","512"
"Whats the LCM of 12 and 15","60"
"5 * 6 equals?","30"
.
.
.
```

## 🧱 Requirements

- A Google account with Google Forms API enabled
- `credentials.json` file from your Google Cloud Console

Install all dependencies using:

```bash
pip install -r requirements.txt
```
***


