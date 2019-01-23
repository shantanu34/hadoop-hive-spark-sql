from SqlLoader import SqlLoader

class HadoopHiveSparkSql:
    
    @staticmethod
    def table(tableName):
        return SqlLoader().table(tableName)
    

        
print(HadoopHiveSparkSql.table("employee").select("id,name").select(",department").get())