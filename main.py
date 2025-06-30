from auth import authenticate
from datetime import datetime
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Google Forms Quiz Generator")
parser.add_argument("--csv", type=str, default="Quiz.csv", help="CSV file with questions")
parser.add_argument("--count", type=int, default=10, help="Number of questions to include")

args = parser.parse_args()

df = pd.read_csv(args.csv)

service = authenticate()

today = datetime.today()
date_str = today.strftime("%d %B %Y")

form_data = {
    "info": {
        "title": f"Quiz: {date_str}",
        "documentTitle": "Auto-Created Quiz"
    }
}

created_form = service.forms().create(body=form_data).execute()

form_id = created_form["formId"]

print(" Form created successfully")
print(f"Form ID: {form_id}")
print(f"Edit URL: https://docs.google.com/forms/d/{form_id}/edit")
print(f"Public Quiz URL (share this with brother): https://docs.google.com/forms/d/{form_id}/viewform")

service.forms().batchUpdate(
    formId=form_id,
    body={
        "requests": [
            {
                "updateSettings": {
                    "settings": {
                        "quizSettings": {
                            "isQuiz": True
                        }
                    },
                    "updateMask": "quizSettings.isQuiz"
                }
            }
        ]
    }
).execute()

requests = []

for index, row in df.head(args.count).iterrows():
    question = row["question"]
    answer = str(row["answer"])

    requests.append({
        "createItem": {
            "item": {
                "title": question,
                "questionItem": {
                    "question": {
                        "required": False,
                        "textQuestion": {},
                        "grading": {
                            "pointValue": 1,
                            "correctAnswers": {
                                "answers": [{"value": answer}]
                            }
                        }
                    }
                }
            },
            "location": {"index": index}
        }
    })

service.forms().batchUpdate(
    formId=form_id,
    body={"requests": requests}
).execute()

print(" All questions added successfully")

remaining = df.iloc[args.count:]
remaining.to_csv(args.csv, index=False, quoting=1)
print(f" Remaining questions saved to '{args.csv}'")

