from newsapi import NewsApiClient
from datetime import datetime
import config

def company_data (company_name, days_back):

    newsapi = NewsApiClient(api_key=config.api_key)

    source = "abc-news,ars-technica,associated-press,bbc-news,bloomberg,breitbart-news,business-insider,buzzfeed,cnbc,cnn,engadget," \
             "espn,financial-post,financial-times,fortune,google-news,mashable,msnbc,national-geographic,nbc-news,new-york-magazine," \
             "politico,reuters,techcrunch,techradar,the-economist,the-huffington-post,the-new-york-times,the-wall-street-journal," \
             "the-washington-post,time,usa-today,wired"

    # today's date
    now_date = datetime.now().date()

    # convert date to ordinal and subtract # of days to look back for article
    prior_toord = datetime.now().date().toordinal() - days_back

    # convert look back date from ordinal to normal date format
    prior_date = datetime.fromordinal(prior_toord).date()

    # there are other sort_by choices though relevancy has had the best results
    top_headlines = newsapi.get_everything(q=company_name, sources=source, from_parameter=str(prior_date), to=str(now_date), language='en', sort_by='relevancy')

    headline_counter = 0

    news_list = []

    if top_headlines['totalResults'] > 0:
        for i in range(0, top_headlines['totalResults'] ):
            news_list.append([
                        top_headlines['articles'][i]['url'],
                        top_headlines['articles'][i]['title'],
                        top_headlines['articles'][i]['source']['name'],
                        # just the date, not the time
                        top_headlines['articles'][i]['publishedAt'][0:10],
                        ])

            # although not in the API documentation, a free plan is limited to 20 articles per request
            if headline_counter >= 19:
                break
            headline_counter+=1

    else:
        news_list.append(['none','none'])

    return news_list

print ( company_data('microsoft', 5) )