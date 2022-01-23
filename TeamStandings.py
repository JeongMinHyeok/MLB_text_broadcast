def TeamStandings(leagueId, date):
    league = ''
    if leagueId not in [103, 104, '']:
        return '잘못된 리그 코드입니다.'
    else:
        if leagueId == 103:
            league = '아메리칸리그(AL)'
        elif leagueId == 104:
            league = '내셔널리그(NL)'
        else:
            league = 'MLB 전체'
            
    if league == 'MLB 전체':
        if date == '':
            print(datetime.today().strftime('%Y년 %m월 %d일'), league , '순위입니다.')
            return print(statsapi.standings( date=datetime.today().strftime('%m/%d/%Y')))
        elif date[0] == '-':
            print(date[1:],'일 전', (datetime.today()-timedelta(int(date[1:]))).strftime('%Y년 %m월 %d일'), league , '순위입니다.')
            return print(statsapi.standings(date=(datetime.today()-timedelta(int(date[1:]))).strftime('%m/%d/%Y')))
        else:
            print('입력한 날짜의', league , '순위입니다.')
            return print(statsapi.standings(date=date))
    
    else:
        if date == '':
            print(datetime.today().strftime('%Y년 %m월 %d일'), league , '순위입니다.')
            return print(statsapi.standings(leagueId = leagueId, date=datetime.today().strftime('%m/%d/%Y')))
        elif date[0] == '-':
            print(date[1:],'일 전', (datetime.today()-timedelta(int(date[1:]))).strftime('%Y년 %m월 %d일'), league , '순위입니다.')
            return print(statsapi.standings(leagueId = leagueId, date=(datetime.today()-timedelta(int(date[1:]))).strftime('%m/%d/%Y')))
        else:
            print('입력한 날짜의', league , '순위입니다.')
            return print(statsapi.standings(leagueId = leagueId, date=date))