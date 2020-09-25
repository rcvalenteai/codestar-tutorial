import json
import datetime

# add a comment

def handler(event, context):
    data = {
        'output': 'Hello World',
        'add': "Testing changes",
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
