import json


def generate(test_details, tests, jsonfile_directory_path):
    li = []
    li.append(test_details)
    for test in tests:
        dict = {"name": test.name,
                "description": test.description,
                "start_time": test.start_time,
                "end_time": test.end_time,
                "duration": test.duration,
                "result": test.result,
                "priority": test.priority,
                "logs": test.logs}
        li.append(dict)

    with open(jsonfile_directory_path, 'w') as json_file:
        json.dump(li, json_file)
