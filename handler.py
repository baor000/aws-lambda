import json
import gspread


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }
    try:
        gc = gspread.service_account(filename="credentials/credentials.json")
        sheet = gc.open_by_url(event.get("url",""))
        worksheet = sheet.worksheet(event.get("name",""))
        col = worksheet.row_values(1)
        data2 = worksheet.get_all_records()
        for i,rec in enumerate(data2):
            rec["id_s"] = i 
        result_event = {
            "url":event.get("url"),
            "name": event.get("name"),
            "col": col,
            "rows": data2,
        } 
        return {"statusCode": 200, "body": json.dumps(result_event)}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({'message': str(e)})}