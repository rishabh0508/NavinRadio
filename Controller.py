import web
import datetime
from bson import ObjectId

from Class import Db

url = ("/", "ind",
       "/add", "add",
       "/avai", "available",
       "/search", "search",
       "/delete", "delete",
       "/remove", "remove",
       "/sold", "sold")
app = web.application(url, globals())
ren = web.template.render("Views/Templates/", base="Main_Layout")
p = Db.In("register", "Registration")
q = Db.In("register", "Completed")

class ind:
    def GET(self):
        return ren.Home()

class add:
    def GET(self):
        return ren.add()

    def POST(self):
        data = web.input()
        p.insert([data])
        return ren.add()


class available:
    def GET(self):
        g = p.display()
        return ren.display(g)



class search:
    def GET(self):
        return ren.search()

    def POST(self):
        data = web.input()
        g = q.dis(data)
        return ren.sold(g)


class delete:
    def GET(self):
        return True


    def POST(self):
        da = web.input()
        ax = da["_id"]
        qn = da["q"]
        print(qn)
        qn = int(qn)
        date = str(datetime.date.today())
        print(qn)
        tt = {'_id': ObjectId(ax)}
        t = p.dis(tt)
        for i in t:
            c = {"item name": i["item name"],
                 "brand name": i["brand name"],
                 "model name": i["model name"],
                 "quantity": qn,
                 "datetime": date,
                 "cost price": i["cost price"]}
            cc = {"item name": i["item name"],
                 "brand name": i["brand name"],
                 "model name": i["model name"],
                 "datetime": date,
                 "cost price": i["cost price"]}
            x = int(int(i["quantity"]) - int(da['q']))

        cn = q.dis(cc)
        if cn.count() == 1:
            q.ad(cc, qn)

        else:
             q.insert([c])

        print("count", cn.count())
        if x>0:
             p.replace(tt, x)
        else:
            p.de(tt)
        a = p.display()
        return ren.display(a)


class sold:
    def GET(self):
        s = q.display()
        return ren.sold(s)

class remove:
    def GET(self):
        return True

    def POST(self):
        da = web.input()
        ax = da["_id"]
        tt = {'_id': ObjectId(ax)}
        t = q.dis(tt)
        for i in t:
            q.de({"_id": i["_id"]})
        a = q.display()
        return ren.sold(a)


if __name__== "__main__":
    app.run()
