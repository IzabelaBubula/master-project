def main(args):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {
            "message": "Funkcja działa",
            "args": args
        }
    }
