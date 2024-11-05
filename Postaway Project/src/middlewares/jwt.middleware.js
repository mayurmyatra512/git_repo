import jwt from 'jsonwebtoken'

const jwtAuth = (req, res, next) =>{
    //1. Read The token
    const token = req.headers['authorization'];

    // const token = req.cookies.jwtToken;
    //2. If no token, return the error
    if(!token){
        return res.status(401).send("Unauthorized")
    }

//3. Check if Token is valid or not.    
    try {
        const payload = jwt.verify(token, 'MwRyYnzzcYlFEAkuhB9s3yoYt2oLYVGC');   
        req.userId = payload.userID;
        // console.log(payload) 
    } catch (error) {
        //4. return error
        return res.status(401).send("Unauthorized");
    }

    //5. call next middleware

    next();
}

export default jwtAuth;