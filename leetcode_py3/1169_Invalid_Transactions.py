class Solution:
    def invalidTransactions(self, transactions):
        name, time, amount, city = [], [], [], []
        res = []
        new_trans = []
        
        if not transactions:
            return []
        
        for transaction in transactions:
            info = transaction.split(',')
            name.append(info[0])
            time.append(info[1])
            amount.append(info[2])
            city.append(info[3])
              
        for i in range(len(name)):
            if int(amount[i]) > 1000:
                res.append(','.join([name[i], time[i], amount[i], city[i]]))
            for j in range(i):
                if abs(int(time[i])-int(time[j])) <= 60 and city[i] != city[j] and name[i] == name[j]:
                    res.append(','.join([name[i], time[j], amount[j], city[j]]))
                    res.append(','.join([name[i], time[i], amount[i], city[i]]))
            
        return set(res)
        

if __name__ == '__main__':

    transactions = ["alice,20,800,mtv","alice,50,100,beijing"] 
    print(Solution().invalidTransactions(transactions))


'''

A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

'''              
