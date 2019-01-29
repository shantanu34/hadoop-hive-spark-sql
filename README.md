# hadoop-hive-spark-sql
Under initial stage big-data sql

<h1>Selects</h1>
<br/><p>
Specifying A Select Clause
Of course, you may not always want to select all columns from a database table. Using the  select method, you can specify a custom select clause for the query:</p>

<code>
$users = DB::table('users')->select('name', 'email as user_email')->get();
</code>
<br/>The distinct method allows you to force the query to return distinct results:

<code>$users = DB::table('users')->distinct()->get();</code>
If you already have a query builder instance and you wish to add a column to its existing select clause, you may use the addSelect method:

$query = DB::table('users')->select('name');

$users = $query->addSelect('age')->get();

Raw Expressions
Sometimes you may need to use a raw expression in a query. These expressions will be injected into the query as strings, so be careful not to create any SQL injection points! To create a raw expression, you may use the DB::raw method:

$users = DB::table('users')
                     ->select(DB::raw('count(*) as user_count, status'))
                     ->where('status', '<>', 1)
                     ->groupBy('status')
                     ->get();

