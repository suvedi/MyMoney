import unittest
import io
from main import *
from investment import *



class AllocationTest(unittest.TestCase):

    def test_initial_allocation(self):
        inv = Investment(0,0,0)
        allocationLine = 'ALLOCATE 6000 3000 1000'
        inv.setInvestment(allocationLine)
        self.assertEqual(inv.equity, 6000)
        self.assertEqual(inv.debt, 3000)
        self.assertEqual(inv.gold, 1000)
        
    #calculate equity, debt and gold based on % change
    def test_change_rate(self):

        allocationLine = 'SIP 6000 3000 1000'
        sipPayment = 'SIP 2000 1000 500'
        change = 'CHANGE 4.00% 10.00% 2.00% JANUARY'
        
        objChange = Investment(0,0,0)
        objChange.setInvestment(allocationLine)

        #additional investment on the month
        objChange.setSIPInvestments(sipPayment)
        #investments should be sum of initial investment and sip monthly investment
        self.assertEqual(objChange.equity, 8000)
        self.assertEqual(objChange.debt, 4000)
        self.assertEqual(objChange.gold, 1500)

        objChange.changeInvestment(change)

        self.assertEqual(objChange.equity, 8320)
        self.assertEqual(objChange.debt, 4400)
        self.assertEqual(objChange.gold, 1530)

    #sip allocation is monthly payment to the investments,
    def test_sip_allocation(self):
        allocationLine = 'SIP 6000 3000 1000'
        sipPayment = 'SIP 2000 1000 500'
        inv = Investment(0,0,0)
        inv.setInvestment(allocationLine)
        #additional investment on the month
        inv.setSIPInvestments(sipPayment)
        #investments should be sum of initial investment and sip monthly investment
        self.assertEqual(inv.equity, 8000)
        self.assertEqual(inv.debt, 4000)
        self.assertEqual(inv.gold, 1500)


    #calculate equity, debt and gold based on % change
    def test_balance_on_march(self):

        allocationLine = 'ALLOCATE 6000 3000 1000'
        sipPayment = 'SIP 2000 1000 500'
        
        objChange = Investment(0,0,0)
        objChange.setInvestment(allocationLine)

        #additional investment on the month
        objChange.setSIPInvestments(sipPayment)
        #investments should be sum of initial investment and sip monthly investment
        self.assertEqual(objChange.equity, 8000)
        self.assertEqual(objChange.debt, 4000)
        self.assertEqual(objChange.gold, 1500)


        changeLine = 'CHANGE 4.00% 10.00% 2.00% JANUARY'
        objChange.changeInvestment(changeLine)
        self.assertEqual(objChange.equity, 8320)
        self.assertEqual(objChange.debt, 4400)
        self.assertEqual(objChange.gold, 1530)

        changeLine = 'CHANGE -10.00% 40.00% 0.00% FEBRUARY'
        objChange.changeInvestment(changeLine)

        self.assertEqual(objChange.equity, 7488)
        self.assertEqual(objChange.debt, 6160)
        self.assertEqual(objChange.gold, 1530)

        changeLine = 'CHANGE 12.50% 12.50% 12.50% MARCH'
        objChange.changeInvestment(changeLine)
        self.assertEqual(objChange.equity, 8424)
        self.assertEqual(objChange.debt, 6930)
        self.assertEqual(math.floor(objChange.gold), 1721)


    def test_rebalance(self):
        inv = Investment(0,0,0)
        allocationLine = 'ALLOCATE 8000 1500 500'
        inv.setInvestment(allocationLine)

        inv.totalInvestment.update({'equity': inv.equity, 'debt': inv.debt, 'gold': inv.gold})
        rebalancedInvestments = inv.rebalance()
        self.assertEqual(float(rebalancedInvestments['equity']), 6000)
        self.assertEqual(float(rebalancedInvestments['debt']), 3000)
        self.assertEqual(float(rebalancedInvestments['gold']), 1000)
        
    def test_balance(self):
        inv = Investment(0,0,0)
        allocationLine = 'ALLOCATE 6000 3000 1000'        
        inv = Investment(0,0,0)
        inv.setInvestment(allocationLine)
        changeLine = 'CHANGE 4.00% 10.00% 2.00% JANUARY'
        inv.changeInvestment(changeLine)

        self.assertEqual

    def test_add_percentage_with_postive_percentage(self):
        inv = Investment(0,0,0)
        original_number = 1000
        strpercentage = "10%"
        percentage = inv.convert_percentage_to_float(strpercentage)
        new_number = inv.add_percentage(original_number, percentage)
        self.assertEqual(new_number, 1100)

    def test_add_percentage_with_negative_percentage(self):
        inv = Investment(0,0,0)
        original_number = 1000
        strpercentage = "-10%"
        percentage = inv.convert_percentage_to_float(strpercentage)
        new_number = inv.add_percentage(original_number, percentage)
        self.assertEqual(new_number, 900)

    def test_convert_percentage_to_float_string(self):
        inv = Investment(0,0,0)
        percentage = inv.convert_percentage_to_float("20%")
        self.assertEqual(percentage, 20.0)
 