<?php
// Database connection
include('connection.php');

// Error flag
$message = '';

if (isset($_GET['id']) && isset($_POST['currentpassword'])) {
    $userId = $_GET['id'];
    $currentPassword = $_POST['currentpassword'];

    // Fetch user data from the database based on the id
    $sql = "SELECT * FROM users_data WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $userId);
    $stmt->execute();
    $result = $stmt->get_result();

    // Check if the user exists and verify the password
    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        if (password_verify($currentPassword, $user['password'])) {
            // Delete the user if password is correct
            $deleteSql = "DELETE FROM users_data WHERE id = ?";
            $deleteStmt = $conn->prepare($deleteSql);
            $deleteStmt->bind_param("i", $userId);
            $deleteStmt->execute();

            // Execute the statement
            if ($stmt->execute()) {
              $message = 'Your account has been successfully deleted.';
            } else {
                $message = "Error: " . $conn->error;
            }
        } else {
            $message = 'Incorrect password. Please try again.';
        }
    } else {
        $message = 'User not found. Please check the user ID.';
    }
} else {
    $message = 'User ID or password not provided.';
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Delete Status</title>
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/delete_handler.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="icon" href="../img/icon.png">
</head>
<body>
  <!-- Header -->
  <div class="header">
    <a href="#" class="logo"><img src="../img/2024.png">ESports<br>Festival</a>
    <div class="header-right">
      <a href="../index.html">Home</a>
      <a href="../index2.html">About</a>
      <a href="../index3.html">Register</a>
      <a href="../index4.html">ContactUs</a>
    </div><br>
    <div class="searchbox">
      <form action="search_handler.php" method="GET">
        <button type="submit">Search</button>
        <input type="text" name="search" placeholder="Enter a keyword..." required>
      </form>
    </div>
  </div>

  <!-- Content -->
  <div class="content">
    <div class="content-box">
    <h2>Delete Status</h2>
      <?php if ($message): ?>
        <p><?php echo $message; ?></p>
      <?php endif; ?>
      <a href="../index.html">Go back to Home</a>
    </div>
  </div>

  <!-- Footer -->
  <footer>
    <h4>© Copyright 2024 | ESports Festival</h4>
  </footer>
</body>
</html>
