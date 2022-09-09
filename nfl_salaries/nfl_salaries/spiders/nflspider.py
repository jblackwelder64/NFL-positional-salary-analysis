import scrapy

class NFLSpider(scrapy.Spider):
    name = 'nfl'
    start_urls = ['https://overthecap.com/positional-spending/']

    def parse(self, response):
        year = 2012
        count = 0
        for row in response.css('tr.sortable'):
            if count%32 == 0:
                year+=1
                count = 0
            count = count+1
            yield {
                'QB': float(row.css('td.sortable::text')[0].get().strip('$').replace(',','')),
                'RB': float(row.css('td.sortable::text')[1].get().strip('$').replace(',','')),
                'WR': float(row.css('td.sortable::text')[2].get().strip('$').replace(',','')),
                'TE': float(row.css('td.sortable::text')[3].get().strip('$').replace(',','')),
                'OL': float(row.css('td.sortable::text')[4].get().strip('$').replace(',','')),
                'Offense': float(row.css('td.sortable::text')[5].get().strip('$').replace(',','')),
                'IDL': float(row.css('td.sortable::text')[6].get().strip('$').replace(',','')),
                'EDGE': float(row.css('td.sortable::text')[7].get().strip('$').replace(',','')),
                'LB': float(row.css('td.sortable::text')[8].get().strip('$').replace(',','')),
                'S': float(row.css('td.sortable::text')[9].get().strip('$').replace(',','')),
                'CB': float(row.css('td.sortable::text')[10].get().strip('$').replace(',','')),
                'Defense': float(row.css('td.sortable::text')[11].get().strip('$').replace(',','')),
                'Team': row.css('a.team-link::text').get(),
                'Year' : year
            }