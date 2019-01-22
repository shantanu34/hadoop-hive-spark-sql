from SqlLoader import SqlLoader

class HadoopHiveSparkSql:
    
    @staticmethod
    def table(tableName):
        return SqlLoader().setTable(tableName)
    

        
print(HadoopHiveSparkSql.table("employee").setSelect("id,name").setSelect(",department").get())