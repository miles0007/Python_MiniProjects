
import pyinputplus as pyip
import random, time

# intialize number of question and
# Correct Ans count
numOfQues = 10
corrAns = 0

for i in range(numOfQues):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    # prompt in user input
    prompt = ('%s X %s = '%(num1,num2))
    try:
    	# when user enters the correct answer by checking in allowRegexes
    	# when user enters the wrong answer by checking in blockRegexes
    	# set the timeout in seconds and Limit for the answer
        user = pyip.inputStr(prompt, allowRegexes=['%s'%(num1*num2)],
                                     blockRegexes=[('.*', 'Incorrect!')],
                                     timeout=8, limit=3)
    
    # when TimeoutException occurs print the Message
    except pyip.TimeoutException:
        print("Session Expired")
    
    # when RetryLimitException occurs print the Message
    except pyip.RetryLimitException:
        print("Limit Exceeded")
    
    # if try block runs correctly without exceptions
    # increase the Ans count and print Meassage
    else:
        corrAns += 1
        print("Correct Congrats")
    # after the loop ends give a time gap of 1 second
    time.sleep(1)
print('Your have score is %s out of %s'%(corrAns,numOfQues))   
        
   

