class SearchLocator:
    search_txb = '//input[@id="search_query_top"]'
    product_hints = '//div[@class="ac_results"]'

    # check result
    hint_ele1 = '//li[@class = "ac_even ac_over"]'
    search_item = '//form[@id = "searchbox"]//button[@type= "submit"]'
    result_all_search = "//ul[@class= 'product_list grid row']//a[@class = 'product-name']"


    # -------------------------------bài tập 07------------------------------------------------

    no_result = '//*[@id="center_column"]/p'
