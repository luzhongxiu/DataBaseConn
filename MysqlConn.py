#coding: utf-8
 
from tkinter import *
from tkinter import messagebox
import pymysql
 
class SignIn(object):
 
    def __init__(self, root):
        self.root = root
        self.name = None
        self.password = None
    def the_Window(self,):
 
        Label(self.root, text = "用户名(*):").grid(row = 1, column = 1, sticky = W)
        Label(self.root, text = "密码(*):").grid(row = 2, column = 1, sticky = W)
        self.name = Entry(self.root)
        self.name.grid(row = 1, column = 2, sticky = W)
        self.password = Entry(self.root, show = "*")
        self.password.grid(row = 2, column = 2, sticky = W)
        Button(self.root, text = "登录", command = self.Login).grid(row = 3, column = 1, sticky = W)
        Button(self.root, text = "注册",command = self.Registered).grid(row = 3, column = 2, sticky = W)
        Label(self.root, text="(用户名，不少于6位.)").grid(row = 1, column = 3, sticky = W)
        Label(self.root, text="(密码，不少于12位.)").grid(row=2, column=3, sticky= W)
 
    def Login(self):
        x = self.name.get()
        y = self.password.get()
 
        if len(x) == 0 or len(y) == 0:
            return
        conn = pymysql.connect(host='localhost',
                        	   user='root',
                        	   passwd='tk553977388',
                        	   port=3306,
                        	   db='test'
                        	   )
        sql_select = "select * from cities"
        cur = conn.cursor()
        try:
            cur.execute(sql_select)
            print(cur)
            rs = cur.fetchall()
            print(rs)
            for r in rs:
                if r[0] == x and r[1] == y:
                    messagebox.showinfo(title="登录成功", message="登录成功")
                    return
                elif r[0] == x and r[1] != y:
                    messagebox.showerror(title= "错误信息", message= "密码错误")
                    messagebox.showerror(title="error", message="当前用户不存在")
 
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    def Registered(self):
        self.username = self.name.get().strip()
        self.passwd = self.password.get().strip()
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "feigu", "feigudb")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = "INSERT INTO t_login(name, password) VALUES ('%s', '%s')" % (self.username, self.passwd)
        try:
            # 执行sql语句
            cursor.execute(sql)
            print("数据插入成功！！！")
            # 提交到数据库执行
            db.commit()
        except:
            print("数据插入失败！！！")
            # Rollback in case there is any error
            db.rollback()

        # 关闭数据库连接
        db.close()
        
if __name__ == "__main__":
    root = Tk()  #创建根窗口，后续组件都放在这个根窗口中
    root.title("登录窗口")
    sign = SignIn(root)
    sign.the_Window()
 
    root.mainloop()
