import matplotlib.pyplot as plt

def plot_pie(df,by_what,labels=None,figsize=(3,3)):
    
    if(labels==None):
        labels = df[by_what].value_counts().index
    
    plt.figure(figsize=figsize)
    plt.pie(df[by_what].value_counts(), labels=labels, autopct='%2.2f%%')
    plt.tight_layout()