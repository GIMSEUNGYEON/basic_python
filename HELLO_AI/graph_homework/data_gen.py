from day06_graph.daostock import DaoStock

ds = DaoStock()

samsung = ds.select("삼성전자")
lg = ds.select("lg")
sk = ds.select("sk")
hanhwa = ds.select("한화")
posco = ds.select("포스코스틸리온")

samPrice = []
lgPrice = []
skPrice = []
hanPrice = []
poPrice = []
class Data_gen:
    for i in range(len(samsung)) :
        samPrice.append(samsung[i].get("price"))
        lgPrice.append(lg[i].get("price"))
        skPrice.append(sk[i].get("price"))
        hanPrice.append(hanhwa[i].get("price"))
        poPrice.append(posco[i].get("price"))
        
    def samsung_data(self) : 
        samX = []
        firstPrice = samPrice[0]
        for i in samPrice:
            bp = (i-firstPrice)/firstPrice * 10000
            samX.append(bp)
        return samX
    
    def lg_data(self) :
        lgX = []
        firstPrice = lgPrice[0]
        for i in lgPrice:
            bp = (i-firstPrice)/firstPrice * 10000
            lgX.append(bp)
        return lgX
    
    def sk_data(self) :
        skX = []
        firstPrice = skPrice[0]
        for i in skPrice:
            bp = (i-firstPrice)/firstPrice * 10000
            skX.append(bp)
        return skX
    
    def han_data(self) :
        hanX = []
        firstPrice = hanPrice[0]
        for i in hanPrice:
            bp = (i-firstPrice)/firstPrice * 10000
            hanX.append(bp)
        return hanX
    
    def po_data(self) :
        poX = []
        firstPrice = poPrice[0]
        for i in poPrice:
            bp = (i-firstPrice)/firstPrice * 10000
            poX.append(bp)
        return poX
    
if __name__=="__main__" :
    dg = Data_gen()
    print(dg.samsung_data())
    print(dg.lg_data())
    print(dg.sk_data())
    print(dg.han_data())
    print(dg.po_data())
    
    