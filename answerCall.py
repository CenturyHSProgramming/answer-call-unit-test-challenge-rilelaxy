# answerCall.py
# by Riley Gregory

def answerCall(caller_code, sameAreaCode, cur_time):
    # hours from cur_time
    hours_string = cur_time.split(":")[0]
    hours = int(hours_string)

    # check if  call is after 10pm or before 7am
    if hours >= 22 or hours < 7:
        return False
    
    # caller is a telemarketer check
    if caller_code == "T":
        return False
    
    # caller is a relative or friend check
    if caller_code in ["F", "R"]:
        return True
    
    # unknown caller check and has the same area code
    if caller_code == "U" and sameAreaCode:
        return True
    
    return False

if __name__ == '__main__':
    # example test
    result = answerCall("U", True, "09:00")
    print(result)  # expected output is True
