<?php
    // getting all values from the HTML form
    if(isset($_POST['submit']))
    {
        $name1 = $_POST['Name'];
        $age = $_POST['Age'];
        $gender = $_POST['Gender'];
        $nation = $_POST['Nation'];
        $address = $_POST['Address'];
        $contact_no = $_POST['Contact Number'];
        $password = $_POST['Password'];
        $confirm_password = $_POST['Confirm Password']
    }

    // database details
    $host = "localhost";
    $username = "root";
    $password = "parvathy";
    $dbname = "intouch";

    // creating a connection
    $con = mysqli_connect($host, $username, $password, $dbname);

    // to ensure that the connection is made
    if (!$con)
    {
        die("Connection failed!" . mysqli_connect_error());
    }

    // using sql to create a data entry query
    $sql = "INSERT INTO contactform_entries (Name, Age, Gender, Nation, Address, Contact_Number, Password, Confirm_Password) VALUES ('$name', '$age', '$gender', '$nation', '$address', '$contact_no', '$password', '$confirm_password')";
  
    // send query to the database to add values and confirm if successful
    $rs = mysqli_query($con, $sql);
    if($rs)
    {
        echo "Entries added!";
    }
  
    // close connection
    mysqli_close($con);

?>