import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def evaluateAsteroid():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    result =[]
    a_dict ={}
    for test_case in data['test_cases']:
        answer = asteroid(test_case)
        a_dict["input"] = test_case
        a_dict['score'] = answer[0]
        a_dict['origin'] = answer[1]
        result.append(a_dict)

    # result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    # return json.dumps(result)
    return jsonify(result)


def asteroid(astroidLine):
    # checking if the given asteroid line is palindrome

    answer = []
    # giving origin------------------
    lengthOfString = len(astroidLine)
    max = 0
    count = 0
    index = 1  #origin
    for j in range(1, lengthOfString - 1):
        character = astroidLine[j]
        if (astroidLine[j - 1] == character) and (astroidLine[j + 1] == character):
            for i in range(1, lengthOfString - 1):
                #checking both right and left of the middle]
                if (j-i >= 0) and (j+i < lengthOfString) and (astroidLine[j - i] == astroidLine[j + i]):
                    count+= 1
                elif count == 0:
                    break
                elif (j-i >= 0) and astroidLine[j - i] == character:
                    count+= 1
                elif (j+i < lengthOfString) and (astroidLine[j + i] == character):
                    count+=1
                else:
                    break
                
        if count > max:
            max = count
            index = j
        count = 0
        
#         origin = index
     #----------------------   
    
    character = astroidLine[index]
    total = 0
    left = index - 1
    right = index + 1
    score = 1
    eachsidecheck = True
    
    # CCCAAAB B BAAACCC
    while left >= 0 and right < lengthOfString:
        if eachsidecheck == True:
            if astroidLine[left] == character and astroidLine[right] == character:
                while left >= 0 and right < lengthOfString and astroidLine[left] == character and astroidLine[right] == character:
                    score += 2
                    left -= 1
                    right+= 1
                    
                eachsidecheck = False
                
                while left >= 0 and astroidLine[left] == character:
                    score += 1
                    left -= 1
                
                while right < lengthOfString and astroidLine[right] == character:
                    score += 1
                    right += 1

                if score < 7:
                    total = total + score
                elif score >= 7 and score < 10:
                    total = total + score*1.5
                else:
                    total = total + score*2
                
                if left >= 0 and right < lengthOfString:
                    character = astroidLine[right]
                    score = 0
                    eachsidecheck = True

    answer.append(int(total))
    answer.append(int(index))

    return answer
