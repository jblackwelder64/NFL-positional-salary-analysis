import scrapy

class WinSpider(scrapy.Spider):
    name = 'wins'
    start_urls = []
    url_root = 'https://www.teamrankings.com/nfl/trends/win_trends/?sc=is_regular_season&range=yearly_'
    for year in range(2013, 2022):
        year_str = str(year)
        start_urls.append(url_root + year_str)

    def parse(self, response):
        # layer1 = response.css('body.nfl.notice.subnav-nfl-trends.wider-desktop-sidebar.no-mobile-tab-bar')
        # layer2 = layer1.css('div.wrapper')
        # layer3 = layer2.css('div.content-wrapper.clearfix')
        # layer4 = layer3.css('div.main-wrapper.clearfix.has-left-sidebar')
        # layer5 = layer4.css('main.has-right-sidebar')

        rows = response.css('tr')
        # print('rows:' , rows) #debugging
        for i in range(1 , len(rows)): #Excluding the first row since it just contains column names
        # for row in rows:
            entries = rows[i].css('td')
            print('entries:' , entries) #debugging
            yield {
                'Team': entries[0].css('a::text').get(),
                'WinPercent': float(entries[2].css('td::text').get().replace('%', '')),
                'Year': int(str(response)[-5:-1])
            }






