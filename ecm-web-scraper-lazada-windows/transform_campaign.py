import pandas as pd
import os
from datetime import datetime, timedelta

def transform_data():
    
    current_date = datetime.now()
    # Calculate the date of yesterday
    yesterday_date = current_date - timedelta(days=1)
    # Format the date as YYYY-MM-DD
    yesterday_date_formatted = yesterday_date.strftime("%Y-%m-%d")

    directory = f'/home/dhon_bobis/Documents/ecm-web-scraper-lazada-windows/downloads/{yesterday_date_formatted}/'
    contents = os.listdir(directory)

    all_data_campaign = []
    all_npl_adgroup = []
    all_ext_overview = []
    all_ext_camp_perf = []
    all_ext_sku_df = []
    all_sa_overview_df = []
    all_sm_sheet0 = []

    for item in contents:

        if "sponsored_solutions" in item:
            # new_filename = item.replace("Off-platform_Traffic_Report---Campaign_Performance---", "")
            brand_name = item.split("_")[1]
            
            date_now = item.split("_")[0]
            
            start_row = 7
            df = pd.read_excel(directory + item, sheet_name="Campaign", skiprows=start_row)

            df['account'] = brand_name
            all_data_campaign.append(df)

        if "new_product_launcher" in item:
            brand_name = item.split("_")[1]
            
            date_now = item.split("_")[0]
            
            start_row = 7
            npl_df = pd.read_excel(directory + item, sheet_name="Adgroup", skiprows=start_row)

            npl_df['account'] = brand_name
            all_npl_adgroup.append(npl_df)

        if "external_traffic" in item:
            brand_name = item.split("_")[1]
            
            date_now = item.split("_")[0]
            
            #Overview
            
            overview_df = pd.read_excel(directory + item, sheet_name="Overview")
            overview_df['account'] = brand_name
            overview_df['date_of_file'] = date_now
            all_ext_overview.append(overview_df)

            #Campaign Performance
            
            camp_df = pd.read_excel(directory + item, sheet_name="Campaign Performance")

            camp_df['account'] = brand_name
            camp_df['date_of_file'] = date_now
            camp_df.drop('Sub Channel', axis=1)
            camp_df['Sub Channel'] = camp_df['Sub Channel']
            #print(camp_df.columns.tolist())
            all_ext_camp_perf.append(camp_df)
            print(camp_df['Sub Channel'])
            #SKU Performance
            
            sku_df = pd.read_excel(directory + item, sheet_name="SKU Performance")

            sku_df['account'] = brand_name
            sku_df['date_of_file'] = date_now
            all_ext_sku_df.append(sku_df)
        
        if "sponsored_affiliate" in item:
            brand_name = item.split("_")[1]
            
            date_now = item.split("_")[0]
            #Overview
            sa_overview_df = pd.read_excel(directory + item, sheet_name="Overview")
            sa_overview_df.rename(columns={'Est. Spend': 'Estimated Spend'}, inplace=True)
            sa_overview_df['account'] = brand_name
            sa_overview_df['date_of_file'] = date_now
            all_sa_overview_df.append(sa_overview_df)

        if "sponsored_media" in item:
            brand_name = item.split("_")[1]
            
            date_now = item.split("_")[0]
            #Overview
            sm_sheet0 = pd.read_excel(directory + item)

            sm_sheet0['account'] = brand_name
            sm_sheet0['date_of_file'] = date_now
            all_sm_sheet0.append(sm_sheet0)


    if all_data_campaign:
        combined_df_campaign = pd.concat(all_data_campaign, ignore_index=True)
        combined_df_campaign.to_parquet(f'{directory}lzd_ss_campaign.parquet')

    if all_npl_adgroup:
        combined_npl = pd.concat(all_npl_adgroup, ignore_index=True)
        combined_npl.to_parquet(f'{directory}lzd_npl_adgroups.parquet')

    if all_ext_overview:
        combined_all_ext_overview = pd.concat(all_ext_overview, ignore_index=True)
        combined_all_ext_overview.to_parquet(f'{directory}lzd_ext_overview.parquet')

    if all_ext_camp_perf:
        combined_all_ext_camp_perf = pd.concat(all_ext_camp_perf, ignore_index=True)
        combined_all_ext_camp_perf.to_parquet(f'{directory}lzd_ext_camp_perf.parquet')

    if all_ext_sku_df:
        combined_all_ext_sku_df = pd.concat(all_ext_sku_df, ignore_index=True)
        combined_all_ext_sku_df.to_parquet(f'{directory}lzd_ext_sku.parquet')

    if all_sa_overview_df:
        combined_all_sa_overview_df = pd.concat(all_sa_overview_df, ignore_index=True)
        combined_all_sa_overview_df.to_parquet(f'{directory}lzd_sa_overview.parquet')
    
    if all_sm_sheet0:
        combined_all_sm_sheet0 = pd.concat(all_sm_sheet0, ignore_index=True)
        combined_all_sm_sheet0.to_parquet(f'{directory}lzd_sm_sheet0.parquet')
    
transform_data()
