<?php
// Database connection
include('php/connection.php');

// Increment view count in `web_views`
$sql_increment_view = "UPDATE web_views SET views = views + 1 WHERE id = 1";
$conn->query($sql_increment_view);

// Fetch updated views count
$sql_get_views = "SELECT views FROM web_views WHERE id = 1";
$result = $conn->query($sql_get_views);
$views_count = $result->fetch_assoc()['views'] ?? 0;

// Fetch total users
$sql_get_users_count = "SELECT COUNT(*) AS total_users FROM users_data";
$result = $conn->query($sql_get_users_count);
$total_users = $result->fetch_assoc()['total_users'] ?? 0;

// Fetch total verified users
$sql_get_verified_users = "SELECT COUNT(*) AS verified_users FROM users_data WHERE image IS NOT NULL AND LENGTH(image) > 0";
$result = $conn->query($sql_get_verified_users);
$verified_users = $result->fetch_assoc()['verified_users'] ?? 0;

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>About</title>
  <link rel="stylesheet" href="css/header.css">
  <link rel="stylesheet" href="css/about.css">
  <link rel="stylesheet" href="css/footer.css">
  <link rel="icon" href="img/icon.png">
</head>
<body>
  <!-- Header -->
  <div class="header">
    <a href="#" class="logo"><img src="img/2024.png">ESports<br>Festival</a>
    <div class="header-right">
      <a href="index.html">Home</a>
      <a class="active" href="about.php">About</a>
      <a href="register.html">Register</a>
      <a href="contact.html">ContactUs</a>
    </div><br>
    <div class="searchbox">
      <form action="php/search_handler.php" method="GET">
        <button type="submit">Search</button>
        <input type="text" name="search" placeholder="Enter a keyword..." required>
      </form>
    </div>
  </div>

  <div class="intro-img">
    <img src="img/gamplay.jpg" alt="">
    <div class="user-counter">
      <div class="user-counter-content ani">
        <p>Users<img src="img/user.png" alt=""> <?php echo $total_users; ?></p>
        <p>Verified<img src="img/check.png" alt=""> <?php echo $verified_users; ?></p>
        <p>Visitor<img src="img/eye.png" alt=""> <?php echo $views_count; ?></p>
      </div>
    </div>
  </div>
  
  <!-- Content -->
  <div class="content">
    <div class="content-box">
      <div class="fist-content ani">
        <h1>ABOUT ESPORTS FESTIVAL</h1>
        <div class="content1 ani">
          <img src="img/imga1.jpg" alt="">
          <p>Founded in 2022, the ESports Festival celebrates all things gaming. By combining the best in competitive video games with electrifying experiences and next-gen talent, the annual festival aims to become a regular fixture in the international circuit.</p>
        </div>
        <div class="content2 ani">
          <img src="img/imga2.jpg" alt="">
          <p>Over thousands of players and hundred teams competing every year, the ESports Festival has become a global stage for showcasing talent and teamwork. From underdog stories to legendary rivalries, each year brings a new wave of champions hungry for victory. These players push the limits of strategy, skill, and endurance, making every match a thrilling experience for fans around the world.</p>
        </div>
        <div class="content3 ani">
          <img src="img/imga3.jpg" alt="">
          <p>Following the phenomenal success of ESports Festival 2023, which attracted over 26,000 visitors and 75,000 gaming enthusiasts, this year's festival is poised to deliver an even more unforgettable adventure over 10 days with events happening across the city.</p>
        </div>
      </div>
    </div>
  </div> 

  <!-- Footer -->
  <footer>
    <h4>© Copyright 2024 | ESports Festival</h4>
  </footer>

  <!-- Animation Script -->
  <script src="javascript/script.js"></script>
</body>
</html>
