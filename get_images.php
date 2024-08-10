<?php
// Directory where your images are stored
$imageDir = "QRcodes/";

// Array to store image filenames
$imageFiles = [];

// Check if the directory exists
if (file_exists($imageDir)) {
    // Open the directory
    $dir = opendir($imageDir);

    // Initialize variables for tracking the most recently modified file
    $latestFile = '';
    $latestModTime = 0;

    // Read directory contents
    while (($file = readdir($dir)) !== false) {
        // Check if the file is an image
        if (is_file($imageDir . $file) && in_array(pathinfo($file, PATHINFO_EXTENSION), array("jpg", "jpeg", "png", "gif"))) {
            // Get the file modification time
            $modTime = filemtime($imageDir . $file);
            // Check if this file is more recent than the previously recorded one
            if ($modTime > $latestModTime) {
                $latestModTime = $modTime;
                $latestFile = $file;
            }
        }
    }

    // Close the directory handle
    closedir($dir);

    // Add the most recently modified file to the array
    if (!empty($latestFile)) {
        $imageFiles[] = $latestFile;
    }
} else {
    echo "Directory not found.";
}

// Output image filenames as JSON
header('Content-Type: application/json');
echo json_encode($imageFiles);
?>
