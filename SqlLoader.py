import cgi


class SqlLoader:
    selectList = list()
    tableName = ""
    whereList = list()
    sqlLimit = str("")
    sqlJoinList = list()

    def table(self, tableName):
        self.tableName = tableName
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

    async def doThread(self, parameter_list):
        print("Jai Ho")

    def select(self, value):
        self.selectList.append(value)
        return self

    def where(self, keyOrRaw, value=""):
        if not value:
            self.whereList.append(keyOrRaw)
        else:
            self.whereList.append(keyOrRaw+"'"+cgi.escape(value)+"'")
        return self

    def limit(self, limitValue, offset=""):
        if not offset:
            self.sqlLimit = " LIMIT "+limitValue
        else:
            self.sqlLimit = " LIMIT "+offset+","+limitValue
        return self

    def get(self):
        sql = "SELECT "
        if not self.selectList:
            sql += "* "
        else:
            sql += ("".join(self.selectList)).strip()

        sql += " FROM "+self.tableName

        if self.whereList:
            sql += " WHERE "+(" AND ".join(self.whereList)).strip()
        return sql
