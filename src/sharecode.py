import sqlite3
import hashlib
import random
import base64

def addtodb(code, modeljson, hash):
    code = str(code)
    conn = sqlite3.connect('sharecodes.db')
    cursor = conn.cursor()
    hashcmd = f"INSERT INTO SCHASH VALUES ('{code}', '{hash}')"
    namecmd = f"INSERT INTO SHARECODE VALUES ('{code}', '{modeljson}')"
    cursor.execute(namecmd)
    cursor.execute(hashcmd)
    conn.commit()
    conn.close()

def hashit(modeljson):
    modeljson = str(modeljson)
    result = hashlib.md5(modeljson.encode())
    return result.hexdigest()

def checkifexisthash(hash):
    conn = sqlite3.connect('sharecodes.db')
    cur = conn.cursor()
    cur.execute("""SELECT Hash FROM SCHASH WHERE Hash=?""",(hash,))
    result = cur.fetchone()
    if result:
        cur.execute("SELECT * FROM SCHASH WHERE Hash=?", (hash,))
        rows = cur.fetchall()
        code = rows[0][0]
        conn.close()
        return code
    else:
        conn.close()
        return False
    
def pullsharecodedata(code):
    str(code)
    conn = sqlite3.connect('sharecodes.db')
    cur = conn.cursor()
    cur.execute("""SELECT Sharecode FROM SHARECODE WHERE Sharecode=?""",(code,))
    result = cur.fetchone()
    if result:
        cur.execute("SELECT * FROM SHARECODE WHERE Sharecode=?", (code,))
        rows = cur.fetchall()
        code = rows[0][1]
        conn.close()
        return code
    else:
        conn.close()
        return False

def generatenum():
    IsNotUnique = True
    while IsNotUnique:
        num = random.randint(100000,999999)
        if pullsharecodedata(num) == False:
            IsNotUnique = False
            return num

def generatecode(modeljson):
    hash = hashit(modeljson)
    chhash = checkifexisthash(hash)
    if chhash != False:
        return chhash
    sharecode = generatenum()
    addtodb(sharecode, modeljson, hash)
    return {"sharecode": sharecode, "modeljson": modeljson}
    



    
 

    

    
  