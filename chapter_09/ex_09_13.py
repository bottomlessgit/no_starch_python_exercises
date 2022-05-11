from collections import OrderedDict

glossary = OrderedDict()
glossary['list'] = 'object that holds an ordered set of values'
glossary['dictionary'] = ('object that holds key value pairs'
                  		 ' in unspecified order')
glossary['float'] = 'object holding decimal number value'
glossary['int'] = 'object holding integer number value'
glossary['string'] = 'object holding a string of characters'

for word, explanation in glossary.items():
    print(word + ": " + explanation)