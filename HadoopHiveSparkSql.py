from SqlLoader import SqlLoader


class HadoopHiveSparkSql:

    @staticmethod
    def table(tableName):
        return SqlLoader().table(tableName)


# print(HadoopHiveSparkSql.table("employee")
#       .select("id,name")
#       .select(",department")
#       .where("ram=(select id from users)")
#       .where("city=", "delhi")
#       .orWhere("seller=",'100')
#       .orWhere("brand=",'rock')
#       .orHaving("seller=",'100')
#       .having("city=", "delhi")
#       .orHaving("brand=",'rock')
#       .whereBetween("age",[200,300])
#       .join("users","users.id=employee.emp_id","left")
#       .join("cars","cars.id=employee.emp_id")
#       .groupBy("name")
#       .orderBy("ID","desc")
#       .limit(10,20).get())
