from bs4 import BeautifulSoup
import os


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ResultCollect:

    def __init__(self):
        pass


    def get_report_info(self, report_path):
        soup = BeautifulSoup(open(report_path), "lxml")
        tmp = soup.find(id="total_row")
        # total_list = []
        # for i in range(4):
        #     text = tmp.find_all('td')[i+1].string
        #     # print(text)
        #     total_list.append(text)

        dic_res = {}
        dic_res.update({'Count': tmp.find_all('td')[1].string})
        dic_res.update({'Pass': tmp.find_all('td')[2].string})
        dic_res.update({'Fail': tmp.find_all('td')[3].string})
        dic_res.update({'Error': tmp.find_all('td')[4].string})
        # return total_list, dic_res
        return dic_res


if __name__ == '__main__':

    html = '/Users/zhulixin/Desktop/UItest/Results/report/report.html'
    results = ResultCollect().get_report_info(html)
    print(results)

    count = results.get('Count')
    print(count)