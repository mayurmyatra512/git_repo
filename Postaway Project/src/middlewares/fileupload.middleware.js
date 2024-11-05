// Import necessary modules
import multer from 'multer';
import fs from 'fs';
import path from 'path';

// Define the upload directory and ensure it exists
const uploadDir = path.resolve('./uploads');
if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir, { recursive: true });
}

// Configure multer storage with filename and location
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, uploadDir); // Use resolved path for consistency
    },
    filename: (req, file, cb) => {
        const uniqueSuffix = new Date().toISOString().replace(/:/g, '-') + '-' + file.originalname;
        cb(null, uniqueSuffix);
    },
});

// Export the multer upload configuration
export const upload = multer({
    storage: storage,
});