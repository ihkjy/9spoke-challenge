import json
  
# Opening JSON file
f = open('data.json')
  
# json data as dictionary
data = json.load(f)

#initializing values
revenue = 0
expense = 0
gross = 0
assets = 0
liabilities = 0
for i in data['data']:

#adding up revenue
    if i['account_category'] == 'revenue':
        revenue += i['total_value']
    
#adding up gross income        
    if i['account_type'] =='sales' and i['value_type'] == 'debit':
        gross += i['total_value']

#adding up expense        
    if i['account_category'] == 'expense':
        expense += i['total_value']

#calculating liabilities        
    if i['account_category'] == 'liabilities' and i['value_type'] == 'credit' and (i['account_type'] == 'current' or 'current_account_receieve'):
             liabilities += i['total_value']
    if i['account_category'] == 'liabilities' and i['value_type'] == 'debit' and (i['account_type'] == 'current' or 'current_account_receieve'):
            liabilities -= i['total_value']

#calculating assets
    if i['account_category'] == 'assets' and i['value_type'] == 'debit' and (i['account_type'] == 'current' or 'bank' or 'current_account_receieve'):
        assets += i['total_value']
    if i['account_category'] == 'assets' and i['value_type'] == 'credit' and (i['account_type'] == 'current' or 'bank' or 'current_account_receieve'):
        assets -= i['total_value']
#getting all the percentage values to 1d.p
        
gross_inccome = round(gross*100 /revenue,1)
net = round((revenue - expense)*100 /expense,1)

#exception for liabilities because it give Zerodivisionerror
if liabilities == 0:
    Working_Capital_Ratio = float('inf')
else:
    Working_Capital_Ratio = round(assets* 100/liabilities,1)

#print result    
print('```')
print('$ ./myChallenge')
print('Revenue: ${:,.0f}'.format((revenue)))
print('Expenses: ${:,.0f}'.format(int(expense)))
print('Gross Profit Margin: '+ str(gross_inccome) + '%')
print('Net Profit Margin: '+str(net) +'%')
print('Working Capital Ratio: ' +str(Working_Capital_Ratio) + '%')
print('```')



f.close()
