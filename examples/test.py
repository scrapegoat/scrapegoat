
# from scrapegoat.multiprocess import generateData






# from utils import automate
# from utils import SearchFunction
# from multiprocess import getLinkData
# from multiprocess import generateData
# import time
# import pandas as pd 

url = 'https://kannada.asianetnews.com/central-government-jobs/hal-is-recruiting-apprentice-posts-and-check-details-qzbcph'
topic = "engineering"
cores = 6
if __name__=="__main__":
    import scrapegoat as sg 
    from scrapegoat.utils import automate
    from scrapegoat.multiprocess import getLinkData
    a,b = getLinkData(url=url, topic=topic, language='kn', cores=cores)
    print(a,b)
# max_bert_len = 512


# if __name__ == '__main__':

#     ################## Your Code For processing Links in DataFrame or list ###################

#     links = [] 
#     s = SearchFunction('kn','engineering')
#     links = s.LinkCollection(n_link=10)

#     ##########################################################################################


#     #################### Iterate and Store the data in files or folder you need #####################
#     folder_path = 'C:\\Users\\navaneethsharma2310\\OneDrive\\Desktop\\opendatagen\\data\\'
#     threshold = 0.2
#     df = pd.read_csv('updated_finace_table.csv')
#     for top,link in zip(df['topic'],df['Link2']):
#         # print(i)
      
#         text, mean = getLinkData(url=link, topic=top, language='kn', cores=4)
#         if mean>threshold:
#         # threashold adjustment code
#             # if i>5:
#             #     threshold = (threshold+mean)/2
#             with open(folder_path+top+".txt",'w', encoding = 'utf-8') as f:
#                 f.write(text)
#                 f.close()