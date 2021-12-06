from num2words import num2words
from datetime import datetime
import humanize
import inflect
from pprint import pprint

a = input("Enter, number to convert into words:- ")
screen_name = input("Enter screen name to perform calculation:- ")

p = inflect.engine()

# Python function to convert number to words
def num2words_converter(data):
    response = {"message": None}
    if data:
        english_format = num2words(data, lang="en_IN")
        internation_format = num2words(data)
        individual = p.number_to_words(data, group=1)
        response.update(
            {
                "message": "Data converted successfully",
                "internation_format": internation_format,
                "english_format": english_format,
                "individual": individual,
            }
        )
    else:
        response.update({"message": "Please, enter valid data", "data": None})
    return response


# Python function to convert timestamp to date time
def convert_into_timestamp(timestamp):
    response = {}
    utc_datetime = datetime.utcfromtimestamp(timestamp)
    local_datetime = datetime.fromtimestamp(timestamp)
    diff = local_datetime - utc_datetime
    humanize_string = humanize.naturaltime(local_datetime)
    response.update(
        {
            "utc_datetime": utc_datetime.strftime("%A, %d %B %Y %I:%M:%S %p"),
            "local_datetime": local_datetime.strftime("%A, %d %B %Y %I:%M:%S %p"),
            "difference between your time to utc time": str(diff),
            "relative": humanize_string,
        }
    )

    return response


# Python function to convert timestamp to date time
def timestamp_to_datetime(timestamp):
    response = {}
    if len(timestamp) <= 10:
        result = convert_into_timestamp(int(timestamp))
        response.update(result)
        response.update({"timestamp_type": "we assuming your timestamp is seconds"})
    elif 10 < len(timestamp) <= 13:
        result = convert_into_timestamp(int(int(timestamp) / 1000))
        response.update(result)
        response.update(
            {"timestamp_type": "we assuming your timestamp is milliseconds",
             **result}
        )
    elif 13 < len(timestamp) <= 16:
        result = convert_into_timestamp(int(int(timestamp) / 1000000))
        response.update(result)
        response.update(
            {"timestamp_type": "we assuming your timestamp is microseconds"}
        )
    elif 16 < len(timestamp) <= 19:
        result = convert_into_timestamp(int(int(timestamp) / 1000000000))
        response.update(result)
        response.update({"timestamp_type": "we assuming your timestamp is nanoseconds"})
    else:
        response.update({"message": "Something went wrong"})
    return response

# Python function to convert date time to timestamp
def datetime_to_timestamp():
    response = {}
    to_timestamp = datetime.now()
    diff = to_timestamp - datetime.utcnow()
    response.update(
        {
            "timestamp_in_seconds": int(to_timestamp.timestamp()),
            "timestamp_in_milliseconds": int(to_timestamp.timestamp()) * 1000,
            "your_time": to_timestamp.strftime("%A, %d %B %Y %I:%M:%S %p"),
            "gmt_time": to_timestamp.utcnow().strftime("%A, %d %B %Y %I:%M:%S %p"),
            "difference between your time to utc time": str(diff)[:7],
        }
    )
    return response


actions = {
    "number_to_words": num2words_converter,
    "timestamp_to_datetime": timestamp_to_datetime,
    "datetime_to_timestamp": datetime_to_timestamp,
}

if __name__ == "__main__":
    # **** For number to words converter ***
    # if a.isdecimal():
    #     result = actions.get(screen_name)
    #     print(result(a))
    # else:
    #     result = actions.get(screen_name)
    #     print(result(a))

    # result = actions.get(screen_name)
    # print(result(a))
    result = actions.get(screen_name)
    pprint(result())
