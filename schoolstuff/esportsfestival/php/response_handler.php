<?php
// Database connection
include('connection.php');

// Response message
$message = ""; 

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data and validate inputs
    $userName = $_POST['username'] ?? '';
    $userEmail = $_POST['email'] ?? '';
    $userMessage = $_POST['message'] ?? '';

    // Reset AUTO_INCREMENT to avoid large gaps in IDs
    $resetSql = "SELECT MAX(id) AS max_id FROM users_response";
    $resetResult = $conn->query($resetSql);
    if ($resetRow = $resetResult->fetch_assoc()) {
      $newAutoIncrement = $resetRow['max_id'] + 1;
      $conn->query("ALTER TABLE users_response AUTO_INCREMENT = $newAutoIncrement");
    }

    // Prepare and execute the SQL query to insert the data into the database
    $sql = "INSERT INTO users_response (username, email, message) VALUES (?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sss", $userName, $userEmail, $userMessage);
            
    // Execute the statement
    if ($stmt->execute()) {
        $message = "Thank you, " . htmlspecialchars($userName) . ". Your message has been submitted successfully!";
    } else {
        $message = "Failed to submit your message: " . $conn->error;
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Message Status</title>
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/response_handler.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="icon" href="../img/icon.png">
</head>
<body>
  <!-- Header -->
  <div class="header">
    <a href="#" class="logo"><img src="../img/2024.png">ESports<br>Festival</a>
    <div class="header-right">
      <a href="../index.html">Home</a>
      <a href="../about.php">About</a>
      <a href="../register.html">Register</a>
      <a href="../contact.html">ContactUs</a>
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
      <h2>Message Status</h2>
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
