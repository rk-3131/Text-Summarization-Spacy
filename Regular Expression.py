import re

text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
# Get name of the twitter handles only

pattern = '.com\/([0-9 A-Z a-z _]+)'

result = re.findall(pattern, text)
print(result)

text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''

# Get the concentartion of the risk types

pattern = 'Risk: ([A-Z A-Z]+)'

result = re.findall(pattern, text, flags=re.IGNORECASE)
print(result)

text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''

# Find the cost of the quarter and semi annual cost of the comapany expenditure

pattern = '(Q[1-4]|S[1-2]) .+(\$[0-9].[0-9]*)+'
# (Q[1-4]|S[1-2]) .+(\$[0-9].[0-9]*)+

result = re.findall(pattern, text)
print(result)

'''
For the purpose of creating the regular expression we have to follow certain rules
These rules are as follows

1. [abc]
Matches either an a, b or c character
/[abc]+/g
a bb ccc

2. [^abc]
Matches any character except for an a, b or c
/[^abc]+/g
Anything but abc.

3. [a-z]
Matches any characters between a and z, including a and z.
/[a-z]+/g
Only a-z

4. [^a-z]
Matches any characters except those in the range a-z.
/[^a-z]+/g
Anything but a-z.

5. [a-zA-Z]
Matches any characters between a-z or A-Z. You can combine as much as you please.
/[a-zA-Z]+/g
abc123DEF

6. .
Matches any character other than newline (or including line terminators with the /s flag)
/.+/
a b c

7. a|b
Matches either what is before the | or what is after it - in this case `a` or `b`.

You can use alternates locally as part of a capturing/non-capturing group. For example: /I love (?:cats|dogs) but hate snakes/
/a|b/g
a or b, pick one!


'''