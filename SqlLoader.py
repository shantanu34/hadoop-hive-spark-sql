import cgi

class SqlLoader:
    selectList = list()
    tableName = ""
    whereList = list()
    orWhereList = list()
    sqlLimit = str("")
    sqlJoinList = list()

    def table(self, tableName):
        self.tableName = tableName
        return self

    def whereBetween(self, key, pointsList=[]):
        if not pointsList[1]:
            pointsList[1] = pointsList[0]
        self.whereList.append(key + ">= "+str(pointsList[0])+" AND "+key + "<= "+str(pointsList[1]))
        return self

    def join(self, tableName, whereText, joinType="INNER"):
        joinType = joinType.strip().upper()
        if joinType == "INNER" or joinType == "JOIN":
            self.sqlJoinList.append("INNER JOIN "+tableName+" ON "+whereText)
        if joinType == "LEFT":
            self.sqlJoinList.append("LEFT JOIN "+tableName+" ON "+whereText)
        if joinType == "RIGHT":
            self.sqlJoinList.append("RIGHT JOIN "+tableName+" ON "+whereText)
        if joinType == "FULL OUTER":
            self.sqlJoinList.append(
                "FULL OUTER JOIN "+tableName+" ON "+whereText)
        if joinType not in ['FULL OUTER', 'INNER', 'LEFT', 'RIGHT', 'JOIN']:
            self.sqlJoinList.append(joinType+" "+tableName+" ON "+whereText)
        return self

    def select(self, value):
        self.selectList.append(value)
        return self

    def where(self, keyOrRaw, value=""):
        if not value:
            self.whereList.append(keyOrRaw)
        else:
            self.whereList.append(keyOrRaw+"'"+cgi.escape(str(value))+"'")
        return self

    def orWhere(self, keyOrRaw, value=""):
        if not value:
            self.orWhereList.append(keyOrRaw)
        else:
            self.orWhereList.append(keyOrRaw+"'"+cgi.escape(str(value))+"'")
        return self

    def limit(self, limitValue, offset=0):
        if not offset:
            self.sqlLimit = " LIMIT "+limitValue
        else:
            self.sqlLimit = " LIMIT "+str(offset)+","+str(limitValue)
        return self

    def get(self):
        sql = "SELECT "
        if not self.selectList:
            sql += "* "
        else:
            sql += ("".join(self.selectList)).strip()

        sql += " FROM "+self.tableName     
        if self.sqlJoinList:
            sql +=  " "+(" ".join(self.sqlJoinList)).strip()
        if self.whereList or self.orWhereList:
            sql += " WHERE "
        if self.whereList:
            sql += (" AND ".join(self.whereList)).strip()
        if self.orWhereList:
            if len(self.orWhereList)==1:
                sql+=" OR "
            else:
                sql+=" AND ("
            sql += (" OR ".join(self.orWhereList)).strip()
            if len(self.orWhereList)>1:
                sql+=")"
        if self.sqlLimit:
            sql+=self.sqlLimit
        return sql.strip()
