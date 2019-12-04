import pandas as pd

dictionary = {'Box' : ['Box1','Box1','Box1','Box2','Box2','Box2'],
              'Dimension': ['Length','Width','Height','Length','Width','Height'],
              'Value': [6,4,2,5,3,4]}

messy = pd.DataFrame(dictionary, columns = ['Box','Dimension','Value'])

tidy = messy.pivot_table(index = ['Box'], columns = 'Dimension', values = 'Value')

vol = tidy.assign(Volume=lambda tidy: tidy.Length*tidy.Width*tidy.Height)

print(vol)