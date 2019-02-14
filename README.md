# hadoop-hive-spark-sql
SQL framework ORM independent, it helps you build sql query in python<br/>
What ever you using Hive, HBase, Spark* SQL, Django & FLASK etc so you can gernate simple SQL query<br/>
Its return raw sql query string this can be use in Framework<br/>



<!--New Section **************************-->
<br/><h4>Select</h4>
<br/>
<code>
HadoopHiveSparkSql.table("employee") .select("id,name") .select(",department").get()
</code>



<!--New Section **************************-->
<br/><h4>Where</h4>
You can use key and value based parameters : where("city=", "ABC")<br>
Or you can use raw where query : 
where("col=(select id from users)")
<br/>
<code>
HadoopHiveSparkSql.table("employee") .select("id,name").select(",department").where("ram=(select id from users)").where("city=", "delhi").get()
</code>

<!--New Section **************************-->
<br/><h4>OrWhere and WhereBetween</h4>
If you want data according min and max  use : <br/>
<code>
whereBetween("age",[200,300]) 
HadoopHiveSparkSql.table("employee") .select("id,name") .whereBetween("age",[200,300]) .get()
</code><br/>
Using OR with where :<br>
<code>
HadoopHiveSparkSql.table("employee") .select("id,name") .orWhere("seller=",'100').get()
</code>


<!--New Section **************************-->
<br/><h4>GroupBy, OrderBy amd Limit
</h4>
Use of group by : groupBy("name")

<br><code>HadoopHiveSparkSql.table("employee") .select("id,name") .groupBy("name") .get()

Use order by : orderBy("ID","desc") 

<br><code>HadoopHiveSparkSql.table("employee") .select("id,name") .orderBy("ID","desc") .get()</code>

use with limit : imit(10,20)

<br><code>HadoopHiveSparkSql.table("employee") .select("id,name") .limit(10,20).get()</code><br/>


<!--New Section **************************-->
<br/><h4>____________</h4>
---------------------------------------------
<br/>
<code>
print(HadoopHiveSparkSql.table("employee")
      .select("id,name")
      .select(",department")
      .where("ram=(select id from users)")
      .where("city=", "delhi")
      .orWhere("seller=",'100')
      .orWhere("brand=",'rock')
      .whereBetween("age",[200,300])
      .join("users","users.id=employee.emp_id","left")
      .join("cars","cars.id=employee.emp_id")
      .groupBy("name")
      .orderBy("ID","desc")
      .limit(10,20).get())
</code>



<!--New Section **************************-->
<br/><h4>____________</h4>
---------------------------------------------
<br/>
<code>
print(HadoopHiveSparkSql.table("employee")
      .select("id,name")
      .select(",department")
      .where("ram=(select id from users)")
      .where("city=", "delhi")
      .orWhere("seller=",'100')
      .orWhere("brand=",'rock')
      .whereBetween("age",[200,300])
      .join("users","users.id=employee.emp_id","left")
      .join("cars","cars.id=employee.emp_id")
      .groupBy("name")
      .orderBy("ID","desc")
      .limit(10,20).get())
</code>


<!--New Section **************************-->
<br/><h4>____________</h4>
---------------------------------------------
<br/>
<code>
print(HadoopHiveSparkSql.table("employee")
      .select("id,name")
      .select(",department")
      .where("ram=(select id from users)")
      .where("city=", "delhi")
      .orWhere("seller=",'100')
      .orWhere("brand=",'rock')
      .whereBetween("age",[200,300])
      .join("users","users.id=employee.emp_id","left")
      .join("cars","cars.id=employee.emp_id")
      .groupBy("name")
      .orderBy("ID","desc")
      .limit(10,20).get())
</code>