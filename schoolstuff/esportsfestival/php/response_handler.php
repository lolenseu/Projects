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

    // Validate required fields
    if (empty($userName) || empty($userEmail) || empty($userMessage)) {
        $message = "All fields are required. Please fill out the form completely.";
    } else {
        try {
            // Insert the message into the database
            $sql = "INSERT INTO users_response (username, email, message) VALUES (?, ?, ?)";
            $stmt = $pdo->prepare($sql);
            $stmt->execute([$userName, $userEmail, $userMessage]);

            $message = "Thank you, " . htmlspecialchars($userName) . ". Your message has been submitted.";
        } catch (PDOException $e) {
            $message = "Failed to submit your message: " . $e->getMessage();
        }
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
