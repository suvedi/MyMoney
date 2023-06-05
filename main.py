import requests
import io
from investment import *
import math

#define global variables to set up total amount in each category of investment
equity = float(0)
debt = float(0)
gold = float(0)

#percentage allocation
equilineItemsrcent = float(0)
debtPercent = float(0)
goldPercent = float(0)

initiatialAllocation = ''
sipInvestment = ''

def main():
    
    userInput = input('Enter 1 for input1.txt and 2 for input2.txt: ')
    #making it easier to choose input file. 1 == input1.txt, 2 == input2.txt
    if userInput == '1':
        processInput('input1.txt')
    elif userInput == '2':
        processInput('input2.txt')
    else:
        print('Invalid Number')

#process the input from file 
def processInput(fileName):
    main.equity = float(0)
    main.debt = float(0)
    main.gold = float(0)
    inv = Investment(0,0,0)

    with open(fileName, 'r') as file:
        for line in file:

            
            #get command lineItems, first item in each line
            lineItems = line.split()

            #check if line is blank
            if len(lineItems) == 0:
                #blank line, continue to next line
                continue
            
            #get command as first line item
            command = lineItems[0]
            
            #based on command lineItems, call appropriate functions 
            if command == 'ALLOCATE':
                #set investment and only invest if its January becase allocation happens in January based on provided assumptions
                #check if the format of the line is correct, it needs to have 4 items in it
                if len(lineItems) == 4:
                    initiatialAllocation = line
                    inv.totalInvestment.update({'equity': lineItems[1], 'debt': lineItems[2], 'gold': lineItems[3]})
                else:
                    print ('bad command, Allocate must start with ALLOCATE followed by three numbers for equity, debt and gold')
            elif command == 'SIP':
                sipInvestment = line
            elif command ==  'CHANGE':
                #if its January then allocate
                month = lineItems[4]
                if month == 'JANUARY':
                    inv.setInvestment(initiatialAllocation)
                else:
                    #SIP Starts from February but it will go up to january next year?
                    #I am making assumption here that the SIP allocation doesn't happen in january. 
                    #I will go with the assumption that SIP goes up to December but doesn't happen in January and gets updated from Feb next year
                    #set SIP investment except for January 
                    inv.setSIPInvestments(sipInvestment)
                    inv.setTotalInvestment()
                
                inv.changeInvestment(line)
                inv.setTotalInvestment()
                inv.setBalance(month)

            elif command ==  'BALANCE':
                month = lineItems[1]
                balanceForTheMonth = inv.balance(month)
                print(balanceForTheMonth[0], balanceForTheMonth[1], balanceForTheMonth[2])

            elif command ==  'REBALANCE':
                if(len(inv.monthbymonth) < 6):
                    print ('CANNOT_REBALANCE')
                else:
                    inv.rebalance()
                    print(inv.totalInvestment['equity'], inv.totalInvestment['debt'], inv.totalInvestment['gold'])
            elif command == '':
                print('invalid command')

#just a starter function to verify environment
def getMyIp():
    response = requests.get('https://httpbin.org/ip')
    print('Your IP is {0}'. format(response.json()['origin']))

#function to check if the input, TODO: remove later
def readInput():
    file= open('input1.txt', 'r')
    return file


if __name__ == "__main__":
    main()











