def frequency_analysis(text_file):

    with open(text_file) as f:
        x = f.read()
    
    print(x)

    
    '''  counts = {}

    for i in text_file:
        
        if i in counts :
            counts[i]+=1
        else:
            counts[i] = 1'''

article = input()

frequency_analysis(article)