from datetime import datetime
from fastapi import HTTPException
from entity.users import CreateUser, ModifyUser, ResultUser
from core.conn import getConn


def createUser(user:CreateUser,expTime:int):
  
    conn = getConn()
    exists = conn.execute("select count(*) from users  where username = ?",(user.username,)).fetchall()

    if not exists[0][0] == 0:
        raise HTTPException(400,"username already exists")
    
    conn.execute("insert into users (id,username,password,expdisable,expire) values (nextval('seq_personid'),?,?,?,?)",(user.username,user.password,user.expdisable,expTime))


def readUsers():
    conn = getConn()
  
    all = conn.sql("select * from users").fetchall()
  
    ret = []
    for res in all:
        result = ResultUser()
        result.id = res[0]
        result.username = res[1]
        result.password = ""
        result.expdisable  = res[3]
        if res[4] > 0:
            date_formated = datetime.utcfromtimestamp(float(res[4]))
            layout = "{year}-{month:02d}-{day:02d}"

            result.expire = layout.format(year=date_formated.year,month=date_formated.month,day=date_formated.day)
        else:
            result.expire = "2024-05-01"
        
        ret.append(result)
    return ret

def deleteUser(id:int):
    conn = getConn()
    conn.execute("delete from users where id=?",(id,))

def modifyUser(user:ModifyUser,changePassword:bool,expTime:int):
    conn = getConn()
    if changePassword:
        conn.execute("update users set username=? , password = ?, expdisable = ?, expire = ? where id=? ",(user.username,user.password,user.expdisable,expTime,user.id))
    else:
        conn.execute("update users set username=? , expdisable = ?, expire = ? where id=? ",(user.username,user.expdisable,expTime,user.id))
