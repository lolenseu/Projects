<?php
// Database connection
include('connection.php');

// Response message
$messageok = "";
$messagebad = "";

// Check if the user is logged in and the 'id' and 'currentpassword' are set
if (isset($_GET['id']) && isset($_POST['currentpassword'])) {
    $userId = $_GET['id'];
    $currentPassword = $_POST['currentpassword']; 

    // Fetch the user's current details from the database
    $sql = "SELECT * FROM users_data WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $userId);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();

        // Check if the entered current password matches the stored password
        if (password_verify($currentPassword, $user['password'])) {

            // Prepare the update query
            $updateSql = "UPDATE users_data SET ";
            $updateParams = [];
            $updateQuery = [];

            // Collect input values
            $newUsername = $_POST['username'] ?? '';
            $newEmail = $_POST['email'] ?? '';
            $newPassword = $_POST['password'] ?? '';
            $newContact = $_POST['contact'] ?? '';
            $newAddress = $_POST['address'] ?? '';
            $newAge = $_POST['age'] ?? '';
            $newBirthday = $_POST['birthday'] ?? '';
            $newRole = $_POST['role'] ?? '';
            $newImage = $_FILES['image'] ?? null;

            // Check and update fields if the new value is not empty
            if (!empty($newUsername) && $newUsername !== $user['username']) {
                $updateQuery[] = "username = ?";
                $updateParams[] = $newUsername;
            }
            if (!empty($newEmail) && $newEmail !== $user['email']) {
                $updateQuery[] = "email = ?";
                $updateParams[] = $newEmail;
            }
            if (!empty($newPassword)) {
                $updateQuery[] = "password = ?";
                $updateParams[] = password_hash($newPassword, PASSWORD_DEFAULT); // Hash the new password
            }
            if (!empty($newContact) && $newContact !== $user['contact']) {
                $updateQuery[] = "contact = ?";
                $updateParams[] = $newContact;
            }
            if (!empty($newAddress) && $newAddress !== $user['address']) {
                $updateQuery[] = "address = ?";
                $updateParams[] = $newAddress;
            }
            if (!empty($newAge) && $newAge != $user['age']) {
                $updateQuery[] = "age = ?";
                $updateParams[] = $newAge;
            }
            if (!empty($newBirthday) && $newBirthday != $user['birthday']) {
                $updateQuery[] = "birthday = ?";
                $updateParams[] = $newBirthday;
            }
            if (!empty($newRole) && $newRole != $user['role']) {
                $updateQuery[] = "role = ?";
                $updateParams[] = $newRole;
            }

            // Handle profile image update if new image is uploaded
            if ($newImage && $newImage['error'] === UPLOAD_ERR_OK) {
                // Read the image file content into a binary string
                $imageData = file_get_contents($newImage['tmp_name']);
                $updateQuery[] = "image = ?";
                $updateParams[] = $imageData; // Add the binary data of the image
            }

            // If there are changes, proceed with the update
            if (count($updateQuery) > 0) {
                $updateSql .= implode(", ", $updateQuery) . " WHERE id = ?";
                $updateParams[] = $userId; // Add user ID as last parameter for the WHERE clause

                // Prepare and execute the update statement
                $stmt = $conn->prepare($updateSql);
                // Adjust binding based on the number of parameters, ensuring the last is an integer for userId
                $stmt->bind_param(str_repeat('s', count($updateParams) - 1) . 'i', ...$updateParams); 
                if ($stmt->execute()) {
                    $messageok = "Your profile has been successfully updated!";
                } else {
                    $messagebad = "There was an error updating your profile. Please try again later.";
                }
            } else {
                $messagebad = "No changes were made to your profile.";
            }
        } else {
            $messagebad = "Incorrect current password. Please try again.";
        }
    } else {
        $messagebad = "User not found.";
    }
} else {
    $messagebad = "Invalid request. Please make sure both ID and current password are provided.";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Update Status</title>
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/update_handler.css">
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
      <h2>Update Status</h2>
      <?php if ($messageok): ?>
        <p><?php echo $messageok; ?></p>
        <a href="profile_handler.php?id=<?php echo $userId; ?>">Go back to Profile</a>
      <?php elseif ($messagebad): ?>
        <p><?php echo $messagebad; ?></p>
        <a href="javascript:history.back()">Go back to Profile</a>
      <?php endif; ?>
    </div>
  </div>

  <!-- Footer -->
  <footer>
    <h4>© Copyright 2024 | ESports Festival</h4>
  </footer>
</body>
</html>
