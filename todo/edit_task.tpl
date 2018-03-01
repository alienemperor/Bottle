%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</head>
<body>
<p>Edit the task with ID = {{no}}</p>
<form action="/edit/{{no}}" method="get">
    <div class="form-group">
        <input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">
    </div>
    <div class="form-group">
        <select name="status">
            <option>open</option>
            <option>closed</option>
        </select>
    </div>
    <div class="form-group">
        <br>
        <input type="submit" name="save" value="save">
    </div>

</form>
</body>
<!--
<p>Edit the task with ID = {{no}}</p>
<form action="/edit/{{no}}" method="get">
  <input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">
  <select name="status">
    <option>open</option>
    <option>closed</option>
  </select>
  <br>
  <input type="submit" name="save" value="save">
</form>
-->
