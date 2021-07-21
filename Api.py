from flask import Flask, app
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

class Validate(Resource):

    def get(self,indentifier):

        indentifier = indentifier.replace("-","")
        # contains the check digit of every identifier
        check_digit = indentifier[-1]
       
        # removes the check digit from the number for calculations
        number = indentifier[:-1]
        result = 0
        counter = 1
        
        #BBC-V1
        if len(indentifier) == 10:
            for i in str(number):
                print(i)
                result = result + int(i)*counter
                result = result % 11
                counter+=1

            print(str(result))
            if str(result) ==  check_digit:
                return {'HTTP 200 Validated as BBC-V1': str(indentifier) }, 200
            elif result == 10 and check_digit.lower() == "x":
                return {'HTTP 200 Validated as BBC-V1': str(indentifier) }, 200
            else: return {'HTTP 400 Not Validated as BBC-V1 or BBC-V2': str(indentifier) }, 400 
        
        #BBC-V2
        if len(indentifier) == 13: 
            multiply = [1,3]
            summ = 0
            for index, digit in enumerate(list(str(number))):

                summ = summ + int(digit)*multiply[index%2] #%2 allows it to re-wrap in the multiply array.
                summ = summ % 10 
                final_sum = 10 - summ 
                final_sum = final_sum % 10
            
                
            if str(final_sum) ==  check_digit:
                return {'HTTP 200 Validated as BBC-V2': str(indentifier) }, 200
            else: return  {'HTTP 400 Not Validated as BBC-V1 or BBC-V2': str(indentifier) }, 400 

        else: return {"Invalid Input, Number should be 10 or 13 Digits": "HTTP 400"},400    

api.add_resource(Validate, "/Validate/<string:indentifier>")

if __name__ == "__main__":
    app.run(debug=True)
