import pandas as pd
import os
from datetime import datetime, timedelta

def transform_data():
        #current_date = datetime.now().strftime("%Y-%m-%d")
    current_date = datetime.now()

    # Calculate the date of yesterday
    yesterday_date = current_date - timedelta(days=1)

    # Format the date as YYYY-MM-DD
    yesterday_date_formatted = yesterday_date.strftime("%Y-%m-%d")

    directory = f'/home/dhon_bobis/Documents/ecm-web-scraper-shopee-main/downloads/{yesterday_date_formatted}/'
    #directory = '/home/dhon_bobis/Documents/ecm-web-scraper-shopee-main/downloads/'
    #directory = '/Users/dhon.bobis/Documents/Sprint 33/ecm-shoppee/downloads/'
    contents = os.listdir(directory)

    all_data_campaign = []
    all_data_product_item = []
    all_data_product_day = []
    all_overall_shop = []
    all_overall_day = []
    all_overall_channel = []
    on_all_overall_day = []
    on_all_product_perf = []


    boost_ads = []
    discovery_ads = []
    search_ads_keywords = []
    search_ads_shop = []

    for item in contents:
        if "Off-platform_Traffic_Report---Campaign_Performance" in item:
            new_filename = item.replace("Off-platform_Traffic_Report---Campaign_Performance---", "")
            new_filename2 = new_filename[-15:-5]
            date_now = new_filename[-15:-5]
            date_now = date_now.replace(".", "-")

            brand_name = new_filename[:-16]
            
            df = pd.read_excel(directory + item, sheet_name="Details Sheet")
            #df = df.drop(0)
            df['account'] = brand_name
            df['date'] = date_now
            all_data_campaign.append(df)

        if "Off-platform_Traffic_Report---Product_Performance" in item:
            new_filename = item.replace("Off-platform_Traffic_Report---Product_Performance---", "")
            new_filename2 = new_filename[-15:-5]
            account = new_filename[:-16]
            date_now = new_filename[-15:-5]
            date_now = date_now.replace(".", "-")

            #By Item
            item_df = pd.read_excel(directory + item, sheet_name="By Item")
            item_df['account'] = account
            item_df['date'] = date_now

            all_data_product_item.append(item_df)

            #By Day
            day_df = pd.read_excel(directory + item, sheet_name="By Day")
            day_df['account'] = account
            all_data_product_day.append(day_df)

        if "Off-platform_Traffic_Report---Overall_Performance" in item:
            new_filename = item.replace("Off-platform_Traffic_Report---Overall_Performance---", "")
            date_now = new_filename[-15:-5]
            account = new_filename[:-16]
            date_now = date_now.replace(".", "-")
            #By Shop
            shop_df = pd.read_excel(directory + item, sheet_name="By Shop")
            shop_df['date'] = date_now
            shop_df['account'] = account
            all_overall_shop.append(shop_df)

            #By Day
            overall_day_df = pd.read_excel(directory + item, sheet_name="By Day")
            overall_day_df['account'] = account
            overall_day_df['date'] = date_now

            all_overall_day.append(overall_day_df) 

            #By Channel
            overall_channel_df = pd.read_excel(directory + item, sheet_name="By Channel")
            overall_channel_df['account'] = account
            overall_channel_df['date'] = date_now
            all_overall_channel.append(overall_channel_df) 


        if "Boost_Ads_On-platform_Ads_Report---Overall_Performance" in item:
            new_filename = item.replace("Boost_Ads_On-platform_Ads_Report---Overall_Performance---", "")
            date_now = new_filename[-15:-5]
            account = new_filename[:-16]
    
            #By Day
            boost_ads_df = pd.read_excel(directory + item, sheet_name="By Day")
            boost_ads_df['account'] = account
            boost_ads_df['date'] = date_now

            boost_ads.append(boost_ads_df)

        if "Discovery_Ads_On-platform_Ads_Report---Overall_Performance" in item:
            new_filename = item.replace("Discovery_Ads_On-platform_Ads_Report---Overall_Performance---", "")
            date_now = new_filename[-15:-5]
            account = new_filename[:-16]
    
            #By Day
            discovery_df = pd.read_excel(directory + item, sheet_name="By Day")
            discovery_df['account'] = account
            discovery_df['date'] = date_now

            discovery_ads.append(discovery_df)
        if "Search_Ads_Keywords_On-platform_Ads_Report---Overall_Performance" in item:
            new_filename = item.replace("Search_Ads_Keywords_On-platform_Ads_Report---Overall_Performance---", "")
            date_now = new_filename[-15:-5]
            account = new_filename[:-16]
    
            #By Day
            search_ads_keywords_df = pd.read_excel(directory + item, sheet_name="By Day")
            search_ads_keywords_df['account'] = account
            search_ads_keywords_df['date'] = date_now

            search_ads_keywords.append(search_ads_keywords_df)

        if "Search_Ads_Shop_On-platform_Ads_Report---Overall_Performance" in item:
            new_filename = item.replace("Search_Ads_Shop_On-platform_Ads_Report---Overall_Performance---", "")
            date_now = new_filename[-15:-5]
            account = new_filename[:-16]
    
            #By Day
            search_ads_shop_df = pd.read_excel(directory + item, sheet_name="By Day")
            search_ads_shop_df['account'] = account
            search_ads_shop_df['date'] = date_now

            search_ads_shop.append(search_ads_shop_df)


        if "On-platform_Ads_Report---Product_Performance---" in item:
            new_filename = item.replace("On-platform_Ads_Report---Product_Performance---", "")
            date_now = new_filename[-15:-5]
            account = new_filename[:-16]
            date_now = date_now.replace(".", "-")

            #Product performance
            on_product_perf = pd.read_excel(directory + item, sheet_name="Product performance")
            on_product_perf['date'] = date_now
            on_product_perf['account'] = account
            on_all_product_perf.append(on_product_perf)

    print(all_data_campaign != [])
    if all_data_campaign:
        combined_df_campaign = pd.concat(all_data_campaign, ignore_index=True)
        combined_df_campaign.to_parquet(f'{directory}shp_off_campaign.parquet')
    if all_data_product_item: 
        item_df_product = pd.concat(all_data_product_item, ignore_index=True)
        item_df_product.to_parquet(f'{directory}shp_off_product_item.parquet')

    if all_data_product_day:
        day_df_product = pd.concat(all_data_product_day, ignore_index=True)
        day_df_product.to_parquet(f'{directory}shp_off_product_day.parquet')

    if all_overall_shop:
        all_overall_shop_df = pd.concat(all_overall_shop, ignore_index=True)
        all_overall_shop_df.to_parquet(f'{directory}shp_off_overall_shop.parquet')

    if all_overall_day:
        all_overall_day_df = pd.concat(all_overall_day, ignore_index=True)
        all_overall_day_df.to_parquet(f'{directory}shp_off_overall_day.parquet')

    if all_overall_channel:
        all_overall_channel_df = pd.concat(all_overall_channel, ignore_index=True)
        all_overall_channel_df.to_parquet(f'{directory}shp_off_overall_channel.parquet')

    if boost_ads:
        boost_ads_total = pd.concat(boost_ads, ignore_index=True)
        boost_ads_total.to_parquet(f'{directory}shp_boost_ads_on_overall.parquet')

    if discovery_ads:
        discovery_ads_total = pd.concat(discovery_ads, ignore_index=True)
        discovery_ads_total.to_parquet(f'{directory}shp_discovery_ads_on_overall.parquet')

    if search_ads_keywords:
        search_ads_keywords_total = pd.concat(search_ads_keywords, ignore_index=True)
        search_ads_keywords_total.to_parquet(f'{directory}shp_search_ads_keywords_on_overall.parquet')

    if search_ads_shop:
        search_ads_shop_total = pd.concat(search_ads_shop, ignore_index=True)
        search_ads_shop_total.to_parquet(f'{directory}shp_search_ads_shop_on_overall.parquet')

    if on_all_product_perf:
        on_product_all = pd.concat(on_all_product_perf, ignore_index=True)
        on_product_all.to_parquet(f'{directory}shp_on_product_perf.parquet')
    #print(search_ads_keywords_total)
#transform_data()
