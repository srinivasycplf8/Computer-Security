def frequency_analysis(text_file):

    with open(text_file) as f:
        x = f.read()
    

    
    counts = {}
    most_frequencies=['E','T','A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z']

    for i in x:


        if i=="\n":
            pass
        else:
            if i in counts :
                counts[i]+=1
            else:
                counts[i] = 1
    del counts[' ']
   # print(counts)
    #sorted_counts=list(reversed(sorted(counts.keys())))
    sort_orders = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

    sorted_new_list=list(sort_orders.keys())

    for letter in sorted_new_list:
        


    


    

article = input()

frequency_analysis(article)