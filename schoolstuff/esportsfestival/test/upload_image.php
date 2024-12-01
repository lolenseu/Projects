<?php
// Include database connection
include('connection.php');

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['image'])) {
    // Get the form data
    $username = $_POST['username'];
    $email = $_POST['email'];
    $image = $_FILES['image'];

    // Validate file upload
    if ($image['error'] === UPLOAD_ERR_OK) {
        // Read the image file content into a binary string
        $imageData = file_get_contents($image['tmp_name']);

        // Prepare the SQL query to insert the image and user details
        $sql = "INSERT INTO user_images (username, email, profile_image) VALUES (?, ?, ?)";
        $stmt = $conn->prepare($sql);
        
        // Bind the parameters to the SQL query
        $stmt->bind_param("sss", $username, $email, $imageData);

        // Execute the query
        if ($stmt->execute()) {
            echo "Image uploaded successfully!";
        } else {
            echo "Error uploading image. Please try again.";
        }

        $stmt->close();
    } else {
        echo "Error uploading file.";
    }
} else {
    echo "Invalid request.";
}
?>
