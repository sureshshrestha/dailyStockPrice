import requests
headers = {'User-Agent': 'Mozilla/5.0','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest'}
companyId = '14'
pageNo = 1
maxPage = 65
for x in range (0, maxPage):
		url = "https://www.sharesansar.com/ajaxcompanypricehistory?" + "page=" + str(pageNo) + "&companyid=" + companyId

		r = requests.get( url = url, headers =headers )

		print r.content

		with open('test.html', 'a') as the_file:
				the_file.write('__________________________________\n')
				the_file.write(r.content)

		pageNo = pageNo + 1
