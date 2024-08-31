from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import random


app = Flask(__name__)
CORS(app)


@app.route("/word-quiz/<category>/<int:quizCount>", methods=['GET'])
def read_item(category: str, quizCount: int):
    quizList = get_json(category, quizCount)
    return createSampleQuiz(quizList, quizCount)
    # return get_json(category, quizCount)
    # return quizList


def get_json(file_name, cout):
    full_path = f'JSON/{file_name}.json'

    with open(full_path, 'r', encoding='utf-8') as file:
        json_str = file.read()

    # 文字列をJSONオブジェクトに変換する
    data = json.loads(json_str)

    # 辞書のキーと値をリストとして取り出す
    items_list = list(data.items())
    random_items = random.sample(items_list, cout)

    return dict(random_items)


def createSampleQuiz(quizList, count):
    with open("sampleWords.json", 'r', encoding='utf-8 ') as file:
        json_str = file.read()

    data = json.loads(json_str)
    wordsList = data['descSample']
    randomWordsList = random.sample(wordsList, count * 3)
    newList = quizList

    # print(quizList)
    for key in quizList.keys():
        answer = quizList[key]['desc']
        words = random.sample(randomWordsList, 3)
        insert_index = random.randint(0, len(words))

        # 指定した位置に文字列を挿入
        # words.insert(insert_index, answer)
        wordObj = {}
        for word in words:
            wordObj[word] = False
            if word in randomWordsList:
                randomWordsList.remove(word)
            newList[key]['quizList'] = words
        wordObj[answer] = True
        newList[key]['quizList'] = wordObj
    return newList


def create():
    descArray = {
        "descSample": []
    }
    full_path = f'JSON/highschool3.json'
    with open(full_path, 'r', encoding='utf-8') as file:
        json_str = file.read()
    data = json.loads(json_str)
    keys = data.keys()
    for key in keys:
        descArray['descSample'].append(data[key]["desc"])

    with open('highschool3.json', 'w', encoding='utf-8') as file:
        json.dump(descArray, file, ensure_ascii=False, indent=4)


def shuffled():
    with open("data.json", "r") as file:
        json_file = file.read()

    json_data = json.loads(json_file)
    shuffled_strings = random.sample(
        json_data["descSample"], len(json_data["descSample"]))


if __name__ == '__main__':
    print("")
    # shuffled()
    app.run(debug=True)
    # create()
