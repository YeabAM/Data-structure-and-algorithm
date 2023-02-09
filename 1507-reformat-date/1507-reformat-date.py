class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan": '01', "Feb": '02', 
                 "Mar": '03', "Apr": '04', 
                 "May": '05', "Jun": '06', 
                 "Jul": '07', "Aug": '08', 
                 "Sep": '09', "Oct": '10', 
                 "Nov": '11', "Dec": '12'}
        
        res = []
        date = date.split(" ")
        day = date[0]
        day = day[:-2]
        if len(day) == 1:
            day = '0' + day
        
        res.append(date[2])
        res.append(month[date[1]])
        res.append(day)
        
        return "-".join(res)
        
    
        
        
        