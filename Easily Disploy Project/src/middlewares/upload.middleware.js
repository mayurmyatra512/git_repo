import multer from "multer";
import path from 'path';

let cvLoc = path.join(path.resolve(), 'src', 'uploads');
        // const resumePath = cvLoc + req.file.filename;
const storageConfig = multer.diskStorage({
    destination:(req, file, cb)=>{
        cb(null, cvLoc);
    },
    filename:(req, file, cb)=>{
        const name = Date.now() + "-" + file.originalname;
        cb(null, name);
    }
})

export const uploadFile = multer({
    storage: storageConfig,
})