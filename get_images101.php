<?php
// Directory where your images are stored
$imageDir = "QRcodes/";

// Array to store image filenames
$imageFiles = [];

// Check if the directory exists
if (file_exists($imageDir)) {
    // Open the directory
    $dir = opendir($imageDir);

    // Read directory contents
    while (($file = readdir($dir)) !== false) {
        // Check if the file is an image
        if (is_file($imageDir . $file) && in_array(pathinfo($file, PATHINFO_EXTENSION), array("jpg", "jpeg", "png", "gif"))) {
            $imageFiles[] = $file;
        }
    }

    // Close the directory handle
    closedir($dir);
} else {
    echo "Directory not found.";
}

// Output image filenames as JSON
header('Content-Type: application/json');
echo json_encode($imageFiles);
?>
