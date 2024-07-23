import pandas as pd

def read_keywords_from_excel(file_path, sheet_name, column_name=None):
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        # 提取指定列的数据并转换为列表
        #keyword_list = df[column_name].dropna().tolist()
        return df
    except Exception as e:
        print(f"读取Excel文件出错: {e}")
        return []


def diff_org_trim(file_path,sheet_org,sheet_trim,sheet_new,sheet_sort,new_file_path):
    # 假设你的DataFrame名为df
    df = pd.read_excel(file_path)
    # 创建新的列C，如果A列和B列的值相同则为空，否则显示A列和B列的值
    df[sheet_new] = df.apply(lambda row: '' if row[sheet_org] == row[sheet_trim] else row[sheet_trim], axis=1)
    
    df_copy = df.copy()
    # 先按照C列排序，然后按照E列排序（降序，保证E列值最高的在前面）
    df_copy = df_copy.sort_values(by=[sheet_new, sheet_sort], ascending=[True, False])

    # 去除重复的行，保留E列值最高的那一行
    #df = df.drop_duplicates(subset=sheet_new, keep='first')
    df_copy = df_copy.drop_duplicates(subset=sheet_new, keep='first')

    # 将结果合并回原始数据框
    df[sheet_new] = df_copy[sheet_new]

    # 保存结果到新的Excel文件
    df.to_excel(new_file_path, index=False)
    print("done")

# 统计非空
def count_no_black(file_path, sheet_name):
    df = pd.read_excel(file_path)
    # count = df[df[sheet_name] != ''].count()# 全部列，单独去重
    # count = df[sheet_name].count()
    count = (df[sheet_name].str.strip()).count()
    print(count)

def nunique_filed(file_path, sheet_name):
    df = pd.read_excel(file_path)
    # 计算 "org_query" 列去重后的数量
    unique_df = df[sheet_name].drop_duplicates()

    unique_count = unique_df.shape[0]
    unique_values = df['5391_usranker-out'].unique()

    print(unique_count,len(unique_values))

# 5391_usranker-out 有值 trim_query  去重
def cc(file_path):
    df = pd.read_excel(file_path)
    # 假设你的DataFrame名为df
    filtered_df = df[df['5391_usranker-out'].notnull()]

    # 然后去重 'trim_query'
    unique_trim_query = filtered_df['trim_query'].drop_duplicates()

    # 打印去重后的 'trim_query'
    print(unique_trim_query) 

def jing_tian_api():
    url = ""
    print("jing_tian_api done")
    return 0
    

# 测试函数
if __name__ == "__main__":
    # file_path = '2.xlsx'
    # sheet_name = 'Sheet1'
    # column_name = 'org_query'
    # keywords = read_keywords_from_excel(file_path, sheet_name, column_name)
    #print(keywords[:10])
    file_path = 'uery.xlsx'  
    
    new_file_path = 'new.xlsx'
    #diff_org_trim(file_path,"org_query","trim_query", "new_diff","PV",new_file_path)

    file_path = '120.xlsx'
    count_no_black(file_path,'dis_trim_diff')

    file_path = '20.xlsx'
    nunique_filed(file_path,'ranker-out')
    cc(file_path)
